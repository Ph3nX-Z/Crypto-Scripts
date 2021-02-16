from hashlib import sha256
import time
import random
import string



class Block:
    def __init__(self,numero_block, data, block=None):
        self.num_block = 0 if not block else block.num_block + 1
        self.nonce = 0
        self.data = data
        self.hash_precedent = None if not block else block.hash
        self.hash = self._hashage()
        self.bloc_precedent = None if not block else block
        self.valide = False
        self.time = 0
    def _hashage(self):
        if self.hash_precedent:
            chaine = str(self.num_block)+str(self.nonce)+self.data+self.hash_precedent
        else:
            chaine = str(self.num_block)+str(self.nonce)+self.data
        self.hash = sha256(bytes(chaine, 'utf-8')).hexdigest()
        return sha256(bytes(chaine, 'utf-8')).hexdigest()
    def __str__(self):
        table = '\n'.join([f"\nInfos for Block number {self.num_block}",f"- Last hash : {self.hash_precedent}",f"- Hash      : {self.hash}",f"- Valid     : {self.valide}",f"- Nonce     : {self.nonce}",f"- Time      : {self.time}\n"])
        return table
    def minage(self):
        start = time.time()
        print('\033[94m'+f"\n[*] Mining Block {self.num_block}"+'\033[0m')
        self.hash = ""
        while self.hash[:2]!="00":
            self._hashage()
            self.nonce += 1
        self.nonce -= 1
        stop = time.time()
        print('\033[94m'+f"Time : {stop-start}"+'\033[0m')
        self.time = stop-start
        self.valide = True
        return '\033[92mValid Hash Found :' + str(self.hash)+str(self.nonce)+'\033[0m'
    def chaine_valide(self):
        block = self
        while block.bloc_precedent!= None:
            #print(f'Checking : {block}')
            if not block.valide:
                return False
            block = block.bloc_precedent
        return True
    
    def check_mine(self):
        print('\033[93m'+"\n[+] Auto Mine:"+'\033[0m')
        liste_blocs = []
        if not self.chaine_valide():
            block = self
            while block.valide != False:
                liste_blocs.append(block)
                block = block.bloc_precedent
            liste_blocs.append(block)
            for i in liste_blocs[::-1]:
                i.hash_precedent = i.bloc_precedent.hash
                i._hashage()
                i.minage()
                
            return "Done"
        else:
            print('\033[92m'+"[~] Verification"+'\033[0m')
            return True

    def auto_mine(self):
        while self.check_mine()!=True:
            pass

if __name__ == "__main__":

    print('\033[93m'+"[+] Initial Mining :"+'\033[0m')
    block = Block(1, "coucou")
    block.minage()

    """
    block2 = Block(2,"salut",block)
    block3 = Block(3,"hey",block2)
    block4 = Block(4,"hey2",block3)
    block4.auto_mine()

    print(block,block2,block3,block4)"""
    alphabet = string.ascii_lowercase
    blocks = []
    blocks.append(block)
    for i in range(20):
        chaine = "".join(random.choice(alphabet) for j in range(100))
        blocks.append(Block(i,chaine,blocks[-1]))
    
    blocks[-1].auto_mine()

    [print(k) for k in blocks]



    print('\033[92m'+"\n[+] Hashs Verified"+'\033[0m') if blocks[-1].chaine_valide() else print('\033[91m'+"\n[+] Invalid Hashs"+'\033[0m')