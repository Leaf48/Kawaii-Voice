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
            # print("Key {0} Pressed!".format(key.char))

        except AttributeError:
            # print("Special Key {0} Pressed!".format(key))
            pass

    def on_release(self, key):
        try:
            if key.char == self.targetKey:
                self.targetKey_state = False
            # print("Key {0} Released!".format(key.char))

        except AttributeError:
            # print("Special Key {0} Released!".format(key))
            pass