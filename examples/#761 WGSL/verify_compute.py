"""Dispatch the corpus WGSL shader and verify the storage buffer readback."""
import hashlib
import json
from pathlib import Path
import struct

import wgpu
from wgpu.backends import wgpu_native

shader_path = Path(__file__).with_name("hello.wgsl")
shader_bytes = shader_path.read_bytes()
adapter = wgpu.gpu.request_adapter_sync(
    power_preference="low-power", force_fallback_adapter=True
)
adapter_info = dict(adapter.info)
assert adapter_info["adapter_type"] == "CPU", adapter_info
assert adapter_info["backend_type"] == "Vulkan", adapter_info
device = adapter.request_device_sync()
output = device.create_buffer(
    size=13 * 4,
    usage=wgpu.BufferUsage.STORAGE | wgpu.BufferUsage.COPY_SRC | wgpu.BufferUsage.COPY_DST,
)
device.queue.write_buffer(output, 0, bytes(13 * 4))
shader = device.create_shader_module(code=shader_bytes.decode("utf-8"))
pipeline = device.create_compute_pipeline(
    layout="auto", compute={"module": shader, "entry_point": "main"}
)
group = device.create_bind_group(
    layout=pipeline.get_bind_group_layout(0),
    entries=[{"binding": 0, "resource": {"buffer": output, "offset": 0, "size": 13 * 4}}],
)
encoder = device.create_command_encoder()
compute = encoder.begin_compute_pass()
compute.set_pipeline(pipeline)
compute.set_bind_group(0, group)
compute.dispatch_workgroups(1)
compute.end()
device.queue.submit([encoder.finish()])
readback = bytes(device.queue.read_buffer(output))
codes = list(struct.unpack("<13I", readback))
expected = list(b"Hello, World!")
assert codes == expected, codes
greeting = bytes(codes).decode("ascii")
print(json.dumps({
    "wgpu_version": wgpu.__version__,
    "wgpu_native_version": list(wgpu_native.lib_version_info),
    "adapter": adapter_info,
    "shader_sha256": hashlib.sha256(shader_bytes).hexdigest(),
    "dispatch_workgroups": [1, 1, 1],
    "workgroup_size": [13, 1, 1],
    "readback_u32": codes,
    "greeting": greeting,
}, sort_keys=True))
print(greeting)
