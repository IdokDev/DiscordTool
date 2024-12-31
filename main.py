from colorama import Fore,Style,init
from time import sleep
import os
import requests
import random
import string

init(autoreset=True)
def logo():
    logo = """
     _______   __                                                __       ________  ______    ______   __       
    /       \ /  |                                              /  |     /        |/      \  /      \ /  |      
    $$$$$$$  |$$/   _______   _______   ______    ______    ____$$ |     $$$$$$$$//$$$$$$  |/$$$$$$  |$$ |      
    $$ |  $$ |/  | /       | /       | /      \  /      \  /    $$ | ______ $$ |  $$ |  $$ |$$ |  $$ |$$ |      
    $$ |  $$ |$$ |/$$$$$$$/ /$$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$$ |/      |$$ |  $$ |  $$ |$$ |  $$ |$$ |      
    $$ |  $$ |$$ |$$      \ $$ |      $$ |  $$ |$$ |  $$/ $$ |  $$ |$$$$$$/ $$ |  $$ |  $$ |$$ |  $$ |$$ |      
    $$ |__$$ |$$ | $$$$$$  |$$ \_____ $$ \__$$ |$$ |      $$ \__$$ |        $$ |  $$ \__$$ |$$ \__$$ |$$ |_____ 
    $$    $$/ $$ |/     $$/ $$       |$$    $$/ $$ |      $$    $$ |        $$ |  $$    $$/ $$    $$/ $$       |
    $$$$$$$/  $$/ $$$$$$$/   $$$$$$$/  $$$$$$/  $$/        $$$$$$$/         $$/    $$$$$$/   $$$$$$/  $$$$$$$$/ 
                                                                                                                                                                                                                                                                                                           
               
                            code by @idok                                          
"""
    
    lines = logo.splitlines()
    for i, line in enumerate(lines):
        color = Fore.RED if i % 2 == 0 else Fore.LIGHTBLACK_EX
        print(f"{color}{line}")

logo()

print("\nWhat do you want to do? ")
print("1. Webhook Spammer")
print("2. Webhook Message Sender")
print("3. Nitro Code Generator")
print("4. EXIT")

choose = int(input("Choose: "))

def spam():
    webhook = input("Enter the webhook: ")
    message = input("Enter the message: ")
    while True:
        data = {
            "content": message
        }
        response = requests.post(webhook, json=data)
        if response.status_code == 204:
            print(Fore.GREEN + "Message sent successfully!")
        else:
            print(Fore.RED + f"Failed to send message. Status code: {response.status_code}")

def nitro():
    webhook = input("Enter the webhook: ")
    while True:
        code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
        data = {
            "content": f"https://discord.gift/{code}"
        }
        response = requests.post(webhook, json=data)
        sleep(0.5)
        if response.status_code == 204:
            print(Fore.GREEN + f"Code sent successfully! Code: {code}")
        else:
            print(Fore.RED + f"Failed to send code. Status code: {response.status_code}")

if choose == 1:
    os.system("cls")
    logo()
    spam()

elif choose == 2:
    os.system("cls")
    logo()
    webhook = input("Enter the webhook: ")
    message = input("Enter the message: ")
    data = {
        "content": message
    }
    response = requests.post(webhook, json=data)
    if response.status_code == 204:
        os.system("cls")
        logo()
        print(Fore.GREEN + "\nMessage sent successfully!")
    else:
        os.system("cls")
        logo()
        print(Fore.RED + f"\nFailed to send message. Status code: {response.status_code}")


elif choose == 3:
    os.system("cls")
    logo()
    nitro()

elif choose == 4:
    for i in range(5):
        os.system("cls")
        logo()
        print(Fore.RED + "\nExiting... in " + str(5-i))
        sleep(1)
    