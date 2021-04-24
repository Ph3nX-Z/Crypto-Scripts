import binascii
import sys

def encrypt(file,password):
    chaine = ""
    with open(file,"rb") as source:
        bytes = source.read()
    binary = bin(int(binascii.hexlify(bytes), 16))[2:]
    password = bin(int(binascii.hexlify(password), 16))[2:]
    while len(binary) != len(password):
        if len(binary)<len(password):
            password=password[:len(binary)]
        elif len(binary)>len(password):
            password += password
    for i in range(len(binary)):
        chaine+=str(int(binary[i])^int(password[i]))
    with open(file,"wb") as outfile:
        outfile.write(chaine.encode("ascii"))

def decrypt(file,password):
    chaine = ""
    with open(file,"rb") as source:
        bytes = source.read()
    binary = bytes.decode("ascii")
    password = bin(int(binascii.hexlify(password), 16))[2:]
    while len(binary) != len(password):
        if len(binary)<len(password):
            password=password[:len(binary)]
        elif len(binary)>len(password):
            password += password
    for i in range(len(binary)):
        chaine+=str(int(binary[i])^int(password[i]))
    chaine = int(chaine,2)
    chaine = binascii.unhexlify('%x' % chaine)
    with open(file,'wb') as outfile:
        outfile.write(chaine)

encrypt("a.pdf",b"pass")
