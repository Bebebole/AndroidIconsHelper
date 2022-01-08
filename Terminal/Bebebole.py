import os
import sys
from pathlib import Path
import requests
import configparser
import shutil
x = [f.name for f in os.scandir() if f.is_file()]

os.chdir("C:\Program Files")

try:
    os.mkdir("Bebebole")
except FileExistsError:
    pass

os.chdir("C:\Program Files\Bebebole")

try:
    os.mkdir("IconPackMaker")
except FileExistsError:
    pass

os.chdir("C:\Program Files\Bebebole\IconPackMaker")

try :
    open("pathsettings.ini","x")
    file = open("pathsettings.ini","w")
    response = requests.get('https://raw.githubusercontent.com/Bebebole/BebeboleIconsPython/main/pathsettings.ini')
    file.write(response.text)
    file.close()
    print("Tu dois mettre à jour le fichier pour que le programme marche correctement !\nIl faut modifier le fichier 'pathsettings.ini'(C:\Program Files\Bebebole\IconPackMaker)")
    input()

except FileExistsError:
    pass

config = configparser.ConfigParser()
config.read("pathsettings.ini")
icon_temp = config.get("path", "icon_temp")
icon_backup = config.get("path", "icon_backup")
icon_all = config.get("path", "icon_all")

print("\n \033[1;32;40m██████╗░███████╗██████╗░███████╗██████╗░░█████╗░██╗░░░░░███████╗\n ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔════╝\n ██████╦╝█████╗░░██████╦╝█████╗░░██████╦╝██║░░██║██║░░░░░█████╗░░\n ██╔══██╗██╔══╝░░██╔══██╗██╔══╝░░██╔══██╗██║░░██║██║░░░░░██╔══╝░░\n ██████╦╝███████╗██████╦╝███████╗██████╦╝╚█████╔╝███████╗███████╗\n ╚═════╝░╚══════╝╚═════╝░╚══════╝╚═════╝░░╚════╝░╚══════╝╚══════╝\n")
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
question2 = input("\n\n\033[34;1;40mSalut Bilel ! \033[37;1;40mTu veux faire quoi ?\n\n[a] Remplir le fichier \033[31;1;40mappfilter\n\033[37;1;40m[b] Remplir le fichier \033[31;1;40mdrawable\n\033[37;1;40m[c] Remplir le fichier \033[31;1;40micon_pack\n\033[37;1;40m[d] Trier les icônes\n\n\033[33;1;40mAlors ? : ")


#Appfilter
if question2 == "a":
    os.chdir(icon_temp)
    clearConsole()
    with os.scandir() as i:
        for entry in i:
            if entry.is_file():
                print('\033[33;1;40m<item\n    \033[32;1;40mcomponent="ComponentInfo{}"\n    drawable="', end = "")
                sys.stdout.write(Path(entry.name).resolve().stem)
                sys.stdout.write('" \033[33;1;40m/>\n\n')

#Drawable
if question2 == "b":
    os.chdir(icon_temp)
    clearConsole()
    with os.scandir() as i:
        for entry in i:
            if entry.is_file():
                print('\033[33;1;40m<item \033[32;1;40mdrawable="' , end = "")
                sys.stdout.write(Path(entry.name).resolve().stem)
                sys.stdout.write('"\033[33;1;40m/>\n')

#Icon Pack
if question2 == "c":
    os.chdir(icon_temp)
    clearConsole()
    with os.scandir() as i:
        for entry in i:
            if entry.is_file():
                print('\033[33;1;40m<item>\033[37;1;40m' , end = "")
                sys.stdout.write(Path(entry.name).resolve().stem)
                sys.stdout.write('\033[33;1;40m</item>\n')

#Trier
if question2 == "d":
    clearConsole()
    src_files = os.listdir(icon_temp)
    for file_name in src_files:
        full_file_name = os.path.join(icon_temp, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, icon_backup)
            shutil.copy(full_file_name, icon_all)

    questionfiledel = input("Tu veux supprimer les fichiers du dossier temp ? (o/n) : ")

    if questionfiledel == "o":
        [f.unlink() for f in Path(icon_temp).glob("*") if f.is_file()] 
        clearConsole()
        print("Les fichiers du dossier temp on été supprimé")
    if questionfiledel == "n":
        pass

input()
