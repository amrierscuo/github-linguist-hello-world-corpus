"""Build hello.kv in a real Kivy window and capture its rendered pixels."""
from pathlib import Path
import hashlib
import json

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label

source = Path(__file__).with_name("hello.kv")
proof = source.parent / "verification" / "rendered.png"
Window.size = (640, 240)


class GreetingApp(App):
    def build(self):
        widget = Builder.load_file(str(source))
        assert isinstance(widget, Label)
        assert widget.text == "Hello, World!" and widget.font_size == 36
        return widget

    def on_start(self):
        Clock.schedule_once(self.capture, 1.0)

    def capture(self, _dt):
        self.root.texture_update()
        assert self.root.texture is not None and self.root.texture.size[0] > 0
        captured = Path(Window.screenshot(name=str(proof)))
        if captured != proof:
            captured.replace(proof)
        print(json.dumps({"kivy": kivy.__version__, "widget": type(self.root).__name__,
                          "text": self.root.text, "texture_size": self.root.texture.size,
                          "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                          "image": proof.name,
                          "image_sha256": hashlib.sha256(proof.read_bytes()).hexdigest()}))
        self.stop()


GreetingApp().run()
