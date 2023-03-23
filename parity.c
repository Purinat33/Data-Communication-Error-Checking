#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WORD_SIZE 9 // To account for adding parity bit later
#define ROWS 8
#define COLUMNS 8

char **parity_gen(char dataword[][WORD_SIZE], char *parity_type, int arr_size)
{
    char **codeWord = malloc(arr_size * sizeof(char *));
    for (int i = 0; i < arr_size; i++)
    {
        codeWord[i] = malloc((WORD_SIZE + 1) * sizeof(char));
    }

    if (parity_type[0] == '1')
    {
        // 1D even
        for (int i = 0; i < arr_size; i++)
        {
            // copy dataword to codeword
            strncpy(codeWord[i], dataword[i], WORD_SIZE);
            codeWord[i][WORD_SIZE] = '\0'; // add null terminator
            // calculate parity bit
            int count = 0;
            for (int j = 0; j < WORD_SIZE - 1; j++)
            {
                if (codeWord[i][j] == '1')
                {
                    count++;
                }
            }
            if (count % 2 == 0)
            {
                codeWord[i][WORD_SIZE - 1] = '0';
            }
            else
            {
                codeWord[i][WORD_SIZE - 1] = '1';
            }
        }
    }
    else if (parity_type[0] == '2')
    {
        // 1D odd
    }
    else if (parity_type[0] == '3')
    { // 2D Even
    }
    else if (parity_type[0] == '4')
    { // 2D odd
    }
    return codeWord;
}

int main(int argc, char const *argv[])
{
    char dataword[ROWS][WORD_SIZE] = {
        "10100",
        "010000",
        "1110",
        "00",
        "10010010",
        "11011011",
        "11001",
        "0101000"};

    char parity_type[4] = "1234"; // Type of parity (one-dimensional-even, one-dimensional-odd, two-dimensional-even, two-dimensional-odd)

    char **codeWord = parity_gen(dataword, parity_type, ROWS);

    for (int i = 0; i < ROWS; i++)
    {
        printf("%s\n", codeWord[i]);
    }

    return 0;
}
