# Curve characteristics as detailed by SECG's secp128r2

p = 0xfffffffdffffffffffffffffffffffff
a = 0xd6031998d1b3bbfebf59cc9bbff9aee1
G = (0x7b6aa5d85e572983e6fb32a7cdebc140, 0x27b6916a894d3aee7106fe805fc34b44)

def scalarMultiply(k, P):
    def pointAdd(P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        if P == Q:
            lam = (3 * P[0] * P[0] + a) * pow(2 * P[1], -1, p)
        else:
            lam = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p)

        x = (lam * lam - P[0] - Q[0]) % p
        y = (lam * (P[0] - x) - P[1]) % p

        return (x, y)

    result = None
    for bit in bin(k)[2:]:
        result = pointAdd(result, result)
        if bit == '1':
            result = pointAdd(result, P)
    return result

def generatePublicKey(private):
    return scalarMultiply(private, G)

def generateSharedSecret(private, coordinates):
    return scalarMultiply(private, coordinates)
