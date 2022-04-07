# Sentence
s = "Gary must look towards the future in order to gather enough information from the target."

# print first ten and last ten characters concatenated
print(s[:10], s[-10:])

# Count the number of white spaces between words from the previous sentence and divide that number with the length of the sentence.
number_of_whitespace = s.count(" ") / len(s) 
print(number_of_whitespace)

# Convert the sentence presented below to list using commas (,) as separators. Then create a new list which contains only the last three items from the list.
# Sentence
s2 = "Occaecat short ribs incididunt laboris. Bresaola, brisket ex, landjaeger ad, boudin pariatur frankfurter eu flank. Enim tail short ribs, shoulder duis minim excepteur, deserunt lorem porchetta. Dolor chicken spare ribs, id in, ball, tip, hamburger labore venison consectetur cupidatat."
lista = s2.split(" ")
print(lista)
uusi_lista = lista[-3:]
print(uusi_lista)
