# Based on secp128r2

class EllipticCurve:
    def __init__(self, p, a, b, g_x, g_y, order, cofactor):
        self.p = p
        self.a = a
        self.b = b
        self.g_x = g_x
        self.g_y = g_y
        self.order = order
        self.cofactor = cofactor

    def point_add(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        if P == Q:
            lam = (3 * P[0] * P[0] + self.a) * pow(2 * P[1], -1, self.p)
        else:
            lam = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, self.p)

        x = (lam * lam - P[0] - Q[0]) % self.p
        y = (lam * (P[0] - x) - P[1]) % self.p

        return (x, y)

    def point_double(self, P):
        return self.point_add(P, P)

    def scalar_multiply(self, k, P):
        result = None
        for bit in bin(k)[2:]:
            result = self.point_double(result)
            if bit == '1':
                result = self.point_add(result, P)
        return result

curve_params = {
    "p": 0xfffffffdffffffffffffffffffffffff,
    "a": 0xd6031998d1b3bbfebf59cc9bbff9aee1,
    "b": 0x5eeefca380d02919dc2c6558bb6d8a5d,
    "g_x": 0x7b6aa5d85e572983e6fb32a7cdebc140,
    "g_y": 0x27b6916a894d3aee7106fe805fc34b44,
    "order": 0x3fffffff7fffffffbe0024720613b5a3,
    "cofactor": 0x04,
}

curve = EllipticCurve(**curve_params)

def getKey(key, start):
    if start is None:
        return curve.scalar_multiply(key, (curve_params["g_x"], curve_params["g_y"]))
    else:
        return curve.scalar_multiply(key, start)
