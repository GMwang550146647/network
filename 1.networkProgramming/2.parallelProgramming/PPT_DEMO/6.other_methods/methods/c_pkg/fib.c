#include "time.h"
#include <stdio.h>
int fib(int n){
    if(n<=1) return 1;
    else return fib(n-1)+fib(n-2);
}

int main(){
    double dur;
    clock_t start,end;
    start = clock();
    int n=35;
    int result=fib(n);
    end = clock();
    dur = (double)(end - start);
    printf("using %f ms result: %d\n",(dur/CLOCKS_PER_SEC)*1000,result);
}