import csv
with open("./Data files/earthquakes.csv") as f:
    quake_data = csv.reader(f)
    next(quake_data)
    
    minor = 0
    light = 0
    moderate = 0
    strong = 0
    major = 0
    mega = 0
    
    for i in quake_data:
        mag = float(i[8]) #magnitude oli 8 rivillä
        
        if mag < 2.5:
            minor += 1

        if mag >= 2.5 and mag <=5.4:
            light += 1
            
        if mag >= 5.5 and mag <= 6.0:
            moderate += 1
        
        if mag >= 6.1 and mag <= 6.9:
            strong += 1
        
        if mag >= 7.0 and mag <= 7.9:
            major += 1
            
        if mag >= 8.0:
            mega += 1
            
print("Minor eartquakes in database", minor)
print("Light eartquakes in database",light)
print("Moderate eartquakes in database",moderate)
print("Strong eartquakes in database",strong)
print("Major eartquakes in database",major)
print("MEGA eartquakes in database",mega)
