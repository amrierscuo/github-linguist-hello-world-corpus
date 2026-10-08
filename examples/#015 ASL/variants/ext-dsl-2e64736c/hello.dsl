DefinitionBlock ("", "SSDT", 2, "HWCRPS", "HELLO", 0x00000001)
{
    Method (HWLD, 0, NotSerialized)
    {
        Store ("Hello World", Debug)
        Return ("Hello World")
    }
}
