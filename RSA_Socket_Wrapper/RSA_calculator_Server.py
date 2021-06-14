import random
import math
from Crypto.PublicKey import RSA
import socket



def modulo_fast(a,b,c):
    return pow(a,b,c)

def random_prime_choice(num_range):
    #is_prime = lambda x:True if [x%j != 0 for j in range(2,x)].count(True) == x-2 else False
    while True:
        prime = True
        number = random.choice(range(int(num_range/100),num_range))
        for i in range(2,20):
            if number%i == 0:
                prime = False
                break
        if prime == True:
            return number

class Rsa_Cipher:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.r = 0
        self.e = 0
        self.d = 0
        self.private_key_pair = (0,0)
        self.public_key_pair = (0,0)
        self.pub_cert = """"""


    def encrypt(self,message,cert):
        pub_key = RSA.importKey(cert)
        n = pub_key.n
        e = pub_key.e
        phrase_deci_enc = []

        for i in message:
            phrase_deci_enc.append(str(modulo_fast(ord(i),e,n)))
        return " ".join(phrase_deci_enc).encode()

    def decrypt(self,message):
        d = self.d
        n = self.n
        message = message.decode()
        chaine = ""
        for i in message.split(" "):
            k = int(i)
            #print(k,d,n)
            to_add = modulo_fast(k,d,n)
            chaine+=str(chr(to_add))
        return chaine


    def generate_cert(self):
        self.p = random_prime_choice(50000000)
        self.q = random_prime_choice(50000000)
        self.n = self.p * self.q
        self.r = (self.p - 1) * (self.q - 1)
        n = -1*(self.r-1)
        r = -1*self.r
        liste_good = []
        for i in range(100000):
            n=n-r
            liste_good.append(n)
        liste_good = liste_good[::-1]
        factorizables={}
        for i in liste_good:
            for j in range(2, 20):
                if i % j == 0:
                    factorizables[i]=f"{j} {int(i / j)}"
                    break
        to_keep = {}
        for i in factorizables:
            if (int(factorizables[i].split(" ")[0])*int(factorizables[i].split(" ")[1])) % self.r == 1:
                if math.gcd(int(factorizables[i].split(" ")[0]),self.n)==1 and math.gcd(int(factorizables[i].split(" ")[1]),self.n)==1:
                    to_keep[i]=factorizables[i]
        key = random.choice(list(to_keep.keys()))

        e = int(to_keep[key].split(" ")[0])
        d = int(to_keep[key].split(" ")[1])

        self.public_key_pair = (e,self.n)
        self.private_key_pair = (d,self.n)
        self.e = e
        self.d = d


        rsaKey = RSA.construct((self.n, self.e))
        pubKey = rsaKey.publickey()
        pubKeyPEM = rsaKey.exportKey()

        self.public_key = pubKeyPEM.decode('ascii')

        return pubKeyPEM.decode('ascii')

    def generate_and_check(self):
        valid = False
        while not valid:
            cert = self.generate_cert()
            en = self.encrypt("a",cert)
            try:
                de = self.decrypt(en)
            except:
                de = ""
            if de == "a":
                valid = True
        return cert

test = Rsa_Cipher()
cert = test.generate_and_check()


host = "0.0.0.0"
port = 5003

buffer = 1024

s = socket.socket()

s.bind((host, port))
s.listen(5)
print(f"Listening at {host}:{port} ...")

client_socket, client_address = s.accept() # accept any connections
print(f"{client_address[0]} on port : {client_address[1]}                    [+]Connected")

distant_cert = client_socket.recv(buffer).decode()
print(distant_cert)
client_socket.send(cert.encode())

while True:
    results = client_socket.recv(buffer)
    decrypted = test.decrypt(results)
    print(f"From {client_address[0]}>>{decrypted}")
    command = input(f"Message to {client_address[0]}>>")
    encrypted = test.encrypt(command,distant_cert)
    client_socket.send(encrypted)
client_socket.close()

s.close()