import math

def gcd(a,b):
    temp = 0 
    
    while(b!=0):
        temp = a % b
        if(temp == 0):
            return b
        a = b 
        b = temp
        

p = int(input("Enter the value of p :"))
q = int(input("Enter the value of q :"))
e = int(input("Enter the value of e :"))

n= p*q
phi = (p-1)*(q-1)

while(e<phi):
    if(gcd(e,phi)==1):
        break
    else:
        e+=1
        
        
k = int(input("Enter the key value :"))

d = (1+(k*phi))/e

msg = float(input("Enter the message :"))

print("Message sent : ",msg)
print("Encryting...")

c = pow(msg,e)
c = math.fmod(c,n)

print("Encrypted message : ",c)

print("Decrypting...")

m = pow(c,d)
m = math.fmod(m,n)
print("Original message sent : ",m)




