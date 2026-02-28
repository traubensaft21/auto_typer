import pyautogui as auto
import time
import os
from colorama import Fore, init

os.system("cls")
mainc = "\u001b[35;1m"
white = Fore.RESET
banner = f"""
{mainc}
        ░█████╗░██╗░░░██╗████████╗░█████╗░ ████████╗██╗░░░██╗██████╗░███████╗██████╗░
        ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗ ╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗
        ███████║██║░░░██║░░░██║░░░██║░░██║ ░░░██║░░░░╚████╔╝░██████╔╝█████╗░░██████╔╝
        ██╔══██║██║░░░██║░░░██║░░░██║░░██║ ░░░██║░░░░░╚██╔╝░░██╔═══╝░██╔══╝░░██╔══██╗
        ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝ ░░░██║░░░░░░██║░░░██║░░░░░███████╗██║░░██║
        ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░ ░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝{white}

                                    Mady by Crazex0303

"""

print(banner)

Name = input("What to Type: ")
customcount = input("How many times to repeat: ")

os.system("cls")
count = int(customcount)
print("Starting in:")
countdown = 5
while(countdown != 0):
    print(countdown)
    time.sleep(1)
    countdown -= 1

for x in range(count):
    print("Typing...")
    auto.write(Name)
    auto.press("enter")
    number = 0
for char in customcount:
    if char == 1:
        count = count + 1
    
os.system("cls")
print("Auto typer succesfully send:",(Name))
print("Typed", (customcount), "times")
time.sleep(1500)