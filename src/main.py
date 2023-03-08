import pyaudio
import wave
# import keyboard
from pynput import keyboard
from voice import Speech2Text

targetKey = 's'
targetKey_state = False

def on_press(key):
    global targetKey_state
    try:
        if key.char == targetKey:
            targetKey_state = True
        # print("Key {0} Pressed!".format(key.char))

    except AttributeError:
        # print("Special Key {0} Pressed!".format(key))
        pass

def on_release(key):
    global targetKey_state
    try:
        if key.char == targetKey:
            targetKey_state = False
        # print("Key {0} Released!".format(key.char))

    except AttributeError:
        # print("Special Key {0} Released!".format(key))
        pass
    
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
        
class Recorder:
    def __init__(self) -> None:
        # Set parameters for recording
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

        # Create PyAudio object
        self.p = pyaudio.PyAudio()

        # Create array to save
        self.frames = []

        # Create stream for recording
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        
    def stopRecording(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def saveAsWav(self, filename="./audio/recorded_audio.wav"):
        # save recorded audio as .wav file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        print("Audio saved as recorded_audio.wav.")
        

if __name__ == "__main__":
    print("Press 's' to start recording...")
    s = Speech2Text()

    while True:
        print("Running")
        r = Recorder()
        while True:
            if targetKey_state:
                print("Recording...")
                break
        
        while targetKey_state:
            data = r.stream.read(r.CHUNK)
            r.frames.append(data)
        else:
            print("Recording stopped.")
            r.stopRecording()
            r.saveAsWav()

        result = s.ToText()
        print(result)
