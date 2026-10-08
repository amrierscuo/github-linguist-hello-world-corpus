circuit Hello :
  module Hello :
    input clock : Clock
    input reset : UInt<1>
    output greeting : UInt<8>[13]
    greeting[0] <= UInt<8>(72)
    greeting[1] <= UInt<8>(101)
    greeting[2] <= UInt<8>(108)
    greeting[3] <= UInt<8>(108)
    greeting[4] <= UInt<8>(111)
    greeting[5] <= UInt<8>(44)
    greeting[6] <= UInt<8>(32)
    greeting[7] <= UInt<8>(87)
    greeting[8] <= UInt<8>(111)
    greeting[9] <= UInt<8>(114)
    greeting[10] <= UInt<8>(108)
    greeting[11] <= UInt<8>(100)
    greeting[12] <= UInt<8>(33)
    printf(clock, not(reset), "Hello, World!\n")
