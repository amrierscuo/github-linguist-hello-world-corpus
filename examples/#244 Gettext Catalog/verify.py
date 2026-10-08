import gettext, sys
with open(sys.argv[1], 'rb') as stream:
    catalog = gettext.GNUTranslations(stream)
assert catalog.gettext('greeting') == 'Hello, World!'
assert catalog.gettext('unknown_key') == 'unknown_key'
print(catalog.gettext('greeting'))
print('Actual compiled GNU message catalog lookup PASS.')
