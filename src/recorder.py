import pyaudio
import wave

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
        
    def stopRecording(self) -> None:
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def saveAsWav(self, filename="./audio/recorded_audio.wav") -> None:
        # save recorded audio as .wav file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        print("Audio saved as recorded_audio.wav.")