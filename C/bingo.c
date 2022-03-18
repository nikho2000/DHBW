#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    int BINGO_NUMBERS[90];
    int cache;
    srand(time(NULL));
    for(int i = 0; i < 90; i++){
        BINGO_NUMBERS[i] = i+1;
    }
    for(int i = 0; i < 90; i++){
        int num = rand()%90;
        cache = BINGO_NUMBERS[i];
        BINGO_NUMBERS[i] = BINGO_NUMBERS[num];
        BINGO_NUMBERS[num] = cache;
    }

    int count = 0;
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 10; j++){
            printf("%i\t", BINGO_NUMBERS[count]);
            count++;
        }
        printf("\n");
    }

    return 0;
}