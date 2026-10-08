pragma circom 2.0.0;

template Greeting() {
    signal output text[13];
    var codes[13] = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33];
    for (var i = 0; i < 13; i++) {
        text[i] <== codes[i];
    }
}

component main = Greeting();
