"""Build and dispatch the unchanged OpenCL kernel on the PoCL CPU runtime."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pyopencl as cl

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source", type=Path, help="hello.cl or the .opencl variant")
args = parser.parse_args()
source_bytes = args.source.read_bytes()
devices = [
    (platform, device)
    for platform in cl.get_platforms()
    if "Portable Computing Language" in platform.name
    for device in platform.get_devices(device_type=cl.device_type.CPU)
]
assert devices, "PoCL CPU OpenCL device required"
platform, device = devices[0]
context = cl.Context([device])
expected = b"Hello, World!"
assert len(expected) == 13
sentinel = 255
host_output = np.full(21, sentinel, dtype=np.uint8)
with cl.CommandQueue(context) as queue:
    program = cl.Program(context, source_bytes.decode("utf-8")).build(
        options=["-cl-std=CL1.2"]
    )
    # OpenCL defines CL_BUILD_SUCCESS as 0; older PyOpenCL does not expose build_status.
    assert program.get_build_info(device, cl.program_build_info.STATUS) == 0
    output_buffer = cl.Buffer(
        context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=host_output
    )
    kernel = cl.Kernel(program, "hello")
    kernel.set_args(output_buffer)
    dispatch = cl.enqueue_nd_range_kernel(queue, kernel, (13,), None)
    cl.enqueue_copy(queue, host_output, output_buffer, wait_for=[dispatch], is_blocking=True)
    queue.finish()
    assert dispatch.command_execution_status == cl.command_execution_status.COMPLETE
    assert host_output[:13].tobytes() == expected, host_output.tolist()
    assert np.all(host_output[13:] == sentinel), host_output.tolist()
print(json.dumps({
    "source": args.source.name,
    "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
    "pyopencl_version": cl.VERSION_TEXT,
    "numpy_version": np.__version__,
    "platform": {"name": platform.name, "vendor": platform.vendor, "version": platform.version},
    "device": {"name": device.name, "type": "CPU", "version": device.version,
               "driver_version": device.driver_version, "opencl_c_version": device.opencl_c_version},
    "build_options": ["-cl-std=CL1.2"],
    "build_log": program.get_build_info(device, cl.program_build_info.LOG),
    "global_work_items": 13,
    "readback_bytes": host_output[:13].tolist(),
    "readback_ascii": host_output[:13].tobytes().decode("ascii"),
    "guard_bytes_unchanged": bool(np.all(host_output[13:] == sentinel)),
    "assertion": "PASS: real OpenCL kernel dispatch writes Hello, World! and preserves guard bytes",
}, indent=2))
