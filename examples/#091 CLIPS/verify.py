from pathlib import Path
import clips

class Capture(clips.Router):
    def __init__(self):
        super().__init__('corpus-capture', 100)
        self.output = ''
    def query(self, name):
        return name == 'stdout'
    def write(self, name, text):
        self.output += text

env = clips.Environment()
capture = Capture()
env.add_router(capture)
env.load(str(Path('hello.clp').resolve()))
env.reset()
fired = env.run()
assert fired == 1, fired
assert capture.output == 'Hello, World!\n', repr(capture.output)
print(capture.output, end='')
print(f'clipspy {clips.__version__}: one native CLIPS rule fired; output assertion PASS.')
