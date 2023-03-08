![Kawaiibanner2](https://user-images.githubusercontent.com/58620209/223855069-767a7f95-33ba-4617-820c-061e2dec1007.png)

# Kawaii-Voice
Kawaii-Voice converts inputed voice to Anime voice using Voicevox.
```
+------------+      +---------+      +----------+      +--------+
| Microphone | ---> | Whisper | ---> | Voicevox | ---> | Output |
+------------+      +---------+      +----------+      +--------+
```

# Environment
- Windows 10
- Python 3.8.0
The above has been confirmed to work.

1. Build environment to use Whisper
[Reference](https://github.com/openai/whisper "Reference")
Small size of model is default.

2. Launch Voicevox On docker
[Reference](https://github.com/VOICEVOX/voicevox_engine#docker-%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8 "Reference")

```d
docker pull voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
```

3.Extra（If you want to use this in game or Discord）
- [Voicemeeter Banana](https://vb-audio.com/Voicemeeter/banana.htm "Voicemeeter Banana")

# Usage
- Record only while a specific key is being pressed.

## Run
```
python main.py
```

## main.py
- Change 's' to key what you want.
- Change 'medium' to your preferred model.

```python
KEYLISTENER = KeyListener("s")
SPEECH2TEXT = Speech2Text("medium")
```

- You can change speaking character by changing character_Id.
- The default is Meimei Himari.

```python
VOICEVOX.text2Speech(result, character_Id)
```

## voicevox.py
- If you change endpoint or ports, you need to change the below code.

```python
url = f"http://localhost:50021/audio_query?text={text}&speaker={speaker}"
url = f"http://localhost:50021/synthesis?speaker={speaker}&enable_interrogative_upspeak=true"
```


## ./src/audio/
- This is where recording file and a file which is outputted by Voicevox is saved.


# List of Characters

```json
[
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "Shikoku Metan",
    "speaker_uuid": "7ffcb7ce-00ec-4bdc-82cd-45a8889e43ff",
    "styles": [
      {
        "name": "Normal",
        "id": 2
      },
      {
        "name": "Sweet",
        "id": 0
      },
      {
        "name": "Tsundere",
        "id": 6
      },
      {
        "name": "Sexy",
        "id": 4
      },
      {
        "name": "Whisper",
        "id": 36
      },
      {
        "name": "Hush-hush",
        "id": 37
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "Zunda Mon",
    "speaker_uuid": "388f246b-8c41-4ac1-8e2d-5d79f3ff56d9",
    "styles": [
      {
        "name": "Normal",
        "id": 3
      },
      {
        "name": "Sweet",
        "id": 1
      },
      {
        "name": "Tsundere",
        "id": 7
      },
      {
        "name": "Sexy",
        "id": 5
      },
      {
        "name": "Whisper",
        "id": 22
      },
      {
        "name": "Hush-hush",
        "id": 38
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Kasukabe Tsumugi",
    "speaker_uuid": "35b2c544-660e-401e-b503-0e14c635303a",
    "styles": [
      {
        "name": "Normal",
        "id": 8
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Ame Hareshi",
    "speaker_uuid": "3474ee95-c274-47f9-aa1a-8322163d96f1",
    "styles": [
      {
        "name": "Normal",
        "id": 10
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Namioto Ritsu",
    "speaker_uuid": "b1a81618-b27b-40d2-b0ea-27a9ad408c4b",
    "styles": [
      {
        "name": "Normal",
        "id": 9
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Genno Takehiro",
    "speaker_uuid": "c30dc15a-0992-4f8d-8bb8-ad3b314e6a6f",
    "styles": [
      {
        "name": "Normal",
        "id": 11
      },
      {
        "name": "Joy",
        "id": 39
      },
      {
        "name": "Tsundere",
        "id": 40
      },
      {
        "name": "Sadness",
        "id": 41
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Shiraki Korotaro",
    "speaker_uuid": "e5020595-5c5d-4e87-b849-270a518d0dcf",
    "styles": [
      {
        "name": "Normal",
        "id": 12
      },
      {
        "name": "Yay",
        "id": 32
      },
      {
        "name": "Frightened",
        "id": 33
      },
      {
        "name": "Angry",
        "id": 34
      },
      {
        "name": "Crying",
        "id": 35
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Aoyama Ryusei",
    "speaker_uuid": "4f51116a-d9ee-4516-925d-21f183e2afad",
    "styles": [
      {
        "name": "Normal",
        "id": 13
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "MeiMing Himari",
    "speaker_uuid": "8eaad775-3119-417e-8cf4-2a10bfd592c8",
    "styles": [
      {
        "name": "Normal",
        "id": 14
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "Kyushu Sora",
    "speaker_uuid": "481fb609-6446-4870-9f46-90c4dd623403",
    "styles": [
      {
        "name": "Normal",
        "id": 16
      },
      {
        "name": "Amama",
        "id": 15
      },
      {
        "name": "Tsuntsun",
        "id": 18
      },
      {
        "name": "Sexy",
        "id": 17
      },
      {
        "name": "Sasayaki",
        "id": 19
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "Mochiko-san",
    "speaker_uuid": "9f3ee141-26ad-437e-97bd-d22298d02ad2",
    "styles": [
      {
        "name": "Normal",
        "id": 20
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Kenzaki Cio",
    "speaker_uuid": "1a17ca16-7ee5-4ea5-b191-2f02ace24d21",
    "styles": [
      {
        "name": "Normal",
        "id": 21
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "WhiteCUL",
    "speaker_uuid": "67d5d8da-acd7-4207-bb10-b5542d3a663b",
    "styles": [
      {
        "name": "Normal",
        "id": 23
      },
      {
        "name": "Tanoshii",
        "id": 24
      },
      {
        "name": "Kanashii",
        "id": 25
      },
      {
        "name": "Bieen",
        "id": 26
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Kouki",
    "speaker_uuid": "0f56c2f2-644c-49c9-8989-94e11f7129d0",
    "styles": [
      {
        "name": "Human ver.",
        "id": 27
      },
      {
        "name": "Stuffed animal ver.",
        "id": 28
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "No.7",
    "speaker_uuid": "044830d2-f23b-44d6-ac0d-b5d733caa900",
    "styles": [
      {
        "name": "Normal",
        "id": 29
      },
      {
        "name": "Announcement",
        "id": 30
      },
      {
        "name": "Reading aloud",
        "id": 31
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Chibi-shiki Ji",
    "speaker_uuid": "468b8e94-9da4-4f7a-8715-a22a48844f9e",
    "styles": [
      {
        "name": "Normal",
        "id": 42
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Sakurauta Miko",
    "speaker_uuid": "0693554c-338e-4790-8982-b9c6d476dc69",
    "styles": [
      {
        "name": "Normal",
        "id": 43
      },
      {
        "name": "Second form",
        "id": 44
      },
      {
        "name": "Loli",
        "id": 45
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Sayo",
    "speaker_uuid": "a8cc6d22-aad0-4ab8-bf1e-2f843924164a",
    "styles": [
      {
        "name": "Normal",
        "id": 46
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Nurse Robo Type T",
    "speaker_uuid": "882a636f-3bac-431a-966d-c5e6bba9f949",
    "styles": [
      {
        "name": "Normal",
        "id": 47
      },
      {
        "name": "Easy",
        "id": 48
      },
      {
        "name": "Horror",
        "id": 49
      },
      {
        "name": "Secret talk",
        "id": 50
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "†Holy Knight Kurenai Sakura†",
    "speaker_uuid": "471e39d2-fb11-4c8c-8d89-4b322d2498e0",
    "styles": [
      {
        "name": "Normal",
        "id": 51
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Jumatsu Shuji",
    "speaker_uuid": "0acebdee-a4a5-4e12-a695-e19609728e30",
    "styles": [
      {
        "name": "Normal",
        "id": 52
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "Kirigashima Muneshige",
    "speaker_uuid": "7d1e7ba7-f957-40e5-a3fc-da49f769ab65",
    "styles": [
      {
        "name": "Normal",
        "id": 53
      }
    ],
    "version": "0.14.2"
  }
]
```
