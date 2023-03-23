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
    
    elif parity_type == '3':
        for i in range(array_size):
            count = 0
            while True:
                if len(codeWord[i]) != 8:
                    codeWord[i] += '0'
                else:
                    break
            
            for j in range(len(codeWord[i])):
                if codeWord[i][j] == '1':
                    count += 1
            if count % 2 == 0: #Even parity
                codeWord[i] += '0' 
            else:
                codeWord[i] += '1'
    
    else:
        for i in range(array_size):
            count = 0
            while True:
                if len(codeWord[i]) != 8:
                    codeWord[i] += '0'
                else:
                    break
            
            for j in range(len(codeWord[i])):
                if codeWord[i][j] == '1':
                    count += 1
            if count % 2 == 0: #Even parity
                codeWord[i] += '1' 
            else:
                codeWord[i] += '0'
            
    return codeWord

def main():
    datawords = [
        "10100",
        "010000",
        "1110",
        "00",
        "10010010",
        "11011011",
        "11001",
        "0101000"
    ]
    
    print(datawords)
    print(parity_gen(datawords, '1', len(datawords)))
    print(parity_gen(datawords, '2', len(datawords)))
    print(parity_gen(datawords, '3', len(datawords)))
    print(parity_gen(datawords, '4', len(datawords)))

main()
