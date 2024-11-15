#include <stdio.h>

int main(){


	//int x[] ={5,7,13,29,35,65,91,145,203,377,455,1015,1885,2639};
	
	int y;

	printf("Please enter the value of y:");
	scanf("%d",&y);
        printf(",%d\n",y);
        printf("\n");


        //Find the factors
	for (int i=0; i<14; ++i){

		int p = (y%i);

		if (p==0){

	        for (int j=1; j<15; ++j){

	            if((p%j==0)&&(p==j)){

                        printf("+++++++++++++\n");
                        printf(",%d\n",p);
                        printf(",%d\n",j);
		}

	    }
	
          }

	}

return(0);

}

