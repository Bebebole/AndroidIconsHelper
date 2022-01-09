import os
import sys
from pathlib import Path
import requests
import configparser
import shutil
import re
try:
	from googlesearch import search
except ImportError:
	print("Tu dois installer google avec pip ! (pip install google)")


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
    response = requests.get('https://raw.githubusercontent.com/Bebebole/BebeboleIconsPython/main/Terminal/Resources/pathsettings.ini')
    file.write(response.text)
    file.close()
    print("Tu dois mettre à jour le fichier pour que le programme marche correctement !\nIl faut modifier le fichier 'pathsettings.ini'(C:\Program Files\Bebebole\IconPackMaker)")
    input()

except FileExistsError:
    pass

try :
    response = requests.get('https://raw.githubusercontent.com/Bebebole/BebeboleIconsPython/main/Terminal/Resources/ComponentInfo_db.txt')
    open('ComponentInfo_db.txt', 'wb').write(response.content)

except FileExistsError:
    pass

config = configparser.ConfigParser()
config.read("pathsettings.ini")
icon_temp = config.get("path", "icon_temp")
icon_backup = config.get("path", "icon_backup")
icon_all = config.get("path", "icon_all")

print("\n \033[1;32;40m██████╗░███████╗██████╗░███████╗██████╗░░█████╗░██╗░░░░░███████╗\n ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔════╝\n ██████╦╝█████╗░░██████╦╝█████╗░░██████╦╝██║░░██║██║░░░░░█████╗░░\n ██╔══██╗██╔══╝░░██╔══██╗██╔══╝░░██╔══██╗██║░░██║██║░░░░░██╔══╝░░\n ██████╦╝███████╗██████╦╝███████╗██████╦╝╚█████╔╝███████╗███████╗\n ╚═════╝░╚══════╝╚═════╝░╚══════╝╚═════╝░░╚════╝░╚══════╝╚══════╝\n")
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
question2 = input("\n\n\033[34;1;40mSalut ! \033[37;1;40mTu veux faire quoi ?\n\n[a] Remplir le fichier \033[31;1;40mappfilter\n\033[37;1;40m[b] Remplir le fichier \033[31;1;40mdrawable\n\033[37;1;40m[c] Remplir le fichier \033[31;1;40micon_pack\n\033[37;1;40m[d] Trier les icônes\n\033[37;1;40m[e] Trouver le ComponentInfo d'une App\n\n\033[33;1;40mAlors ? : ")


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

#ComponentInfo
if question2 == "e":
    clearConsole()
    appsearch= input("Le nom de l'app : ")
    searchongoogle1 = "m.apkpure.com" + appsearch
    linkapk = "https://m.apkpure.com/*/"


    for respo in search(searchongoogle1, tld="co.in", num=10, stop=1, pause=2):
        appid1 = respo.lstrip(linkapk)

    appid2 = re.sub(r'^.*?/', '/', appid1)
    appid3 = appid2.lstrip("/")

    clearConsole()
    print(appsearch + " : " + appid3 + "\n")

    questionsearchdbci = input("Tu veux chercher dans la db ? (o/n) : ")

    if questionsearchdbci == "o":
        clearConsole()
        os.chdir("C:\Program Files\Bebebole\IconPackMaker")
        with open("ComponentInfo_db.txt") as openfile:
            for line in openfile:
                if appid3 in line:
                    print(line + "\n\n" + appsearch + " : " + appid3)
    if questionsearchdbci == "n":
            pass

input()