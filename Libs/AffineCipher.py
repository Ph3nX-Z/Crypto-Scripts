import string
class AffineCipher:
    def __init__(self,raw,a,b):
        self.raw = raw
        self.a = int(a)
        self.b = int(b)
    
    def encrypt(self):
        return "".join([string.ascii_lowercase[(self.a*int(element)+self.b)%26] for element in [[str(num) for num in range(26)][string.ascii_lowercase.index(i)] for i in self.raw]])

test = AffineCipher("test",12,3)
print(test.encrypt())