# Install these libraries first (only once):
# pip install googletrans==4.0.0-rc1 pyttsx3

from googletrans import Translator
import pyttsx3

def speak(text, lang="en"):
    engine = pyttsx3.init()

    # Change voice based on language if available
    voices = engine.getProperty("voices")
    for voice in voices:
        if lang in voice.id:   # match language code (like 'fr', 'es')
            engine.setProperty("voice", voice.id)
            break

    engine.say(text)
    engine.runAndWait()

# Create translator object
translator = Translator()

# Take input from user
english_txt = input("Enter text in English: ")

# Ask for target language
lang_choice = input("Enter target language code (e.g., fr=French, es=Spanish, de=German): ")

# Translate English → Target language
translated = translator.translate(english_txt, src='en', dest=lang_choice)

print(f"Translated ({lang_choice}):", translated.text)

# Speak the translated text in chosen language
speak(translated.text, lang_choice)


