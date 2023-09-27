import speech_recognition as sr
from dotenv import load_dotenv
import os
import openai
import pyttsx3


class Assistant:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_user_input(self):
        rec = sr.Recognizer()
        with sr.Microphone() as microfone:
            rec.adjust_for_ambient_noise(microfone)
            print('Comece a falar: ')
            audio = rec.listen(microfone)
            return rec.recognize_google(audio, language='pt-BR')

    def get_assistant_reply(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": user_input},
            ]
        )
        return response['choices'][0]['message']['content']

    def run(self):
        while True:
            if self.get_user_input == "sair":
                break

            user_input = self.get_user_input()
            
            response = self.get_assistant_reply(user_input)
            print(response)
            
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)  
            engine.say(response)
            engine.runAndWait()
            

if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()
