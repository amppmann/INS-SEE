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

- **4.Implement key generation process using ECC(Elliptic curve cryptographic) function**

```py




```

- **5.Perform encryption,decryption using the vignere cipher (Polyalphabetic) substitution techniques.**

```py
import tinyec 
from tinyec import registry 
import secrets 

curve = registry.get_curve('brainpoolP256r1') 

def compress_point(point): 
    return hex(point.x) + hex(point.y % 2)[2:] 


def getEnKey(pubKey): 
   ciPrivKey = secrets.randbelow(curve.field.n) 
   ciPubKey = ciPrivKey * curve.g 
   enKey = ciPrivKey * pubKey 
   return (enKey, ciPubKey) 

senderPriKey = secrets.randbelow(curve.field.n) 
senderPubKey = senderPriKey * curve.g 


print("Sender's Private Key: " + hex(senderPriKey)) 
print("Sender's Public Key: " + compress_point(senderPubKey)) 


(enKeySender, ciPubKeySender) = getEnKey(senderPubKey) 

print("\nSender's Ciphertext Public Key: " + compress_point(ciPubKeySender)) 
print("Sender's Encryption Key: " + compress_point(enKeySender)) 

receiverPriKey = secrets.randbelow(curve.field.n) 
receiverPubKey = receiverPriKey * curve.g 


print("\nReceiver's Private Key: " + hex(receiverPriKey)) 
print("Receiver's Public Key: " + compress_point(receiverPubKey)) 

(enKeyReceiver, ciPubKeyReceiver) = getEnKey(receiverPubKey) 

print("\nReceiver's Ciphertext Public Key: " + compress_point(ciPubKeyReceiver)) 
print("Receiver's Encryption Key: " + compress_point(enKeyReceiver)) 
```

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


- **1.Write a program to demonstrate the working of Feistel Cipher algorithm**

```py

# Fiestel cipher


s = input("Enter a string : ")


# This will convert string to ASCII--> then to 8-bit binary
result = "".join(format(ord(i),'08b') for i in s)


print("Result : ",result)

l = int(len(result)/2)

left = result[:l]
right = result[l:]


k = input("Enter a key : ")
key = "".join(format(ord(i),'08b') for i in k)
s = bin(int(right,2)+int(key,2))
answer = bin(int(s[2:],2)^int(left,2))

newr= answer[2:]
newl = right


newr,newl = newl,newr

s= bin(int(newr,2)+int(key,2))
ans = bin(int(s[2:],2) ^ int(newl,2))
nl = newr

nr = ans[2:]
nl,nr = nr,nl
cipher = nl+nr

if(len(cipher)!=len(result)):
    while(len(cipher)!=len(result)):
        cipher="0"+cipher

print(cipher)

plainText = ""
for i in range(0,len(cipher),8):
    temp = cipher[i:i+8]
    d = int(temp,2)
    plainText=plainText+chr(d)
    
print(plainText)
```


- **2.Perform encryption,decryption using the Hill Cipher substitution techniques**
```py

import numpy as np


l = list(map(int,input("Enter the key matrix : ").split()))
keyMatrix = np.array(l).reshape(2,2)
det = keyMatrix[0,0]*keyMatrix[1,1] - keyMatrix[0,1]*keyMatrix[1,0]


det = pow(int(det),1,26)

detInverse = pow(det,-1,26)

keyInverse  = np.array([[keyMatrix[1,1],-keyMatrix[0,1]],[-keyMatrix[1,0],keyMatrix[0,0]]])

keyInverse = (detInverse*keyInverse)%26


def text_to_num(text):
    return [ord(char)-ord('A') for char in text]

def num_to_text(nums):
    return "".join([chr(num+ord('A')) for num in nums])



def encrypt(plainText):
    plainText = plainText.upper().replace(' ','')

    if(len(plainText)%2!=0):
        plainText+='X'

    
    cipherText = ""

    
    for i in range(0,len(plainText),2):
        block = np.array(text_to_num(plainText[i:i+2]))
        encryptedBlock = np.dot(keyMatrix,block)%26
        cipherText+=num_to_text(encryptedBlock)
    return cipherText



def decrypt(cipherText):
    cipherText = cipherText.upper().replace(' ','')
    plainText = ""

    for i in range(0,len(cipherText),2):
        block = np.array(text_to_num(cipherText[i:i+2]))
        decryptedBlock = np.dot(keyInverse,block)%26
        plainText+=num_to_text(decryptedBlock)
    return plainText


plainText = input("Enter a message :")
cipherText = encrypt(plainText)
print("Encrypted : ",cipherText)
print("Decrypted : ",decrypt(cipherText))


```


- **3. Perform encryption, decryption using the Playfair cipher substitution techniques**
```py



```


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
    print("Key ",i+1," = ",keys[i])
```

- **5.Implement encryption & decryption using RSA**
```py


def gcd(a,b):
    while b:
        a,b = b,a%b
    return a


def RSA(p,q,msg):
    n = p*q
    phi = (p-1)*(q-1)

    for i in range(2,phi):
        if(gcd(i,phi)==1):
            e = i
            break
        
    j = 0
    
    while True:
        if(j*e%phi) == 1:
            d = j
            break
        j+=1
        
    c = (msg**e)%n

    print("Encrypted message : ",c)

    d = (c**d)%n
    
    print("Decrypted message : ",d)


p = int(input("Enter the value of p :"))
q = int(input("Enter the value of q :"))
msg = int(input("Emter a message :"))

RSA(p,q,msg)
```