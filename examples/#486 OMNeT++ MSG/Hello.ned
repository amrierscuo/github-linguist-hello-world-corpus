simple HelloWorld
{
    parameters:
        @display("i=block/app");
}
network GreetingNetwork
{
    submodules:
        greeting: HelloWorld;
}
