#include <core.p4>
#include <v1model.p4>
header Greeting { bit<104> text; }
struct Headers { Greeting greeting; }
struct Metadata { }
parser Parser(packet_in packet, out Headers h, inout Metadata m, inout standard_metadata_t sm) {
    state start { transition accept; }
}
control Verify(inout Headers h, inout Metadata m) { apply { } }
control Ingress(inout Headers h, inout Metadata m, inout standard_metadata_t sm) {
    apply { h.greeting.setValid(); h.greeting.text = 104w0x48656c6c6f2c20576f726c6421; sm.egress_spec = 1; }
}
control Egress(inout Headers h, inout Metadata m, inout standard_metadata_t sm) { apply { } }
control Compute(inout Headers h, inout Metadata m) { apply { } }
control Deparser(packet_out packet, in Headers h) { apply { packet.emit(h.greeting); } }
V1Switch(Parser(), Verify(), Ingress(), Egress(), Compute(), Deparser()) main;
