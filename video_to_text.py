import whisper

model = whisper.load_model("base")

result = model.transcribe("Enter video file path: ")

text = result["text"]

print(text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Done!")
