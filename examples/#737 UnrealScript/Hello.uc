class Hello extends Actor;
event PostBeginPlay()
{
    Super.PostBeginPlay();
    `log("Hello, World!");
}
