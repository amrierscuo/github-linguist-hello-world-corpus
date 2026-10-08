configuration HelloAppC {}
implementation {
  components MainC, HelloC, PrintfC, SerialStartC;
  HelloC.Boot -> MainC.Boot;
}
