import string
class bifidCipher:
    def __init__(self,raw):
        self.grille = [[i for i in string.ascii_lowercase][0:-1][j::5] for j in range(5)]
        self.raw = raw
    
    def encrypt(self):
        liste_y,liste_x = [],[]
        for i in self.raw:
            for ligne in self.grille:
                if i in ligne:
                    liste_y.append(str(self.grille.index(ligne)))
                    liste_x.append(str(ligne.index(i)))
        liste_x_y = "".join(liste_y+liste_x)
        paires = [liste_x_y[i:i+2] for i in range(0, len(liste_x_y), 2)]
        return "".join(self.grille[int(str(nombres)[0])][int(str(nombres)[1])] for nombres in paires)




test = bifidCipher("test")
print(test.encrypt())
