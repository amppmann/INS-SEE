key = input("Enter a key :")
key = key.upper()


keysAlready = []
mapper = {}

matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


# Key matrix creation


i = 0
j = 0

for ch in key:
    if(ch not in keysAlready):
        matrix[i][j] = ch
        mapper[ch] = (i,j)
        keysAlready.append(ch)
        j = (j+1)%5
        if(j == 0):
            i+=1


for ascii in range(65,91):
    ch = chr(ascii)
    if(ch not in keysAlready and ch!='J'):
        matrix[i][j] = ch
        mapper[ch] = (i,j)
        keysAlready.append(ch)
        j = (j+1)%5
        if(j == 0):
            i+=1
print("Matrix : ",matrix)


# Plaintext modification

plainText = input("Enter a plaintext :")
plainText = plainText.upper()

for i in range(0,len(plainText)-1,2):
    if(plainText[i] == plainText[i+1]):
        plainText=plainText[:i+1]+"X"+plainText[i+1:]

if(len(plainText)%2!=0):
    plainText+="X"

print("Plaintext : ",plainText)



#Encryption

cipherText = ""
for i in range(0,len(plainText)-1,2):
    char1 = plainText[i]
    char2 = plainText[i+1]

    (row1,col1) = mapper[char1]
    (row2,col2) = mapper[char2]


    if(row1 == row2):
        row = row1 = row2
        cipherText+=matrix[row][(col1+1)%5]
        cipherText+=matrix[row][(col2+1)%5]

    elif(col1 == col2):
        col = col1 = col2
        cipherText+=matrix[(row1+1)%5][col]
        cipherText+=matrix[(row2+1)%5][col]
    else:
        cipherText+=matrix[row1][col2]
        cipherText+=matrix[row2][col1]

print("Ciphertext : ",cipherText)

plainText = ""


for i in range(0,len(cipherText)-1,2):
    char1 = cipherText[i]
    char2 = cipherText[i+1]

    (row1,col1) = mapper[char1]
    (row2,col2) = mapper[char2]

    if(row1 == row2):
        row = row1 = row2
        plainText+=matrix[row][(col1-1)%5]
        plainText+=matrix[row][(col2-1)%5]
    elif(col1 == col2):
        col = col1 = col2
        plainText+=matrix[(row1-1)%5][col]
        plainText+=matrix[(row2-1)%5][col]

    else:
        plainText+=matrix[row1][col2]
        plainText+=matrix[row2][col1]


print("Plaintext : ",plainText)


    






    
