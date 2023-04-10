# Divide the data into fixed-size blocks (usually bytes or words).
# Add all the bytes/words together.
# Take the one's complement of the result.
# The one's complement is the checksum value.

def Checksum_gen(datawords, num_blocks):
    # Concatenate the datawords
    concatenated_datawords = ''.join(datawords)

    # Divide the concatenated datawords into blocks
    block_size = len(concatenated_datawords) // num_blocks
    blocks = [concatenated_datawords[i:i+block_size] for i in range(0, len(concatenated_datawords), block_size)]

    # Calculate the checksum
    checksum = ''
    for i in range(block_size):
        total = 0
        for block in blocks:
            total += int(block[i], 2)
        checksum += str(total % 2)

    # Combine the datawords and checksum to form the codeword
    codeword = concatenated_datawords + checksum
    return codeword

def Checksum_check(codeword, num_blocks):
    # Divide the codeword into dataword and checksum
    dataword_size = (len(codeword) - num_blocks) // (num_blocks + 1)
    datawords = [codeword[i:i+dataword_size] for i in range(0, len(codeword) - dataword_size, dataword_size)]
    received_checksum = codeword[-dataword_size:]

    # Calculate the checksum for the datawords
    checksum = [0] * dataword_size
    for i in range(dataword_size):
        for dataword in datawords:
            if len(dataword) <= i:
                continue
            checksum[i] ^= int(dataword[i])

    # Compare the calculated checksum to the received checksum
    if checksum == [int(x) for x in received_checksum]:
        return 0
    else:
        return -1


def main():
    # CHECKSUM GEN
    datawords = [
        ["10010110", "11111010", "10101011", "01011101", "01100110", "11110111", "01011001", "00111010"],
        ["01011101", "11010010", "01101011", "00101110", "11000101", "00010101", "10101100", "00111010"],
        ["11011110", "10101001", "11110111", "00110111", "01001011", "10111101", "10110011", "01001110"],
        ["11100011", "10111011", "00110010", "11010111", "01001010", "01100101", "11001110", "10111100"],
        ["00011100", "10001110", "11110110", "01101000", "11001101", "00100100", "00110011", "01011011"],
        ["11100111", "11011111", "10111001", "01110000", "10010111", "01001011", "10010110", "11010100"],
        ["00111010", "01101011", "01001110", "10110001", "11101001", "11011101", "10000111", "11101100"],
        ["10101101", "10011011", "10110100", "11010010", "01001011", "11100011", "11100100", "01110101"],
        ["00110010", "11101001", "10110011", "01100011", "01011100", "10111110", "00111001", "00010011"],
        ["11100110", "11011110", "10110000", "01010111", "00101110", "10010001", "10101111", "00110111"]
    ]
    
    for i in range(10):
        print("Case " + str(i) + ": ")
        codeword = Checksum_gen(datawords[i], 8)
        print("Input string:", ''.join(datawords[i]))
        print("Checksum:", codeword[-8:])
        print("Codeword:", codeword)
        print()
        
    print("\nValidity\n-----------------")
    codewords = ['100101101111101010101011010111010110011011110111010110010011101001101000',
                 '010111011101001001101011001011101100010100010101101011000011101010001100',
                 '110111101010100111110111001101110100101110111101101100110100111010111100',
                 '111000111011101100110010110101110100101001100101110011101011110011100000',
                 '000111001000111011110110011010001100110100100100001100110101101110001101',
                 '111001111101111110111001011100001001011101001011100101101101010001101111',
                 '001110100110101101001110101100011110100111011101100001111110110011110001',
                 '101011011001101110110100110100100100101111100011111001000111010101101001',
                 '001100101110100110110011011000110101110010111110001110010001001111000011',
                 '111001101101111010110000010101110010111010010001101011110011011111111000']
    
    for i in range(10):
        print('Test ' + str(i) + ": ")
        validity = Checksum_check(codewords[i], 16)
        if validity == 0:
            print('PASS');
        else:
            print('FAIL')

    
        
    

main()
