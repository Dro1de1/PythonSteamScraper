from urllib import parse
from urllib import request
import json

with open("./data/data.json") as f:
    data = f.read()
steamSticker = json.loads(data)
print(len(steamSticker))

# for sticker in steamSticker:
#     if sticker==sticker[0]:
#         print("error")
#     else:
#         x= sticker["Name"]
#         print(str(x))

COLOR_RESET ="\033[0;m"
BOLD        ="\033[1m"
BLACK_TEXT  ="\033[30;1m"
RED_TEXT    ="\033[31;1m"
GREEN_TEXT  ="\033[32;1m"
YELLOW_TEXT ="\033[33;1m"
BLUE_TEXT   ="\033[34;1m"
MAGENTA_TEXT="\033[35;1m"
CYAN_TEXT   ="\033[36;1m"
WHITE_TEXT  ="\033[37;1m"

print(BOLD+"Nr. "+COLOR_RESET+RED_TEXT+" xxx | xxx | xxx "+COLOR_RESET+" "+"Anzahl"+" "+"Einzelkaufpreis"+" "+"Verkaufpreis"+" "+"Profit"+" "+"Gesammter Profit")
b=1
for n in range(1,len(steamSticker)):
    s = steamSticker[n]
    Name=s["Name"]
    Stueckzahl=s["Stueckzahl"]
    Einkaufspreis=s["Einkaufspreis"]
    Verkaufspreis=0
    Profit=0
    ProfitG=0
    result =str(b)+". "+str(Name)+"  "+str(Stueckzahl)+"  "+str(Einkaufspreis)+"  "+str(Verkaufspreis)+"  "+str(Profit)+"  "+str(ProfitG)
    b+=1
    print(result)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

# for i in range(2,len(steamSticker)): # for Schleife mit i als Zähler i++ in einer Spanne von 0 bis zur Länge des dictionarys 'steamStickerId'
#     AssembleStickerHash(i) # startet die Funktion mit Zahl für passenden Sticker

def AssembleStickerHash(n):
    steamStickerHash = open("data.lson","w")
    steamSticker = json.loads("/data/data.json")
    steamSticker[1]["Name"]
    return steamStickerHash, steamSticker
