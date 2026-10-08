# @ECLASS: hello-world.eclass
# @SUPPORTED_EAPIS: 8
# @BLURB: Install the original greeting fixture from FILESDIR.

case ${EAPI} in
    8) ;;
    *) die "hello-world.eclass requires EAPI 8" ;;
esac

hello-world_src_install() {
    newbin "${FILESDIR}/hello.sh" hello-world
}

EXPORT_FUNCTIONS src_install
