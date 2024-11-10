#include <stdio.h>

int main(){


	int x=0;
	int c=0;
	int i=0;
	//int j=0;
	//int length=0;
	int y[]={};

	printf("Please enter the value of x:");
	scanf("%d", &x);

	for(i=0; i<=x; i++){

            c=(x%=i);

	    if(c==0){

	        y[i]=i;
                printf("%d\n",y[i]);
	    }

	}

	//length=sizeof(y) / sizeof(y[0]);

	//for(j=0; j<=length; j++){
          
	//printf("%d\n",y[j]);

	//}


return(0);
}
