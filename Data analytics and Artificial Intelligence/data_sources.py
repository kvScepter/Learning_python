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


pelit3 = sorted(pelit, key=itemgetter("savings"), reverse=True)
for d in pelit3:
    if float(d["savings"]) >= 90:
        print("Peli :", d["title"], ", Säästät nyt", d["savings"][:5], "%")

        
pelit4 = sorted(pelit, key=itemgetter("metacriticScore"), reverse=True)
for d in pelit4:
    if d["metacriticScore"] > d["steamRatingPercent"]:
        print("Pelillä", d["title"], "on suurempi metacritic arvo joka on", d["metacriticScore"], "vs Steam rating percent", d["steamRatingPercent"])      
  
