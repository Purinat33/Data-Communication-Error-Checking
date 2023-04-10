def parity_gen(dataword, parity_type, array_size):
    
    codeWord = list.copy(dataword)
    
    if parity_type == '1':
        for i in range(array_size):
            count = 0
            for j in range(len(codeWord[i])):
                if codeWord[i][j] == '1':
                    count += 1
            if count % 2 == 0: #Even parity
                codeWord[i] += '0' 
            else:
                codeWord[i] += '1'
                
    elif parity_type == '2':
        for i in range(array_size):
            count = 0
            for j in range(len(codeWord[i])):
                if codeWord[i][j] == '1':
                    count += 1
            if count % 2 == 0: #Even parity
                codeWord[i] += '1' 
            else:
                codeWord[i] += '0'
    
    elif parity_type == '3': #2D Even
        
        for i in range(array_size):
            while True:
                if len(codeWord[i]) != 8:
                    codeWord[i] += '0'
                else:
                    break
        
        for i in range(array_size):
            row_count = 0
            col_count = [0] * len(codeWord[i])
            for j in range(len(codeWord[i])):
                if codeWord[i][j] == '1':
                    row_count += 1
                    col_count[j] += 1
            for j in range(len(col_count)):
                if col_count[j] % 2 == 0: #Even parity
                    codeWord[i] += '0' 
                else:
                    codeWord[i] += '1'
            if row_count % 2 == 0: #Even parity
                codeWord[i] += '1' # 2D even parity
            else:
                codeWord[i] += '0' # 2D odd parity
    
    else: #2D Odd
        for i in range(array_size):
            while True:
                if len(codeWord[i]) != 8:
                    codeWord[i] += '0'
                else:
                    break
                
        for i in range(array_size):
            row_count = 0
            col_count = [0] * len(codeWord[i])
            for j in range(len(codeWord[i])):
                if codeWord[i][j] == '1':
                    row_count += 1
                    col_count[j] += 1
            for j in range(len(col_count)):
                if col_count[j] % 2 == 0: #Even parity
                    codeWord[i] += '1' 
                else:
                    codeWord[i] += '0'
            if row_count % 2 == 0: #Even parity
                codeWord[i] += '0' # 2D odd parity
            else:
                codeWord[i] += '1' # 2D even parity
            
    return codeWord



def parity_check(codeword, parity_type, array_size):
    result = []
    
    if parity_type == '1': # 1D-Even parity
        for i in range(array_size):
            count = 0
            for j in range(len(codeword[i])):
                if codeword[i][j] == '1':
                    count += 1
            if count % 2 == 0: # Even parity
                result.append(True)
            else:
                result.append(False)
    
    elif parity_type == '2': # 1D-Odd parity
        for i in range(array_size):
            count = 0
            for j in range(len(codeword[i])):
                if codeword[i][j] == '1':
                    count += 1
            if count % 2 == 0: # Even parity
                result.append(False)
            else:
                result.append(True)
    
    elif parity_type == '3': # 2D-Even parity
        row_parity = [sum([int(bit) for bit in row]) % 2 == 0 for row in codeword]
        col_parity = [sum([int(codeword[row][col]) for row in range(array_size)]) % 2 == 0 for col in range(len(codeword[0]))]
        overall_parity = sum(row_parity) + sum(col_parity) == len(row_parity) + len(col_parity)
        result = [overall_parity] + row_parity + col_parity
    
    else: # 2D-Odd parity
        row_parity = [sum([int(bit) for bit in row]) % 2 == 1 for row in codeword]
        col_parity = [sum([int(codeword[row][col]) for row in range(array_size)]) % 2 == 1 for col in range(len(codeword[0]))]
        overall_parity = sum(row_parity) + sum(col_parity) == len(row_parity) + len(col_parity)
        result = [overall_parity] + row_parity + col_parity
            
    return result

def write2D(data):
    for i in range(len(data)):
            print('\n')
            for j in range(len(data[i])):
                print(data[i][j], end=' ')
    
    print('\n')
     
        
def main():
    datawords = [
        "10100",
        "010000",
        "1110",
        "00",
        "10010010",
        "11011011",
        "11001",
        "0101000",
        "00010",
        "10000",
        "0111111",
        "1",
        "010"
    ]
    
    print("Parity_Gen:")
    print("Original: ",datawords)
    print("------------------------")
    print("1D-Even: ",parity_gen(datawords, '1', len(datawords)))
    print("------------------------")
    print("1-D Odd: ",parity_gen(datawords, '2', len(datawords)))
    print("------------------------")
    print("2D Even:")
    write2D(parity_gen(datawords, '3', len(datawords)));
    print("2D Odd:")
    write2D(parity_gen(datawords, '4', len(datawords)));
    print("------------------------")
    
    parityCheck = [
        '101011001',
        '000010110',
        '111111111',
        '010100001',
        '011100011',
        '000101011',
        '111010111',
        '101100111',
        '000000011',
        '000100000'
    ]
    
    print("\nParity_Check")
    print("Original: ",parityCheck)
    print("------------------------")
    print('1D Even: ', parity_check(parityCheck, '1', len(parityCheck)))
    print("------------------------")           
    print('1D Odd: ', parity_check(parityCheck, '2', len(parityCheck)))
    print("------------------------")
    print('2D Even: ')
    print(parity_check(parityCheck, '3', len(parityCheck)))
    print("------------------------")
    print('2D Odd: ')
    print(parity_check(parityCheck, '4', len(parityCheck)))
    
main()
