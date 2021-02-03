import string
class vigenere:
    def __init__(self,key,raw):
        self.key = key
        self.raw = raw

        if len(key) != len(raw):
            raise ValueError("Key and Raw must have the same length")
    
    def encrypt(self):
        encrypted_str = ""
        for i in range(len(self.key)):
            encrypted_str += string.ascii_uppercase[ord(self.raw[i])-65+ord(self.key[i])-65]
        return encrypted_str


if __name__ == "__main__":
    test = vigenere("TES","EHE")
    print(test.encrypt())