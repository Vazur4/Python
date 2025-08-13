

from Encode_logo.art import logo
from uu import decode
print(logo)
def caesar(direction, original_text, shift_amount):
    if direction in "decode":
        shift_amount *= -1
    cipher_text = ""
    for letter in original_text:
        if letter == " " or letter in numbers:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    
    print(f"Result: {cipher_text}")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

continu = False
while not continu:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))







    

    caesar(direction, text, shift)
    option =input("type yes if you want to go again. Otherwise, type no")
    if option.upper() in "yes":
        continu = True
    


