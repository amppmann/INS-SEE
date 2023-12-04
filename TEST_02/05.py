def vigenere(message,key):
    message = message.lower()
    message = message.replace(' ','')
    cipherText = ""
    m = len(key)

    for i in range(len(message)):
        letter = message[i]
        k = key[i%m]

        cipherText+=chr((ord(letter)+k-97)%26+97)
    return cipherText


if __name__ == "__main__":
    key = input("Enter a keystream :")
    key = [ord(letter)-97 for letter in key]

    message = input("Enter a message :")

    cipher = vigenere(message,key)
    print("Encrypted message : ",cipher)

    key = [-1*k for k in key]
    plain = vigenere(cipher,key)
    print("Decrypted message :",plain)


