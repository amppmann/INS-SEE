import math


q = int(input("Enter a prime number :"))
a = int(input("Enter a primitive root :"))


Xa = int(input("Enter a private key for A :"))
Xb = int(input("Enter a private key for B :"))


Ya = pow(a,Xa)%q
Yb = pow(a,Xb)%q

print("Public key of A : ",Ya)
print("Public key of B : ",Yb)


Ka = pow(Yb,Xa)%q
Kb = pow(Ya,Xb)%q

print("Shared key for A :",Ka)
print("Shared key for B :",Kb)