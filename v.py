import whisper

model = whisper.load_model("base")

result = model.transcribe(r"C:\Users\acer\Desktop\video23.mp4")

text = result["text"]

print(text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Done!")
