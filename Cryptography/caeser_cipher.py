# The alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Function to encrypt a text based on the Rot-13 method
def encrypt(text):
        
    
    text = text.lower()
    
    # the encrypted message
    result = ''
    
    # Replace each letter in the string with a letter which is 13 positions further
    for char in text:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) + 13) % 26]
        else:
            result += char
    return result
