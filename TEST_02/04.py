import tinyec
from tinyec import registry
import secrets



curve  = registry.get_curve('brainpoolP256r1')

def compress_point(point):
    return hex(point.x)+hex(point.y % 2)[2:]

def getEnKey(publicKey):
    