---- MODULE Hello ----
EXTENDS TLC
VARIABLE message
Init == /\ message = "Hello, World!"
        /\ PrintT(message)
Next == UNCHANGED message
Spec == Init /\ [][Next]_message
GreetingIsExact == message = "Hello, World!"
====
