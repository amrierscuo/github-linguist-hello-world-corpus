@group(0) @binding(0) var<storage, read_write> output: array<u32>;

@compute @workgroup_size(13)
fn main(@builtin(global_invocation_id) id: vec3<u32>) {
    let codes = array<u32, 13>(72u, 101u, 108u, 108u, 111u, 44u, 32u, 87u, 111u, 114u, 108u, 100u, 33u);
    if (id.x < 13u) { output[id.x] = codes[id.x]; }
}
