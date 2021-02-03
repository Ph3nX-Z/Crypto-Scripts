import string
import random


class xor:
    def __init__(self,raw,key):
        self.raw = raw
        self.encrypted = None
        self.key = key
        self.decrypted = None

    def encrypt(self):
        while len(self.key)<len(self.raw):
            self.key += string.ascii_lowercase[random.randint(0,25)]
        bin_raw = ''.join(format(ord(x), 'b') for x in self.raw)
        bin_key = ''.join(format(ord(x), 'b') for x in self.key)
        self.encrypted = "".join([str(int(bin_raw[i])^int(bin_key[i])) for i in range(len(bin_raw))])
        return self.encrypted


    def decrypt(self,binary,key):
        bin_key = ''.join(format(ord(x), 'b') for x in key)
        bin_raw = binary
        self.decrypted = "".join([str(int(bin_raw[i])^int(bin_key[i])) for i in range(len(bin_raw))])
        decrypted_split = list(map(''.join, zip(*[iter(self.decrypted)]*7)))
        ascii_string = "".join([chr(int(binary, 2)) for binary in decrypted_split])
        self.decrypted = ascii_string
        return self.decrypted
    def __str__(self):
        return f"Raw : {self.raw}\nEncrypted : {self.encrypted}\nKey : {self.key}"


if __name__ == "__main__":
    value = xor("testtests","pass")
    print(value.encrypt())