from ai import generateText
import traceback
from constants import systemMessageComputer
from products import products
import json
from colorama import Fore
from colorama import init as colorama_init


colorama_init(autoreset=True)
try:
    computer_type = None
    while True:
        inputType = input("what type of a computer do you want (laptop, desktop): ")
        if inputType == "laptop" or inputType == "desktop":
            computer_type = inputType
            break
        else:
            print(f"{Fore.RED}Invalid input")
    systemMessage = systemMessageComputer
    if computer_type == "laptop":
        systemMessage["content"] = systemMessage["content"].replace("{Products}", json.dumps(products["Computers"]["Laptops"]))
    else:
        systemMessage["content"] = systemMessage["content"].replace("{Products}", json.dumps(products["Computers"]["Desktops"]))
    
    # print (systemMessage["message"])
    history = [systemMessage, {"role": "user", "content": "Can you help me find a computer?"}]
    text = generateText(history)
    history.append({"role": "assistant", "content": text})
    print(f"{Fore.GREEN} Chatbot: {text}")
    while True:
        inputType = input("USER: ")
        history.append({"role": "user", "content": inputType})
        response = generateText(history)
        history.append({"role": "assistant", "content": response})
        print(f"{Fore.CYAN}Ollama: {response}")
        if "END TEXT" in response:
            break
except Exception as e:
    print(f"{Fore.RED} Error: {e}")
    print(traceback.format_exc())