AES_S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

AES_MIX_COLUMN_MATRIX = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

AES_INVERSE_MIX_COLUMN_MATRIX = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
]

ROUND_CONSTANTS = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36, 00]

# Turn string of hex into 4x4 grid
def createMatrix(list):
    # Initialize a 4x4 list
    matrix = [[0] * 4 for _ in range(4)]
    # Insert elements column-wise
    for i in range(4):
        for j in range(4):
            matrix[j][i] = list[i * 4 + j]
    return matrix

# Turn 4x4 back into string of hex
def deconstructMatrix(matrix):
    string = ""
    for i in range(4):
        for j in range(4):
            string += str(matrix[j][i])
    return string
    
# Use s_box to substitute bytes
def subBytes(state):

    def subOneByte(byte):
        row, column = byte
        row, column = int(row, 16), int(column, 16)
        return hex(AES_S_BOX[row * 16 + column])[2:].zfill(2)
    
    resultState = []
    for row in range(0, len(state)):
        for col in range(0, len(state)):
            resultState.append(subOneByte(state[row][col]))
    state = createMatrix(resultState)
    return state

# Use s_box to reverse substitutions
def unsubBytes(state):

    def unsubOneByte(s_box_value):
        index = AES_S_BOX.index(int(s_box_value, 16))
        row = hex(index // 16)[2:]
        column = hex(index % 16)[2:]
        return row + column
    
    resultState = []
    for row in range(0, len(state)):
        for col in range(0, len(state)):
            resultState.append(unsubOneByte(state[row][col]))
    state = createMatrix(resultState)
    return state
        
def shiftRows(state):
    # Leave row 1
    # Shift row 2 1 space
    state[1].append(state[1].pop(0))

    # Shift row 3 2 spaces
    state[2].append(state[2].pop(0))
    state[2].append(state[2].pop(0))

    # Shift row 4 3 spaces
    state[3].insert(0, state[3].pop(3))
    return state

def unShiftRows(state):
    # Leave row 1
    # Shift row 4 1 space
    state[3].append(state[3].pop(0))

    # Shift row 3 2 spaces
    state[2].append(state[2].pop(0))
    state[2].append(state[2].pop(0))

    # Shift row 2 3 spaces
    state[1].insert(0, state[1].pop(3))
    return state

def gfMultiply(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b
        b >>= 1
    return result & 0xFF

def mixColumns(state):
    resultState = [row[:] for row in state]

    for col in range(4):  # Assuming 4 columns in the state matrix
        # Iterate through each row of the MixColumns matrix
        for row in range(4):
            # Initialize the result for the current cell
            result = 0

            # Multiply and accumulate the values from the current column and MixColumns matrix
            for i in range(4):
                result ^= gfMultiply(AES_MIX_COLUMN_MATRIX[row][i], int(state[i][col], 16))

            resultState[row][col] = result

    return [[hex(num)[2:].zfill(2) for num in row] for row in resultState]

def unmixColumns(state):
    resultState = [row[:] for row in state]

    for col in range(4):  # Assuming 4 columns in the state matrix
        # Iterate through each row of the inverse MixColumns matrix
        for row in range(4):
            # Initialize the result for the current cell
            result = 0

            # Multiply and accumulate the values from the current column and inverse MixColumns matrix
            for i in range(4):
                result ^= gfMultiply(AES_INVERSE_MIX_COLUMN_MATRIX[row][i], int(state[i][col], 16))

            resultState[row][col] = result

    return [[hex(num)[2:].zfill(2) for num in row] for row in resultState]

# Bitwise xor each element in state with each element in key
def addRoundKey(state, key):
    def xor(x, y):
        return hex(int(x, 16) ^ int(y, 16))[2:].zfill(2)

    return list(map(lambda x, y: list(map(xor, x, y)), state, key))

# Generate next round based on previous key
def expandKey(key, round):
    def subBlock(byte):
        row, column = byte
        return AES_S_BOX[int(row, 16) * 16 + int(column, 16)]
    
    # g function for first column
    def g(key):
        def subFirst(word):
            a, b, c, d = word
            return [hex(subBlock(a) ^ ROUND_CONSTANTS[round])[2:].zfill(2), b, c, d]
        a, b, c, d = key
        return [subFirst(b), subFirst(c), subFirst(d), subFirst(a)]
    
    # Folds right bitwise xor to generate columns 2, 3, and 4
    def rowxor(row):
        def xor(x, y):
            return hex(int(x, 16) ^ int(y, 16))[2:].zfill(2)
        a, b, c, d = row
        b = xor(b, a)
        c = xor(c, b)
        d = xor(d, c)
        return [a, b, c, d]   

    a, b, c, d = g(key)
    return [rowxor(a), rowxor(b), rowxor(c), rowxor(d)]
