# def pri(x):
#     print("Petar")
#     return x

# @pri
# def pri2(x):
#     print(x)

# pri2("ppP")

# vl = [("niska Banja", [1, 2, 3]), ("tele", [2, 3, 5])]

# print(vl[1][1])

# import sounddevice as sd
# import soundfile as sf

# # Set the duration of the recording in seconds
# duration = 5

# # Record the audio using a default device
# recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2)
# print("Recording audio...")

# # Wait until recording is finished
# sd.wait()

# # Save the recorded audio to a file
# sf.write("recording.wav", recording, 44100)

# # Load the recorded audio from the file
# data, fs = sf.read("recording.wav")

# # Play the recorded audio
# print("Playing back recorded audio...")
# sd.play(data, fs)

# # Wait until playback is finished
# sd.wait()

# import speech_recognition as sr

# # Set the audio file to transcribe
# audio_file = "recording.wav"

# # Create a Recognizer instance
# r = sr.Recognizer()

# # Open the audio file
# with sr.AudioFile(audio_file) as source:
#     # Read the audio file
#     audio = r.record(source)

# # Transcribe the audio to text
# text = r.recognize_google(audio)

# # Print the transcribed text
# print(text)

# import speech_recognition as sr
# import pyautogui

# # Set the audio file to transcribe
# audio_file = "recording.wav"

# # Create a Recognizer instance
# r = sr.Recognizer()

# # Open the audio file
# with sr.AudioFile(audio_file) as source:
#     # Read the audio file
#     audio = r.record(source)

# # Transcribe the audio to text
# text = r.recognize_google(audio)

# # Type the transcribed text on the keyboard
# pyautogui.typewrite(text)

import speech_recognition as sr

# Create a Recognizer instance
r = sr.Recognizer()

# Listen for audio input
with sr.Microphone() as source:
    print("Listening for audio...")
    audio = r.listen(source)

# Transcribe the audio to text
text = r.recognize_google(audio)

# Print the transcribed text
print(text)

