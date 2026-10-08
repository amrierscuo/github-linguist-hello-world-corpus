SUMMARY = "Corpus greeting task"
LICENSE = "CLOSED"

python do_build() {
    bb.plain("Hello, World!")
}
addtask build
