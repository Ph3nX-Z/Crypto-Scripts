import string
class atbash_num:
    def __init__(self,raw):
        self.raw = raw
    
    def encrypt(self):
        return "".join([string.ascii_lowercase[::-1][string.ascii_lowercase.index(i)] for i in self.raw])

if __name__ == "__main__":
    test = atbash_num("test")
    print(test.encrypt())
