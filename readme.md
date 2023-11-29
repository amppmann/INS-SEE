### **PART A**

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

- **3.Implement Diffie-Hellman Algorithm to establish a shared secret between two parties that can be used for secret communication to exchange data over a public network.**


```py
import math

q = int(input("Enter a prime number : "))
a = int(input("Enter a primitive root :"))


Xa = int(input("Enter the private key of A :"))
Xb = int(input("Enter the private key of B : "))


Ya = math.pow(a, Xa) % q
Yb = math.pow(a, Xb) % q


print("Public key of  A  : ",Ya)
print("Public key of B : ",Yb)

Ka = math.pow(Yb,Xa)%q
Kb = math.pow(Ya,Xb)%q

print("Shared key for A : ",Ka)
print("Shared key for B : ",Kb)```

```

- **5.Perform encryption,decryption using the vignere cipher (Polyalphabetic) substitution techniques.**

```py



def vignere(key,message):
    
    message = message.lower()
    message = message.replace(' ','')
    m = len(key)
    
    cipherText = ""

    for i in range(len(message)):
        letter = message[i]
        k = key[i%m]
        cipherText+=chr((ord(letter)+k-97)%26+97)

    return cipherText


if __name__ == "__main__":
    print("Encrypting....")
    key = input("Enter a keystream : ")
    key = [ord(letter) - 97 for letter in key]

    message = input("Enter a message : ")
    cipherText = vignere(key,message)
    print("CipherText : ",cipherText)

    print("Decrypting...")

    key = [-1*k for k in key]
    plainText = vignere(key,cipherText)
    print("Plain text : ",plainText)
```


### **PART B**


- **1.**

```py
```


- **2.**
```py```


- **3.**
```py```


- **4.Implement key generation technique used in Data Encryption Standard(DES)**

```py
import random

s = input("Enter a string : ")

result = ''.join(format(ord(i),'08b') for i in s)
answer = ""


for i in range(len(result)):
    if(i%8!=0):
        answer+=result[i]


l = int(len(answer)/2)
left = answer[:l]
right = answer[l:]

lt = [2,3,6,7,1,6,5,9]
keys = []

for i in range(0,8):
    newKey = ""
    newAnswer = ""

    nl=int(left,2)
    nl=bin(nl<<lt[i])
    num=2+lt[i]

    nr = int(right,2)
    nr = bin(nr<<lt[i])
    num=2+lt[i]
    
    newKey = nr[num:]+nl[num:]
    rm =[]
    
    while(len(rm)!=8):
        r = random.randint(0,len(newKey)-1)
        if(r not in rm):
            rm.append(r)
    
    for i in range(len(newKey)):
        if(i not in rm):
            newAnswer+=newKey[i]

    keys.append(newAnswer)

for i in range(0,len(keys)):
    print("Key ",i+1," = ",keys[i])```
```

- **5.Implement encryption & decryption using RSA**
```py
import math

def gcd(a,b):
    temp = 0
    
    while(b!=0):
        temp = a%b
        if(temp==0):
            return b
        a = b
        b = temp
        
p = 3
q = 7
n = p*q
e = 2
pi = (p-1)*(q-1)

while(e<pi):
    if(gcd(e,pi)==1):
        break
    else:
        e+=1
        
        
k  =2
d = (1+(pi*k))/e
msg = 12.0

print("Message data : ",msg)

c = pow(msg,e)
c = math.fmod(c,n)
print("Encrypted data : ",c)

m = pow(c,d)
m = math.fmod(m,n)
print("Original message data : ",m)


```