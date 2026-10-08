#include <omnetpp.h>
#include "Greeting_m.h"
using namespace omnetpp;
class HelloWorld : public cSimpleModule {
 protected:
  void initialize() override { GreetingMessage message("greeting"); EV_INFO << message.getGreeting() << "\n"; }
};
Define_Module(HelloWorld);
