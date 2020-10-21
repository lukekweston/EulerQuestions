#include <stdio.h>
#include <stdlib.h>

int main()
{
    int f1 = 0;
    int f2 = 1;
    int sum = 0;

    while(f1 < 4000000){
        if(f1 % 2 == 0){
            sum += f1;
        }
        int temp = f2;
        f2 = f1+ f2;
        f1 = temp;

    }

    printf("%d\n", sum);

    int sum2 = 0;
    int f3 = 0;
    for(int i = 0; f3 < 4000000; i ++){
            f3 = recurssiveFib(i);
            if(!(f3 % 2)){
                sum2 += f3;
            }
            printf("%d: %d\n", i, recurssiveFib(i));
    }

    printf("%d\n", sum2);

    return 0;
}

//Recurssively gets fibonaci numbers
//n is the index of the fibonacci number in the sequence
int recurssiveFib(int n){
    if(n <= 1){
        return n;
    }
    else{
        return(recurssiveFib(n - 1) + recurssiveFib(n - 2));
    }


}
