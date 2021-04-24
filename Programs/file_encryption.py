import binascii

def str_to_bin(string):
    return "".join([str(bin(j))[2:] for j in [ord(i) for i in string]])



def cipher(intext):
    salt = "itisasalt"

    password = str_to_bin(salt)
    file_content=str_to_bin(intext)

    if len(file_content)%4 != 0:
        file_content = "0" + file_content

    while len(password) != len(file_content):
        if len(password)<len(file_content):
            if len(password)%3==0:
                password += "0"
            else:
                password += "1"
        elif len(password)>len(file_content):
            password = password[:-1]


    tofile="".join([str(int(password[i])^int(file_content[i])) for i in range(len(password))])

    tofile = int(tofile,2)

    toreturn = []
    for i in str(tofile):
        toreturn.append(chr(49+int(int(i)*8.1)))

    return "".join(toreturn)

def hash(intext,rounds):
    for loop in range(rounds):
        intext = cipher(intext)
    return intext
print(hash("thisisapassword",1))