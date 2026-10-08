program corpus_hello_world.aleo;

function greeting:
    cast 72u8 101u8 108u8 108u8 111u8 44u8 32u8 87u8 111u8 114u8 108u8 100u8 33u8 into r0 as [u8; 13u32];
    output r0 as [u8; 13u32].public;
