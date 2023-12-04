def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result+=chr((ord(char)+s-65)%26+65)
        elif char.islower():
            result+=chr((ord(char)+s-97)%26+97)
        
        else:
            result+=""
            
    return result

def decrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result+=chr((ord(char)-s-65)%26+65)
        elif char.islower():
            result+=chr((ord(char)-s-97)%26+97)
    
        else:
            result+=""

    return result

while True:
    print("1.Encrypt\n2.Decrypt\n3.Exit\n")
    ch = int(input("Enter your choice (1-3):"))
     
    if ch ==1:
        text = input("Enter a text :")
        key = int(input("Enter a key :"))
        print("Encrypting...")
        cipher = encrypt(text,key)
        print("Cipher text : ",cipher)

    elif ch == 2:
        text = input("Enter a text :")
        key = int(input("Enter a key :"))
        print("Decrypting...")
        plain = decrypt(text,key)
        print("Plain text : ",plain)

    elif ch == 3:
        break
    else:
        print("Invalid choice...")
        