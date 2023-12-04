import tinyec
from tinyec import registry
import secrets



curve  = registry.get_curve('brainpoolP256r1')

def compress_point(point):
    return hex(point.x)+hex(point.y % 2)[2:]

def getEnKey(publicKey):
    ciPrivateKey = secrets.randbelow(curve.field.n)
    ciPublicKey = ciPrivateKey * curve.g
    enKey = ciPrivateKey * publicKey
    return (enKey,ciPublicKey)


senderPrivateKey = secrets.randbelow(curve.field.n)
senderPublicKey = senderPrivateKey *curve.g

print("Sender's private key : ",hex(senderPrivateKey))
print("Sender's public key : ",compress_point(senderPublicKey))

print("\n")


(senderEncryptionKey,ciPublicKeyOfSender) = getEnKey(senderPublicKey)

print("Sender's encryption key : ",compress_point(senderEncryptionKey))
print("Sender's ciphertext public key : ",compress_point(ciPublicKeyOfSender))
print("\n")



receiverPrivateKey = secrets.randbelow(curve.field.n)
receiverPublicKey = receiverPrivateKey * curve.g

print("Receiver's private key : ",hex(receiverPrivateKey))
print("Receiver's public key : ",compress_point(receiverPublicKey))

print("\n")

(receiverEncryptionKey,ciPublicKeyOfReceiver) = getEnKey(receiverPublicKey)

print("Receiver's encryption key : ",compress_point(receiverEncryptionKey))
print("Receiver's ciphertext public key : ",compress_point(ciPublicKeyOfReceiver))

print("\n")



