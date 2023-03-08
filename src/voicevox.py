import requests

class Voicevox:
    def text2Speech(self, text: str, speaker: int="14"):
        url = f"http://localhost:50021/audio_query?text={text}&speaker={speaker}"
        headers = {"accept": "application/json"}

        r = requests.post(url, headers=headers)
        print(r.json())

        url = f"http://localhost:50021/synthesis?speaker={speaker}&enable_interrogative_upspeak=true"
        headers = {
            "accept": "audio/wav",
            "Content-Type": "application/json"
        }
        payload = r.json()
        r = requests.post(url, json=payload, headers=headers)

        with open("./audio/output.wav", "wb") as f:
            f.write(r.content)
