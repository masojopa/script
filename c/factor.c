#include <stdio.h>

int factor(int x){

    int i=1;
    int y[50]={1};

    for(i=1; i<=x; ++i){

	    if((x%i)==0){
	        y[i]=i;
	        printf(",%d\n",y[i]);
            }
    } 
return(y[i]);

}

int main(){


	int x;

	printf("Please enter the value of x:");
	scanf("%d", &x);
        printf(",%d\n",x);
        printf("\n");

        factor(x);

return(0);

}

