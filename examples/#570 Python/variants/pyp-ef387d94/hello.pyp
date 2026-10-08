import c4d
from c4d import plugins
class CorpusGreeting(plugins.CommandData):
    def Execute(self, doc):
        print("Hello, World!")
        return True
# Registrazione esclusa: occorre un Plugin ID assegnato realmente da Maxon.
