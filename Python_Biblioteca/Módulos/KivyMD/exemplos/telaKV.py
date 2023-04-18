import speech_recognition as sr
import pyttsx3

# inicialize a biblioteca de reconhecimento de fala
r = sr.Recognizer()

# inicialize a biblioteca de síntese de fala
engine = pyttsx3.init()

# defina as configurações da voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # altere o índice para mudar a voz

# peça ao usuário para digitar algo
print("Digite algo: eia maluco muito doido")

# ouça o áudio do microfone
with sr.Microphone() as source:
    audio = r.listen(source)

    # use a biblioteca de reconhecimento de fala para transcrever o áudio em texto
    text = r.recognize_google(audio)

    # use a biblioteca de síntese de fala para falar o texto em voz alta
    engine.say(text)
    engine.runAndWait()
