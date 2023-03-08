from voice import Speech2Text
from keyListener import KeyListener
from recorder import Recorder

# Create Instances
KEYLISTENER = KeyListener("s")
SPEECH2TEXT = Speech2Text()

if __name__ == "__main__":
    print("Press {0} to start recording...".format(KEYLISTENER.targetKey))

    while True:
        r = Recorder()
        while True:
            if KEYLISTENER.targetKey_state:
                print("Recording...")
                break
        
        while KEYLISTENER.targetKey_state:
            data = r.stream.read(r.CHUNK)
            r.frames.append(data)
        else:
            print("Recording stopped.")
            r.stopRecording()
            r.saveAsWav()

        result = SPEECH2TEXT.ToText()
        print(result)
