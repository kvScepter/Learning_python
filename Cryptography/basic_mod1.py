import string

with open("decrypthis.txt") as filp:
          
          contents = filp.read()
          #make list of numbers to list
          numbers = [ int(value) for value in contents.split() ]
          # print(numbers)
          for number in numbers:
                    modulus = number % 37
                    
                    if modulus in range(0, 26):
                              print(string.ascii_letters[modulus], end="")
                    elif:     modulus in range(26, 36):
                              print(string.digits[modulus-26], end="")
                    else:
                              print("_", end="")
                    
         
          
