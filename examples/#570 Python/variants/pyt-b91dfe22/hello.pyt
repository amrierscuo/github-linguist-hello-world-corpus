class Toolbox:
    def __init__(self):
        self.label = "Corpus Greeting"
        self.alias = "corpusgreeting"
        self.tools = [Greeting]
class Greeting:
    def __init__(self):
        self.label = "Greeting"
        self.description = "Print an original greeting"
    def getParameterInfo(self):
        return []
    def execute(self, parameters, messages):
        messages.addMessage("Hello, World!")
