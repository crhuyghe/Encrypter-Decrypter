from aes_library import *

def encrypt(data, key):
    def padHex(data):
        nibbles = len(data)
        remainder = nibbles % 32
        toFit = nibbles + (32 - remainder)
        return data.zfill(toFit)

    data = padHex(data)
    initialKey = createMatrix([key[i:i+2].zfill(2) for i in range(0, len(key), 2)])

    roundKeys = [initialKey]
    for round_number in range(0, 10):
        roundKeys.append(expandKey(roundKeys[-1], round_number))

    def encrypt_block(data, roundKeys):
        # Round 0 setup
        data = addRoundKey(data, roundKeys[0])

        # Rounds 1-10 encryption
        for round in range(1, 11):
            data = subBytes(data)
            data = shiftRows(data)
            if round < 10:
                data = mixColumns(data)
            data = addRoundKey(data, roundKeys[round])

        # Returns 1D hex string
        return deconstructMatrix(data)
    
    encryptedMessage = ""

    for i in range(0, len(data), 32):
        block = data[i:i+32]
        block = createMatrix([block[i:i+2].zfill(2) for i in range(0, len(block), 2)])
        encryptedMessage += encrypt_block(block, roundKeys)

    return encryptedMessage

def decrypt(data, key):
    initialKey = createMatrix([key[i:i+2].zfill(2) for i in range(0, len(key), 2)])

    roundKeys = [initialKey]
    for round_number in range(0, 10):
        roundKeys.append(expandKey(roundKeys[-1], round_number))

    def decrypt_block(data, roundKeys):
        #Rounds 10-1 decryption
        for round in range(10, 0, -1):
            data = addRoundKey(data, roundKeys[round])
            if round < 10:
                data = unmixColumns(data)
            data = unShiftRows(data)
            data = unsubBytes(data)

        # Undo round 0 setup
        data = addRoundKey(data, roundKeys[0])
        
        # Returns 1D hex string
        return deconstructMatrix(data)
    
    decryptedMessage = ""

    for i in range(0, len(data), 32):
        block = data[i:i+32]
        block = createMatrix([block[i:i+2].zfill(2) for i in range(0, len(block), 2)])
        decryptedMessage += decrypt_block(block, roundKeys)
    
    return decryptedMessage.lstrip('0')
