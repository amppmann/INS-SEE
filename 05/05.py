#Perform encryption,decryption using the vignere cipher (Polyalphabetic) substitution techniques.



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