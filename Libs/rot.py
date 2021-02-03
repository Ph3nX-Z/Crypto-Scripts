import string
class rot:
    def __init__(self,rotations,raw):
        self.raw = raw
        self.rotations = rotations

    def encrypt(self):
        return "".join([string.ascii_lowercase[(string.ascii_lowercase.index(i)+self.rotations)%26] for i in self.raw])


if __name__ == "__main__":
    test = rot(20,"aha")
    print(test.encrypt())