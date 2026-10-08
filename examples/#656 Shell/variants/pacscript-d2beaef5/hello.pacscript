pkgname="corpus-greeting"
pkgver="1.0.0"
pkgrel="1"
arch=("any")
pkgdesc="Hello, World!"
url="https://example.invalid/corpus-greeting"
license=("MIT")
source=()
package() {
  install -d "${pkgdir}/usr/bin"
  printf '#!/bin/sh\nprintf "Hello, World!\\n"\n' > "${pkgdir}/usr/bin/corpus-greeting"
  chmod 755 "${pkgdir}/usr/bin/corpus-greeting"
}
