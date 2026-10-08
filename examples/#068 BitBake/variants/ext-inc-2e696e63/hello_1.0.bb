SUMMARY = "Corpus greeting"
LICENSE = "CLOSED"
require hello.inc
python do_build() {
    bb.plain(d.getVar("CORPUS_GREETING"))
}
addtask build
