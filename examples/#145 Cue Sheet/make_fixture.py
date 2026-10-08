from pathlib import Path
import wave
# Original one-second PCM fixture; generated only when testing in a temporary copy.
with wave.open(str(Path(__file__).with_name("silence.wav")), "wb") as audio:
    audio.setnchannels(2)
    audio.setsampwidth(2)
    audio.setframerate(44100)
    audio.writeframes(bytes(44100 * 2 * 2))
