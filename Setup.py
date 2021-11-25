import os, colorama
from colorama import init

init()

os.system("pip install colorama")
os.system("cls")

SUCCESS = "[\x1b[32m+\x1b[39m]"
ERROR = "[\x1b[31m-\x1b[39m]"
print('{} This Will Setup What Is Needed To Run The Claimer!\n'.format(SUCCESS))
print('{}'.format(SUCCESS), end='');Setup = input(' Press Enter To Start Setup... ')

os.system("pip install requests")
os.system("pip install discord_webhook")
os.system("pip install colorama")