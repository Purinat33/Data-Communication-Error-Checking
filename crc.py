import os
import random
# For CRC-32
CRC32_POLY = 0xEDB88320
CRC32_TABLE = [((CRC32_POLY >> (8*i)) & 0xFF) for i in range(4)]

# For CRC-16
CRC16_POLY = 0x8005
CRC16_TABLE = [((CRC16_POLY >> (8*i)) & 0xFF) for i in range(2)]

# For CRC-8
CRC8_POLY = 0x07
CRC8_TABLE = [((CRC8_POLY >> i) & 0x01) for i in range(8)]

def CRC_gen(dataword, crcType):
    crcTable = None
    crcSize = 0
    if crcType == "CRC-8":
        crcTable = CRC8_TABLE
        crcSize = 1
    elif crcType == "CRC-16":
        crcTable = CRC16_TABLE
        crcSize = 2
    elif crcType == "CRC-32":
        crcTable = CRC32_TABLE
        crcSize = 4
    else:
        raise ValueError("Unsupported CRC type: " + crcType)

    crc = 0
    for b in dataword:
        crc ^= b
        for i in range(8):
            if (crc & 0x80) != 0:
                crc = (crc << 1) ^ crcTable[crcSize - 1]
            else:
                crc <<= 1

    codeword = bytearray(dataword) + bytearray(crcSize)
    for i in range(crcSize):
        codeword[dataword.__len__() + i] = (crc >> (8 * (crcSize - i - 1))) & 0xFF

    return bytes(codeword)

def CRC_check(codeword, crcType):
    
    crcTable = None
    crcSize = 0
    if crcType == "CRC-8":
        crcTable = CRC8_TABLE
        crcSize = 1
    elif crcType == "CRC-16":
        crcTable = CRC16_TABLE
        crcSize = 2
    elif crcType == "CRC-32":
        crcTable = CRC32_TABLE
        crcSize = 4
    else:
        raise ValueError("Unsupported CRC type: " + crcType)

    crc = 0
    for i in range(len(codeword) - crcSize):
        crc ^= codeword[i]
        for j in range(8):
            if (crc & 0x80) != 0:
                crc = (crc << 1) ^ crcTable[crcSize - 1]
            else:
                crc <<= 1

    for i in range(crcSize):
        if codeword[len(codeword) - crcSize + i] != (crc >> (8 * (crcSize - i - 1))) & 0xFF:
            return -1 # FAIL

    return 0 # PASS

def failTest():
    print('--------')
    print('Fail example: ')
    data = [255, 255, 0]
    print(f'Dataword: ', list(data))
    code = CRC_gen(data, "CRC-16")
    print(f'Codeword: ', list(code))
    
    validity = CRC_check(code, "CRC-16")
    
    print('Validity: ', "PASS" if validity == 0 else "FAIL")
    wrong = [255,255,0,0,1]
    print('Passing a wrong Codeword: ', list(wrong))
    validity = CRC_check(wrong, "CRC-16")
    print('Validity: ', "PASS" if validity == 0 else "FAIL")

    


def main():

    # Test CRC-8
    print("Testing CRC-8...")
    for i in range(10):
        dataword = bytearray(os.urandom(random.randint(1, 8)))
        crcType = "CRC-8"

        codeword = CRC_gen(dataword, crcType)
        validity = CRC_check(codeword, crcType)

        print("Dataword: ", list(dataword))
        print("Codeword: ", list(codeword))
        print("Validity: ", "PASS" if validity == 0 else "FAIL")

    # Test CRC-16
    print("\nTesting CRC-16...")
    for i in range(10):
        dataword = bytearray(os.urandom(random.randint(1, 8)))
        crcType = "CRC-16"

        codeword = CRC_gen(dataword, crcType)
        validity = CRC_check(codeword, crcType)

        print("Dataword: ", list(dataword))
        print("Codeword: ", list(codeword))
        print("Validity: ", "PASS" if validity == 0 else "FAIL")

    # Test CRC-32
    print("\nTesting CRC-32...")
    for i in range(10):
        dataword = bytearray(os.urandom(random.randint(1, 8)))
        crcType = "CRC-32"

        codeword = CRC_gen(dataword, crcType)
        validity = CRC_check(codeword, crcType)

        print("Dataword: ", list(dataword))
        print("Codeword: ", list(codeword))
        print("Validity: ", "PASS" if validity == 0 else "FAIL")
    
    failTest();

main()
