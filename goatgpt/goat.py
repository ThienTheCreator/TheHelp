import openai
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("API_KEY")

class Goat:
    def __init__(self):
        pass
        # self.storage = {"default": []}
        # self.current_basket = "default"

    def ask(self, prompt):
        response = openai.Completion.create(
            engine="babbage",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text
        # self.storage[self.current_basket].append(item)
        if len(message) > 2000:
            message = message[:1997] + "..."
        print("message:")
        print(message)
        return message
    

 
    # def history(self):
    #     return random.choice(choices)