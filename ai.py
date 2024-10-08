import requests
import json
from constants import ollamaModel, ollamaURL
from colorama import Fore

def generateText(messages):
    try:
        # print(messages)
        payload = json.dumps({
            "model": ollamaModel,
            "messages": messages,
            "stream": False
        })
        headers = {
            'Content-Type': 'application/json'
        }
        print(f"{Fore.GREEN}Starting request to ollama")
        response = requests.request("POST", ollamaURL, headers=headers, data=payload)
        return json.loads(response.text)['message']['content']
    except Exception as e:
        print(f"{Fore.RED} Error: {e}")
        return json.dumps({"message": {"content": "Ollama is down"}})
