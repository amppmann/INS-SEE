import tinyec
from tinyec import registry

import secrets


curve = registry.get_curve("brainpoolP256r1")


def compress_point(point):
    return hex(point.x)+hex(point.y % 2)[2:]


def getEnKey(publicKey):
    ciPrivateKey = secrets.randbelow(curve.field.n)
    ciPublicKey = ciPrivateKey * curve.g
    enKey = ciPublicKey * ciPrivateKey
    
    return (enKey,ciPublicKey)


senderPrivateKey = secrets.randbelow(curve.field.n)
senderPublicKey = senderPrivateKey * curve.g

print("Sender's private key : ",hex(senderPrivateKey))
print("Sender's public key : ",compress_point(senderPublicKey))

print("\n")


(senderEncryptionKey,ciPublicKeyOfSender) = getEnKey(senderPublicKey)

print("Sender's Encryption key : ",compress_point(senderEncryptionKey))
print("Sender's Ciphertext public key : ",compress_point(ciPublicKeyOfSender))

print("\n")


print("Receiver side---")

receiverPrivateKey = secrets.randbelow(curve.field.n)
receiverPublicKey = receiverPrivateKey * curve.g

print("Sender's private key : ",hex(receiverPrivateKey))
print("Sender's public key : ",compress_point(receiverPublicKey))

print("\n")


(receiverEncryptionKey,ciPublicKeyOfReceiver) = getEnKey(receiverPublicKey)

print("Sender's Encryption key : ",compress_point(receiverEncryptionKey))
print("Sender's Ciphertext public key : ",(compress_point(ciPublicKeyOfReceiver)))

print("\n")
