

def vigenere(key,message):
    message = message.lower()
    message = message.replace(' ','')

    m = len(key)
    cipherText = ""

    for i in range(len(message)):
        letter = message[i]
        k = key[i%m]

        cipherText+=chr((ord(letter)-97+k)%26+97)
    return cipherText


if __name__ == "__main__":
    
    key = input("Enter a keystream :")
    key = [ord(letter)-97 for letter in key]

    
    message = input("Enter a message :")

    cipher = vigenere(key,message)
    print("Encrypting...")

    print("Encrypted message : ",cipher)

    print("\n")
    print("Decrypting...")

    key = [-1*k for k in key]

    plain = vigenere(key,cipher)

    print("Decrypted message : ",plain)
    