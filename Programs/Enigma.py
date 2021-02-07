import string

liste_rotors = []

operation = input("ENCODE or DECODE : ") # ENCODE or DECODE
pseudo_random_number = int(input("Number of rotations : ")) # 4 for exemple
for i in range(3):
    rotor = input(f"Rotor {i} : ")  # format AJDKSIRUXBLHWTMCQGZNPYFVOE
    liste_rotors.append(rotor)
message = input("Your Message :") # format COUCOU


def _rotate(letter,key):
    alphabet = string.ascii_uppercase
    return alphabet[(alphabet.index(letter)+key)%26]

def _rotate_invert(letter,key):
    alphabet = string.ascii_uppercase
    index = alphabet.index(letter)-key
    while index < 0:
        index=26+index
    return alphabet[index]


def cesar(message,key,operation):
    compteur = 0
    message_return = ""
    for i in message:
        if operation == "ENCODE":
            message_return += _rotate(i,key+compteur)
        else:
            message_return += _rotate_invert(i,key+compteur)
        compteur += 1
    return message_return

def rotorize(message,liste_rotors,operation):
    alphabet = string.ascii_uppercase
    for rotor in liste_rotors:
        chaine = ""
        for i in message:
            if operation == "ENCODE":
                lettre = rotor[alphabet.index(i)]
            else:
                lettre = alphabet[rotor.index(i)]
            chaine += lettre
        message = chaine
    return message

if operation=="ENCODE":
    print(f"Encoded : {rotorize(cesar(message,pseudo_random_number,operation),liste_rotors,operation)}")
elif operation=="DECODE":
    liste_rotors = liste_rotors[::-1]
    print(f"Decoded : {cesar(rotorize(message,liste_rotors,operation),pseudo_random_number,operation)}")
