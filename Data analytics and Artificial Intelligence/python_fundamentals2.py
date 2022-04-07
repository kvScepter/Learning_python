# Add the following cars to the existing list of dictionary objects:
#- Red Toyota Corolla (1985)
#- Lightblue Ford Mustang (1965)
#- Black Pontiac Firebird (1987)

#cars on the list of dict
cars = [{"make":"Ford","model":"escort","color":"green","year":1994},{"make":"Lexus","model":"IS250","color":"beige","year":2013},{"make":"Volvo","model":"S40","color":"blue","year":1998}]

#car to add
cars2 = [{"make":"Toyota", "model":"Corolla","color":"red","year":1985},{"make":"Ford", "model":"Mustang","color":"Lightblue","year":1965},{"make":"Pontiac", "model":"Firebird","color":"Black","year":1987}]

cars.extend(cars2)
print(cars)
