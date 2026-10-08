#include "EXTERN.h"
#include "perl.h"
#include "XSUB.h"

MODULE = Corpus::Greeting PACKAGE = Corpus::Greeting
PROTOTYPES: DISABLE

SV *
greeting()
  CODE:
    RETVAL = newSVpv("Hello, World!", 0);
  OUTPUT:
    RETVAL
