def Hamming_gen(dataword):
    # Determine the number of parity bits needed for the dataword
    r = 0
    while 2**r < len(dataword) + r + 1:
        r += 1

    # Print the position(s) of the redundancy bit(s)
    print("Redundancy bit(s) at position(s): ", end="")
    for i in range(r):
        print(str(2**i) + " ", end="")
    print()

    # Initialize the codeword with zeros
    codeword = [0] * (len(dataword) + r)

    # Copy the data bits to the codeword, skipping the parity bit positions
    j = 0
    for i in range(len(codeword)):
        if i+1 not in [2**k for k in range(r)]:
            codeword[i] = int(dataword[j])
            j += 1

    # Calculate the parity bits
    for i in range(r):
        # Determine the indices of the data bits that this parity bit checks
        indices = [j for j in range(len(codeword)) if ((j+1) & (2**i))]

        # Calculate the parity bit value
        parity_bit = 0
        for index in indices:
            parity_bit ^= codeword[index]

        # Update the codeword with the parity bit
        codeword[2**i - 1] = parity_bit
    
    return ''.join([str(bit) for bit in codeword])

def err_pos(codeword):
    # Determine the number of parity bits in the codeword
    r = 0
    while 2**r < len(codeword):
        r += 1
    
    # Initialize the error position to 0
    error_pos = 0
    
    # Check each parity bit
    for i in range(r):
        # Determine the indices of the data bits that this parity bit checks
        indices = [j for j in range(len(codeword)) if ((j+1) & (2**i))]

        # Calculate the parity bit value
        parity_bit = 0
        for index in indices:
            parity_bit ^= int(codeword[index])

        # If the parity bit is incorrect, set the error position
        if parity_bit != int(codeword[2**i - 1]):
            error_pos += 2**i - 1
    
    return error_pos



def main():
    datawords = ['1101',
                 '1010101',
                 '11010101101',
                 '11100101101011',
                 '10101010101010101010101',
                 '11100111110001111000',
                 '1010101010101010101010101',
                 '1010010110100110101011001',
                 '1110001110010100111010011',
                 '1001011010110101011110101010101',
                 '110110111011101100111101110110011101']
    
    for i in range(11):
        codeword = Hamming_gen(datawords[i])
        print("Case " + str(i) + ": ")
        print("Dataword: " + datawords[i])
        print("Codeword: " + codeword)
        print('--------------')
        
    codeWords = ['10100101100', '1100101011', '11110001110', '1101100110101', '10101111010010', '1001110101101', '101111010100110', '1111010101111000', '11100110010001101', '101010101010101001']
    for i in range(10):
        print('TEST ' + str(i) + ": ")
        print('Codeword: ' + codeWords[i])
        err = err_pos(codeWords[i])
        if err <= 0:
            print('No Error')
        else:
            print("Error at bit #"+str(err))
        print('------')


main()