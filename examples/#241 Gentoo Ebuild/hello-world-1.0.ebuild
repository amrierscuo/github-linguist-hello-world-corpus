EAPI=8

DESCRIPTION="Original Hello, World! console example"
HOMEPAGE="https://example.invalid/hello-world"
LICENSE="0BSD"
SLOT="0"
KEYWORDS="~amd64"
S="${WORKDIR}"

src_install() {
    newbin "${FILESDIR}/hello.sh" hello-world
}
