import math

q = int(input("Enter the prime number :"))
a = int(input("Enter the value of primitive root :"))


Xa = int(input("Enter a private key for A :"))
Xb = int(input("Enter a private key for B :"))

Ya = pow(a,Xa)%q
Yb = pow(a,Xb)%q

print("Public key of A : ",Ya)
print("Public key of B : ",Yb)

Ka = pow(Yb,Xa)%q
Kb = pow(Ya,Xb)%q

print("Shared key of A :",Ka)
print("Shared key of B :",Kb)


