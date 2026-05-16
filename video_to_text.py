import whisper

print("Loading Whisper model...")
model = whisper.load_model("base")

# Ask user for video path
video_path = input("Enter video file path: ")

print("Transcribing video...")
result = model.transcribe(video_path)

text = result["text"]

print("\nTranscribed Text:\n")
print(text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\nDone! Text saved to output.txt")
