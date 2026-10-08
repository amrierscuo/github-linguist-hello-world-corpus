__constant uchar greeting[13] = {72,101,108,108,111,44,32,87,111,114,108,100,33};
__kernel void hello(__global uchar *output) {
    size_t i = get_global_id(0);
    if (i < 13) output[i] = greeting[i];
}
