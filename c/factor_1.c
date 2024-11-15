#include <stdio.h>

int factor(int x){

    int i=1;
    int y[50]={1};

    for(i=1; i<=x; ++i){

	    if((x%i)==0){
	        y[i]=i;
	       //printf(",%d\n",y[i]);
            }
    } 
return(y[i]);

}

void pri(int y[50]){

     int j;

     for(j=0; j<50; ++j);
         printf(",%d\n",y[j]);
}

int main(){


	int x;
	int z;

	printf("Please enter the value of x:");
	scanf("%d", &x);
        printf(",%d\n",x);
        printf("\n");

	z=factor(x);
        printf(",%d\n",z);

return(0);

}

