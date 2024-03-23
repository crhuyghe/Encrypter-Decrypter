# Curve characteristics as detailed by SECG's secp128r2

p = 0xfffffffdffffffffffffffffffffffff
a = 0xd6031998d1b3bbfebf59cc9bbff9aee1
x = 0x7b6aa5d85e572983e6fb32a7cdebc140
y = 0x27b6916a894d3aee7106fe805fc34b44
G = (x, y)

def scalar_multiply(n, P):
    def mod_inverse(k):
        return pow(k, -1, p)

    def point_add(P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        x_p, y_p = P
        x_q, y_q = Q
  
        # Point double
        if P == Q:
            lam = (3 * x_p ** 2 + a) * mod_inverse(2 * y_p)
        # Point add
        else:
            lam = (y_q - y_p) * mod_inverse(x_q - x_p)

        x_r = lam ** 2 - x_p - x_q
        y_r = lam * (x_p - x_r) - y_p

        return (x_r % p, y_r % p)

    result = None

    # Double and add method
    for bit in bin(n)[2:]:
        result = point_add(result, result)
        if bit == '1':
            result = point_add(result, P)

    return result

def generatePublicKey(private):
    return scalar_multiply(private, G)

def generateSharedSecret(private, public):
    return scalar_multiply(private, public)
