#pragma version(1)
#pragma rs java_package_name(org.corpus.greeting)

uchar __attribute__((kernel)) root(uint32_t x) {
    switch (x) {
        case 0: return 72;
        case 1: return 101;
        case 2: return 108;
        case 3: return 108;
        case 4: return 111;
        case 5: return 44;
        case 6: return 32;
        case 7: return 87;
        case 8: return 111;
        case 9: return 114;
        case 10: return 108;
        case 11: return 100;
        case 12: return 33;
        default: return 0;
    }
}
