import ctypes as c
import json
import os
from pathlib import Path
import sys

def bind(lib, name, result, args):
    f = getattr(lib, name)
    f.restype = result
    f.argtypes = args
    return f

def text(value):
    if not value:
        raise ValueError('GIO returned NULL')
    return value.decode('utf8')

gio = c.CDLL('libgio-2.0.so.0')
glib = c.CDLL('libglib-2.0.so.0')
gobj = c.CDLL('libgobject-2.0.so.0')
p, s = c.c_void_p, c.c_char_p
new = bind(gio, 'g_desktop_app_info_new_from_filename', p, [s])
name = bind(gio, 'g_app_info_get_name', s, [p])
executable = bind(gio, 'g_app_info_get_executable', s, [p])
get_string = bind(gio, 'g_desktop_app_info_get_string', p, [p,s])
get_bool = bind(gio, 'g_desktop_app_info_get_boolean', c.c_int, [p,s])
free = bind(glib, 'g_free', None, [p])
unref = bind(gobj, 'g_object_unref', None, [p])

app = new(os.fsencode(str(Path(sys.argv[1]).resolve())))
if not app:
    raise SystemExit('GDesktopAppInfo rejected input')
try:
    exec_ptr = get_string(app,b'Exec')
    try:
        properties = {'Name':text(name(app)),
                      'Exec':text(c.string_at(exec_ptr)) if exec_ptr else None,
                      'Executable':text(executable(app)),
                      'Terminal':bool(get_bool(app,b'Terminal'))}
    finally:
        free(exec_ptr)
finally:
    unref(app)
expected = {'Name':'Hello, World!','Exec':'printf "Hello, World!"','Executable':'printf','Terminal':True}
print(json.dumps({'glib_version':'.'.join(str(c.c_uint.in_dll(glib,'glib_'+p+'_version').value) for p in ('major','minor','micro')),'properties':properties,'application_launched':False}))
if properties != expected:
    raise SystemExit('Desktop launcher metadata differs from expected values')
