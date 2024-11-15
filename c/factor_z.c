#include <stdio.h>

int main(){


	int x;
	int largest_prime_factor;

	printf("Please enter the value of x:");
	scanf("%d", &x);
        printf(",%d\n",x);
        printf("\n");


        //Find the factors
	for (int i=2; i<x; ++i){

	    if (x%i==0)

                //Find if the factor is prime
	        for (int j=2; j<i; ++j){

		    if (i%j==0)

                        break;

		    else

                        largest_prime_factor = i; 

		}

             //largest_prime_factor = i; 

	}
printf(",%d\n",largest_prime_factor);

return(0);

}

