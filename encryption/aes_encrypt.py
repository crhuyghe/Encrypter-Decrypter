from aes_library import *

def encrypt(data, key):
    initialKey = createMatrix([key[i:i+2].zfill(2) for i in range(0, len(key), 2)])
    data = createMatrix([data[i:i+2].zfill(2) for i in range(0, len(data), 2)])

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
    
    # TODO: Split data into 128-bit chunks

    return encrypt_block(data, roundKeys)

def decrypt(data, key):
    initialKey = createMatrix([key[i:i+2].zfill(2) for i in range(0, len(key), 2)])
    data = createMatrix([data[i:i+2].zfill(2) for i in range(0, len(data), 2)])

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
    
    # TODO: Split data into 128-bit chunks
    
    return decrypt_block(data, roundKeys)
        

