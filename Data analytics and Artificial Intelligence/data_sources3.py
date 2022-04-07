import xml.etree.ElementTree as e
from operator import itemgetter

tree = e.parse("netflix_titles.xml")
root = tree.getroot()

movie_collection = []

titles = []
for i in root[0]:
    titles.append(i.tag)

for elem in root:
    movie = []
    for subelem in elem:
        movie.append(subelem.text)
    movie_collection.append(movie)
#print(movie_collection[:50])

movies = []
for lst in movie_collection:
    movie_obj = {}
    for i in range(len(lst)):
        movie_obj[titles[i]] = lst[i]
    movies.append(movie_obj)
#print(movies[:50])

movies2 = sorted(movies, key=itemgetter("release_year"), reverse=True)
for d in movies:
    if float(d["release_year"]) == 2017:
        print("movie:", d["title"], "--> released in year :", d["release_year"])
 
duration = 0
for i in movies:
    pituus = (i["duration"])
    
    if pituus >= 15 and pituus <=20:
        duration += 1
print(duration)
