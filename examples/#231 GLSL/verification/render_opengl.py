"""Execute exact GLSL fragment/geometry sources in an OpenGL EGL context."""
import argparse
import hashlib
import importlib.metadata
import json
import pathlib
import platform
import struct
import moderngl

parser = argparse.ArgumentParser()
parser.add_argument('--stage', choices=['frag', 'geom'], required=True)
parser.add_argument('files', nargs='+', type=pathlib.Path)
args = parser.parse_args()
ctx = moderngl.create_context(standalone=True, backend='egl', require=450)
expected = b'Hello, World!'
results = []
for path in args.files:
    source_bytes = path.read_bytes()
    source = source_bytes.decode('utf-8')
    if args.stage == 'frag':
        vertex = """#version 450
void main() {
    const vec2 position[3] = vec2[3](vec2(-1,-1), vec2(3,-1), vec2(-1,3));
    gl_Position = vec4(position[gl_VertexID],0,1);
}
"""
        program = ctx.program(vertex_shader=vertex, fragment_shader=source)
        fbo = ctx.simple_framebuffer((13, 1), components=3, dtype='f1')
        fbo.use()
        fbo.clear(0, 0, 0, 1)
        vao = ctx.vertex_array(program, [])
        vao.render(vertices=3)
        pixels = fbo.read(components=3, alignment=1)
        required = bytes(channel for value in expected for channel in [value]*3)
        assert pixels == required, (path, list(pixels))
        decoded = bytes(pixels[0::3]).decode('ascii')
        result = {'measurement': '13x1 RGB8 framebuffer readback',
                  'rgb_bytes': list(pixels), 'ascii_bytes': list(pixels[0::3]),
                  'decoded': decoded, 'exact_rgb_match': pixels == required}
        vao.release()
        fbo.release()
        program.release()
    else:
        vertex = '#version 450\nvoid main() { gl_Position=vec4(0,0,0,1); }\n'
        program = ctx.program(vertex_shader=vertex, geometry_shader=source,
                              varyings=['greeting_value'])
        fbo = ctx.simple_framebuffer((1, 1))
        fbo.use()
        vao = ctx.vertex_array(program, [])
        buffer = ctx.buffer(reserve=13 * 4)
        with ctx.query(primitives=True) as query:
            vao.transform(buffer, mode=moderngl.POINTS, vertices=1)
        data = buffer.read()
        values = list(struct.unpack('<13f', data))
        ascii_bytes = [round(value * 255) for value in values]
        max_error = max(abs(value - wanted/255) for value, wanted in zip(values, expected))
        assert query.primitives == 13, query.primitives
        assert ascii_bytes == list(expected), ascii_bytes
        assert max_error < 1e-6, max_error
        result = {'measurement': 'geometry stage transform feedback and primitive query',
                  'emitted_points': query.primitives,
                  'raw_float_values': values, 'raw_buffer_hex': data.hex(),
                  'ascii_bytes': ascii_bytes, 'decoded': bytes(ascii_bytes).decode('ascii'),
                  'max_float_error': max_error}
        vao.release()
        buffer.release()
        fbo.release()
        program.release()
    result.update(source_file=path.as_posix(),
                  source_sha256=hashlib.sha256(source_bytes).hexdigest(),
                  shader_stage=args.stage)
    results.append(result)
print(json.dumps({'platform': platform.platform(), 'python': platform.python_version(),
                  'moderngl': importlib.metadata.version('moderngl'),
                  'glcontext': importlib.metadata.version('glcontext'),
                  'context_version': ctx.version_code,
                  'renderer': ctx.info.get('GL_RENDERER'), 'vendor': ctx.info.get('GL_VENDOR'),
                  'version': ctx.info.get('GL_VERSION'),
                  'results': results}, indent=2))
ctx.release()
