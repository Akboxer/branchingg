#include <stdio.h>

int main(){
    //printing even numbers
    printf("today we are printing star pattern \n");
    for (int i = 0 ; i<5; i++){
        for (int j = 0 ; j<i; j++){
            printf("*");
        }
        printf("\n");
    }
}   