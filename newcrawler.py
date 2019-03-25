from urllib import parse
from urllib import request
import json

steamStickerId = [
    "BIG",
    "Ninjas in Pyjamas",
    "Astralis",
    "Team Liquid",
    "Team Spirit",
    "FACEIT",
    "HellRaisers",
    "Cloud9",
    "Winstrike Team",
    "Rogue",
    "FaZe Clan"
]

link = 'https://steamcommunity.com/market/priceoverview/?'

params = {
        'currency': '3', # 1=$, 2=£, 3=€
        'appid': '730', # CSGO=730
        'market_hash_name':''
    }

stickerNr = 0

def AssembleStickerHash(n):
    steamStickerHash = "Sticker | "+ steamStickerId[n] +" | London 2018"
    print(steamStickerHash)
    return steamStickerHash

def RequestPrice(b): 
    params['market_hash_name'] = str(AssembleStickerHash(b)) # fügt den Stickernamen in Stingform als Value dem dictionary Eintrag 'market_hash_name' hinzu
    steamStickerLinkHash = link + str(parse.urlencode(params)) # fügt Anfangslink und urlencodete params als String zusammen zu fertigem Link
    print(steamStickerLinkHash)
    steamItemPriceR = request.urlopen(steamStickerLinkHash) # fragt die Seite nach der JSON Datei
    data = steamItemPriceR.read() # liest angeforderte Seite
    json_object1 = json.loads(data.decode('utf-8')) # decodet die gelesene Seite 'data' zu einem JSON Objekt
    print(json_object1["lowest_price"]) # gibt den niedrigsten Preis zurück

for i in range(0,len(steamStickerId)): # for Schleife mit i als Zähler i++ in einer Spanne von 0 bis zur Länge des dictionarys 'steamStickerId'
    RequestPrice(i) # startet die Funktion mit Zahl für passenden Sticker




#http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>

#https://steamcommunity.com/market/search/render/?query=&start=0&norender=1&count=10

#https://steamcommunity.com/market/priceoverview/?currency=<currencyno€=3>&appid=<csgo=730>&market_hash_name=<name of he skin with urlencode>

# https://www.w3schools.com/tags/ref_urlencode.asp
# %2F   =   /
# %28   =   (
# %29   =   )
# %20   =   <Space>
# %7C   =   |
# %3A   =   :
# %3F   =   ?
# %e2 %84 %a2 wird zu kleinem tm
# https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name=AWP | Atheris (Field-Tested)
# https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name=AWP%20%7C%20Atheris%20%28Field-Tested%29
