from sage.all import EllipticCurve, GF

# Curve characteristics as detailed by SECG's secp128r2

p = 0xfffffffdffffffffffffffffffffffff
K = GF(p)
a = K(0xd6031998d1b3bbfebf59cc9bbff9aee1)
b = K(0x5eeefca380d02919dc2c6558bb6d8a5d)
E = EllipticCurve(K, (a, b))
G = E(0x7b6aa5d85e572983e6fb32a7cdebc140, 0x27b6916a894d3aee7106fe805fc34b44)
E.set_order(0x3fffffff7fffffffbe0024720613b5a3 * 0x04)

def generatePublic(private):
    return private * G

def generateShared(private, public):
    return private * public
