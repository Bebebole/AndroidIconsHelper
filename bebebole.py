import os, glob, shutil, requests, re, ascii_magic
from google_play_scraper_py.scraper import PlayStoreScraper
from google_play_scraper import app

#les dossiers des icônes
icon_temp = "chemin du dossier"
icon_backup = "chemin du dossier"
icon_all = "chemin du dossier"


#quelques variables pour mon programme
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
datadir = os.getcwd()
tempdir = f'{datadir}/temp'


#il fait un dossier temp si il n'existe pas (pour télécharger des images par exemple)
try:
    os.mkdir("temp")
except FileExistsError:
    pass

#télécharge le txt avec les Compo
try :
    response = requests.get('https://raw.githubusercontent.com/Bebebole/BebeboleIconsPython/main/ComponentInfo_db.txt')
    open('ComponentInfo_db.txt', 'wb').write(response.content)
except FileExistsError:
    pass



#a
def appfilter() :
    os.chdir(icon_temp)
    clearConsole()
    for file in glob.glob("*.png"):
        file = file.replace('.png', '')
        print('\033[33;1;40m<item\n    \033[32;1;40mcomponent="ComponentInfo{}"\n    drawable="' + f'{file}" \033[33;1;40m/>\n\n')


#b
def drawable() :
    os.chdir(icon_temp)
    clearConsole()
    for file in glob.glob("*.png"):
        file = file.replace('.png', '')
        print(f'\033[33;1;40m<item \033[32;1;40mdrawable="{file}"\033[33;1;40m/>\n')


#c
def iconpack() :
    os.chdir(icon_temp)
    clearConsole()
    for file in glob.glob("*.png"):
        file = file.replace('.png', '')
        print("\033[33;1;40m<item>\033[37;1;40m{file}\033[33;1;40m</item>\n")


#d
def trier() : 
    clearConsole()
    for file_name in os.listdir(icon_temp):
        full_file_name = os.path.join(icon_temp, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, icon_backup)
            shutil.copy(full_file_name, icon_all)


#e
def componentinfo() :
    clearConsole()
    appsearch= input("Le nom de l'app : ")
    scraper = PlayStoreScraper()
    results = scraper.get_app_ids_for_query(appsearch)
    
    clearConsole()
    print(f"\033[32;1;40mAppId : \033[33;1;40m{results[0]}\n\n\033[32;1;40mApp Name : \033[33;1;40m{appsearch}")

    with open("ComponentInfo_db.txt") as openfile:
        for line in openfile:
            if results[0] in line:
                line = re.match(r'^.*?\"', line).group(0)
                line = line.replace(' "',"")
                print(f"\n\033[32;1;40mComponentInfo :\033[33;1;40m{line}")

    result = app(
        results[0],
        lang='en',
        country='us'
    )

    os.chdir(tempdir)
    response = requests.get(result["icon"])
    open('imgdl.jpg', 'wb').write(response.content)
    output = ascii_magic.from_image_file("imgdl.jpg",columns=40,char="#")
    print("\n")
    ascii_magic.to_terminal(output)
    os.remove("imgdl.jpg")


#j'ai vraiment besoin d'faire un dessin ?
def main() :
    clearConsole()
    print("\033[1;32;40m  ____       _          _           _\n |  _ \     | |        | |         | |\n | |_) | ___| |__   ___| |__   ___ | | ___\n |  _ < / _ \ '_ \ / _ \ '_ \ / _ \| |/ _ \ \n | |_) |  __/ |_) |  __/ |_) | (_) | |  __/\n |____/ \___|_.__/ \___|_.__/ \___/|_|\___|\n")
    question = input("\n\n\033[34;1;40mSalut ! \033[37;1;40mTu veux faire quoi ?\n\n[a] Remplir le fichier \033[31;1;40mappfilter\n\033[37;1;40m[b] Remplir le fichier \033[31;1;40mdrawable\n\033[37;1;40m[c] Remplir le fichier \033[31;1;40micon_pack\n\033[37;1;40m[d] Trier les icônes\n\033[37;1;40m[e] Trouver le ComponentInfo d'une App\n\n\033[33;1;40mAlors ? : ")

    if question == "a" :
        appfilter()
    elif question == "b" :
        drawable()
    elif question == "c" :
        iconpack()
    elif question == "d" :
        trier()
    elif question == "e" :
        componentinfo()
    else :
        print("\n???")

main()