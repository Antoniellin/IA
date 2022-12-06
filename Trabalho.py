import whisper

#biblioteca python para ler metadados de música em vários formatos
from tinytag import TinyTag 

arquivo = open('arquivo.txt', 'w')
with open('t1.txt','r') as firstfile, open('arquivo.txt','a') as secondfile: 
      
    
    for line in firstfile: 
                     secondfile.write(line)

model = whisper.load_model("base")

# carregue o áudio e pad/apare-o para caber em 30 segundos
audio = whisper.load_audio("testeA.mp3")
audio = whisper.pad_or_trim(audio)

# faça o espectrograma log-Mel e mova para o mesmo dispositivo que o modelo
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detectar o idioma falado
_, probs = model.detect_language(mel)
print(f"Idioma: {max(probs, key=probs.get)}",file=arquivo)

# decodificar o áudio
options = whisper.DecodingOptions(fp16 = False)
result = whisper.decode(model, mel, options)

# imprimir o texto reconhecido
print( result.text, file=arquivo)
  
# imprimir o tamanho do audio
audio = TinyTag.get("testeA.mp3") 
print("Tamanho: " + str(audio.filesize) + " bytes",file=arquivo) 


arquivo.close()