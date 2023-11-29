# Implement encryption and decryption using RSA

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