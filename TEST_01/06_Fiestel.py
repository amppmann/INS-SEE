s = input("Enter a string :")

result = "".join(format(ord(i),'08b') for i in s)

print("Result : ",result )

l = int(len(result)/2)
left = result[:l]
right = result[l:]

k = input("Enter a key : ")
key = "".join(format(ord(i),'08b') for i in k)

s = bin(int(right,2)+int(key,2))
answer = bin(int(s[2:],2)^int(left,2))

newr = answer[2:]
newl =right

newl,newr = newr,newl

s = bin(int(newr,2)+int(key,2))
newAns = bin(int(s[2:],2)^int(newl,2))

nl = newr
nr = newAns[2:]

nl,nr = nr,nl

cipher = nl+nr

if(len(cipher)!=len(result)):
    while(len(cipher)!=len(result)):
        cipher = "0"+cipher

print(cipher)

plainText = ""

for i in range(0,len(cipher),8):
    temp = cipher[i:i+8]
    d = int(temp,2)
    plainText = plainText+chr(d)
    
    
print(plainText)

