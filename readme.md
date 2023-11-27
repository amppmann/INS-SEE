- **1. Perform encryption, decryption using the Caesar cipher substitution 
techniques**

```py
def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += ""

    return result


def decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += ""

    return result


while True:
    print("Enter a choice (1-3) ")
    choice = int(input("1.Encrypt\n2.Decrypt\n3.Exit :"))

    if choice == 1:
        text = input("Enter a text :")
        key = int(input("Enter a key :"))
        print("Encrypting...")

        ciphertext = encrypt(text, key)

        print("Cipher text : ", ciphertext)

    elif choice == 2:
        print("Decrypting...")
        print("Plain text : ", decrypt(ciphertext, key))
    elif choice == 3:
        break
    else:
        print("Invalid choice ")

```

- **2. Perform encryption, decryption using the Monoalphabetic cipher
substitution techniques**

```py


l = []

def encrypt(a,dict1):
    for x in a:
        y = dict1.get(x)
        l.append(y)
        
    return "".join(l)


def decrypt(dict1):
    keyList = list(dict1.keys())
    valueList = list(dict1.values())

    print("Decrypted value...")

    for i in l:
        position = valueList.index(i)
        print(keyList[position],end="")

        
dict2 = {
'A':'Z',
'B':'Y',
'C':'X',
'D':'W',
'E':'V',
'F':'U',
'G':'T',
'H':'S',
'I':'R',
'J':'Q',
'K':'P',
'L':'O',
'M':'N',
'N':'M',
'O':'L',
'P':'K',
'Q':'J',
'R':'I',
'S':'H',
'T':'G',
'U':'F',
'V':'E',
'W':'D',
'X':'C',
'Y':'B',
'Z':'A',
'a':'z',
'b':'y',
'c':'x',
'd':'w',
'e':'v',
'f':'u',
'g':'t',
'h':'s',
'i':'r',
'j':'q',
'k':'p',
'l':'o',
'm':'n',
'n':'m',
'o':'l',
'p':'k',
'q':'j',
'r':'i',
's':'h',
't':'g',
'u':'f',
'v':'e',
'w':'d',
'x':'c',
'y':'b',
'z':'a'

}

text = input("Enter a text : ")
encrypt = encrypt(text,dict2)

print("Encrypting...")
print("Cipher text : ",encrypt)

print("Decrypting...")
decrypt(dict2)

```    

