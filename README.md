# Jarvis — Voice Assistant

Jarvis is a Python-based voice assistant that listens for your voice, understands your commands, and takes action — opening websites, playing music, and more. Just say "Jarvis" to wake it up!

---

## Features

- Wake word detection — activates on hearing "Jarvis"
- Open websites — Google, YouTube, Facebook via voice command
- Play music — looks up songs from a custom music library and opens them in the browser
- Text-to-speech responses — speaks back to you using `pyttsx3`
- Real-time audio recording — captures microphone input using `sounddevice`

---

## Prerequisites

- Python 3.7+
- A working microphone
- Internet connection (for Google Speech Recognition)

---

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/jarvis.git
   cd jarvis
   ```

2. Install dependencies
   ```bash
   pip install speechrecognition pyttsx3 sounddevice numpy
   ```

3. Set up your music library

   Create a `musicLibrary.py` file in the project directory with your songs:
   ```python
   music = {
       "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
       "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
       # Add more songs here...
   }
   ```

---

## Usage

Run Jarvis with:

```bash
python jarvis.py
```

Jarvis will announce it's initializing, then start listening. Speak clearly into your microphone.

### Example Commands

| What you say | What Jarvis does |
|---|---|
| `"Jarvis"` | Wakes up and says *"Yaa"* |
| `"open google"` | Opens google.com in your browser |
| `"open youtube"` | Opens youtube.com in your browser |
| `"open facebook"` | Opens facebook.com in your browser |
| `"play believer"` | Looks up *believer* in the music library and opens the link |

---

## Project Structure

```
jarvis/
│
├── jarvis.py          # Main assistant script
└── musicLibrary.py    # Dictionary of song names mapped to URLs
```

---

## How It Works

1. On startup, Jarvis speaks *"Initialising Assistant...."* and enters a listening loop.
2. Every 2 seconds, it records audio from your microphone using `sounddevice`.
3. The audio is sent to **Google Speech Recognition** to convert speech to text.
4. If the recognized word is **"jarvis"**, it wakes up, acknowledges, and records a 5-second command.
5. The command is processed by `processCommand()`, which matches it to an action (open a site or play music).
6. Any errors (background noise, unrecognized speech) are caught and printed without crashing.

---

## Dependencies

| Library | Purpose |
|---|---|
| `speech_recognition` | Converts audio to text via Google Speech API |
| `pyttsx3` | Text-to-speech engine for voice responses |
| `sounddevice` | Records audio from the microphone |
| `numpy` | Handles audio data arrays |
| `webbrowser` | Opens URLs in the default browser |
| `musicLibrary` | Custom module storing song name → URL mappings |

---

## Limitations

- Requires an internet connection for speech recognition (uses Google's API)
- Wake word detection is not continuous — it checks every 2-second audio chunk
- Music library must be manually maintained in `musicLibrary.py`
- No support for offline speech recognition yet

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---
