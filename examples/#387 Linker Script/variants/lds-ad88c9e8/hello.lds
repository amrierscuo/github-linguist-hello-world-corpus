SECTIONS
{
  .greeting :
  {
    __greeting_start = .;
    KEEP(*(.greeting))
    __greeting_end = .;
  }
}
INSERT AFTER .rodata;
