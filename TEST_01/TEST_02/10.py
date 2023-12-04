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
        if(j*e%phi)==1:
            d = j
            break
        
        j+=1
        
    
    c = (msg**e)%n

    print("Encrypted message : ",c)

    d = (c ** d)%n

    print("Decrypted message : ",d)



p = int(input("Enter p :"))
q = int(input("Enter q :"))
msg = int(input("Enter msg :"))


RSA(p,q,msg)

