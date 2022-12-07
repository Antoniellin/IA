import whisper

#biblioteca python para ler metadados de música em vários formatos
from tinytag import TinyTag 

model = whisper.load_model("medium")
result = model.transcribe("Tubarão Te Amo - DJ LK.mp3")

# carregue o áudio e pad/apare-o para caber em 30 segundos
audio = whisper.load_audio("Tubarão Te Amo - DJ LK.mp3")
audio = whisper.pad_or_trim(audio)

# faça o espectrograma log-Mel e mova para o mesmo dispositivo que o modelo
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# imprimir o texto reconhecido

print(result["text"])
  
# imprimir o tamanho do audio
audio = TinyTag.get("Tubarão Te Amo - DJ LK.mp3") 
print("Tamanho: " + str(audio.filesize) + " bytes") 

# detectar o idioma falado
_, probs = model.detect_language(mel)
print(f"Idioma: {max(probs, key=probs.get)}")

