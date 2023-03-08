import whisper
import json

class Speech2Text:
    def __init__(self, modelname="small") -> None:
        self.modelname = modelname
        self.model = whisper.load_model(self.modelname)
    
    def ToText(self, filename="./audio/recorded_audio.wav") -> str:
        result = self.model.transcribe(filename)
        return result
        
        