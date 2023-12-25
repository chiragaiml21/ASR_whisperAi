import whisper

model = whisper.load_model("medium")
result = model.transcribe("test.mp3")
print(result["text"])