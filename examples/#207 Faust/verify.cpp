#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>

class UI {
public:
    void openVerticalBox(const char*) {}
    void closeBox() {}
};
class Meta { public: void declare(const char*, const char*) {} };
class dsp { public: virtual ~dsp() = default; };

#include "GreetingDSP.h"

int main() {
    GreetingDSP dsp;
    dsp.init(48000);
    if (dsp.getNumInputs() != 0 || dsp.getNumOutputs() != 13)
        throw std::runtime_error("Unexpected DSP channel count");
    FAUSTFLOAT samples[13][1] = {};
    FAUSTFLOAT* outputs[13];
    for (int i = 0; i < 13; ++i) outputs[i] = samples[i];
    dsp.compute(1, nullptr, outputs);
    std::string message;
    for (int i = 0; i < 13; ++i) message += static_cast<char>(samples[i][0]);
    if (message != "Hello, World!") throw std::runtime_error(message);
    std::cout << message << '\n';
    std::cout << "PASS: genuine Faust generated DSP; 13 constant channels, one sample each\n";
}
