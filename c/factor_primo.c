#include <stdio.h>

int main(){


	int x;
	int c;
	int i=1;
	int j=0;
        int y[5]={};
	int length=sizeof(y) / sizeof(y[0]);

	printf("Please enter the value of x:");
	scanf("%d", &x);
        printf(",%d\n",x);
        printf("\n");

	for(i=1; i<=x; ++i){

	    if((x%i)==0){
	        y[i]=i;
                //printf(",%d\n",y[i]);

	    }
	}
        
	//length=sizeof(y) / sizeof(y[0]);

	for(j=0; j<=length; ++j){
          
	printf("%d\n",y[j]);

	}


return(0);
}

