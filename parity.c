#include <stdio.h>

#define WORD_SIZE 8
#define ROWS 8 
#define COLUMNS 8

char** parity_gen(char* dataword, char* parity_type, int arr_size){
    char* codeWord[WORD_SIZE];
    for (int i = 0; i < WORD_SIZE; i++ ){
             codeWord[i] = (char *)malloc(sizeof(char) * WORD_SIZE);
    };
    if(parity_type[0] == '1'){
        //1D even        
    for(int i = 0 ; i < WORD_SIZE; i++){
            codeWord[i] = dataword[i];
        }
    }
    else if(parity_type[0] == '2'){
        //1D odd

    }
    else if (parity_type[0] == '3')
    { //2D Even

    }
    else if (parity_type[0] == '4')
    { //2D odd

    }
    return codeWord;
}

int main(int argc, char const *argv[])
{
    char dataword[WORD_SIZE][WORD_SIZE] = {
        "10100",
        "010000",
        "1110",
        "00",
        "10010010",
        "11011011",
        "11001",
        "0101000"
    };

    char parity_type[4] = "1234"; // Type of parity (one-dimensional-even, one-dimensional-odd, two-dimensional-even, two-dimensional-odd)

    char** codeWord = parity_gen(dataword, parity_type[0], WORD_SIZE);

    return 0;
}
