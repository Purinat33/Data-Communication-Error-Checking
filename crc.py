#In this function, the inputs dividend and divisor are binary strings. The function converts them to integers using the int() function with a base of 2 (indicating binary). The division is then performed using the // (floor division) and % (modulus) operators. Finally, the outputs are converted back to binary strings using the bin() function with a slice ([2:]) to remove the "0b" prefix, and padded with zeros using the zfill() method.
def binary_division(dividend, divisor):
    """Performs binary division and returns both quotient and remainder"""
    dividend_str = bin(dividend)[2:]
    divisor_str = bin(divisor)[2:]
    divisor_len = len(divisor_str)
    dividend_len = len(dividend_str)
    quotient = ''
    temp = dividend_str[0 : divisor_len - 1]
    for i in range(divisor_len - 1, dividend_len):
        if len(temp) > 0 and temp[0] == "1":
            temp = int(temp, 2) ^ int(divisor_str, 2)
            temp = bin(temp)[2:]
            temp = temp.zfill(divisor_len - 1)
            quotient += '1'
        else:
            quotient += '0'
            temp = temp[1:]
        if i != dividend_len - 1:
            temp += dividend_str[i + 1]
    remainder = int(temp, 2)
    quotient = '0b' + quotient
    return (quotient[2:], remainder)


def crc_gen(dataword:str, crc_type:str):

    temp = dataword    
    
    temp = dataword    
    
    if crc_type == "CRC-8":
        #   x^8 +   x^7 +   x^6 +   x^4 +   x^2 +   1
        #   1       1       10      10      10      1
        crc8 = "111010101"
        for i in range(len(crc8) - 1):
            temp += '0' #Appending for the divisions
    
        crc = binary_division(int(dataword, 2), int(crc8, 2))[1]
        crc_bin = bin(crc)[2:].zfill(8)
        print("CRC-8:", crc_bin)        
    elif crc_type == "CRC-16":
        return 1
    else:
        return 2
    
def main():
    datawords = [
        "11000111",
        "01011010",
        "00000011",
        "11010001",
        "10001001",
        "00010100",
        "10001011",
        "10010011",
        "00100000",
        "11111110"
    ]
    
    for i in range(len(datawords)):
        print(crc_gen(datawords[i], "CRC-8"))
    
main()
