result = ""
key = ""


s = input("Enter String: ")
for ch in s:
    result += format(ord(ch), "08b")

l = int(len(result)/2)


left = result[:l]
right = result[l:]

k = input("Enter key: ")


for ch in k:
    key += format(ord(ch), "08b")
    
print("Key: " + key)



s = bin(int(right, 2) + int(key, 2))
answer = bin(int(s[2:], 2) ^ int(left, 2))

newl = right
newr = answer[2:]

newl, newr = newr, newl

s = bin(int(newr, 2) + int(key, 2))
ans = bin(int(s[2:], 2) ^ int(newl, 2))

nl = newr
nr = ans[2:]
nl, nr = nr, nl

cipher = nl + nr

if len(cipher) != len(result):
    while len(cipher) != len(result):
        cipher = "0" + cipher


print("CipherText is: " + cipher)

plainText = ""


for i in range(0, len(cipher), 8):
    temp = cipher[i : i + 8]
    d = int(temp, 2)
    plainText = plainText+ chr(d)


print("Decrypted Text is: " + plainText)