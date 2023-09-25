import openai
from key import apikey

class Chatbot:
    def __init__(self):
        openai.api_key = apikey

    def getresponse(self, userinput):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt = userinput,
            max_tokens = 4000,
            temperature = 0.4
        ).choices[0].text
        return response
    