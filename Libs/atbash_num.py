import string
class atbash_num:
    def __init__(self,raw):
        self.raw = raw
    
    def encrypt(self):
        return " ".join([[str(num) for num in range(26)][string.ascii_lowercase.index(i)] for i in self.raw])

if __name__ == "__main__":
    test = atbash_num("coucou")
    print(test.encrypt())