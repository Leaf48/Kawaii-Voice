"""
This is a listener of key detection.
"""

from pynput import keyboard

class KeyListener:
    def __init__(self, target) -> None:
        self.targetKey = target
        self.targetKey_state = False

        self.registerListener(self.on_press, self.on_release)

    def registerListener(self, press, release):
        listener = keyboard.Listener(on_press=press, on_release=release)
        listener.start()

    def on_press(self, key):
        try:
            if key.char == self.targetKey:
                self.targetKey_state = True

        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key.char == self.targetKey:
                self.targetKey_state = False

        except AttributeError:
            pass