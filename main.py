from ai import generateText
import traceback
from constants import systemMessageGeneric, listOfProductTypes, listOfProductTypeQuestions, addingProductMessage
from products import products
import json
from colorama import Fore
from colorama import init as colorama_init


colorama_init(autoreset=True)
try:
    systemMessage = systemMessageGeneric
    systemMessage["content"] = systemMessage["content"].replace("{ProductTypes}", json.dumps(listOfProductTypes))
    systemMessage["content"] = systemMessage["content"].replace("{ProductTypeQuestions}", json.dumps(listOfProductTypeQuestions))

    history = [systemMessage, {"role": "user", "content": "Can you help me find a product?"}]
    text = generateText(history)
    history.append({"role": "assistant", "content": text})
    print(f"{Fore.GREEN} Chatbot: {text}")
    while True:
        inputType = input("USER: ")
        history.append({"role": "user", "content": inputType})
        response = generateText(history)
        history.append({"role": "assistant", "content": response})
        print(f"{Fore.CYAN}Ollama: {response}")
        lowerResponse = response.lower()
        # TODO make this better
        if "**found product: " in lowerResponse and ("computer" or "printer" in lowerResponse):
            addingProductMessageCopy = addingProductMessage.copy()
            if "computer" in lowerResponse:
                addingProductMessageCopy["content"] = addingProductMessageCopy["content"].replace("{Products}", json.dumps(products["Computers"]))
            elif "printer" in lowerResponse:
                addingProductMessageCopy["content"] = addingProductMessageCopy["content"].replace("{Products}", json.dumps(products["Printers"]))
            history.append(addingProductMessageCopy)
        if "END TEXT" in response:
            break
except Exception as e:
    print(f"{Fore.RED} Error: {e}")
    print(traceback.format_exc())