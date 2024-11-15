#include <stdio.h>

int main(){


	int x[] ={5,7,13,29,35,65,91,145,203,377,455,1015,1885,2639};

	//printf("Please enter the value of x:");
	//scanf("%lld",&x);
        //printf(",%lld\n",x);
        //printf("\n");


        //Find the factors
	for (int i=0; i<14; ++i){

	    for (int j=1; j<15; ++j){

	        if((x[i]%j==0)&&(x[i]==j)){
                    printf("+++++++++++++\n");
                    printf(",%d\n",x[i]);
                    printf(",%d\n",j);
		}

	    }
	}

return(0);

}

