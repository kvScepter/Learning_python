from operator import itemgetter
import json
with open("./Data files/gamedata.json") as gamedata:
    pelit = json.load(gamedata)

#print(type(pelit))

#print(len(pelit))

#for i in range(len(pelit))[:3]:
   
        #print("pelin: ",pelit[i].get("title"), " metacritit arvo: ",pelit[i].get("metacriticScore"))
    
pelit2 = sorted(pelit, key=itemgetter("metacriticScore"), reverse=True)
pelit2 = pelit2 [:3]
for d in pelit2:
    print("Pelillä :", d["title"], " Metacritic arvo on :", d["metacriticScore"])
