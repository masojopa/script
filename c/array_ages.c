#include <stdio.h>

int main() {

	//An array storing ages
	int ages[] = {20,14,18,23};

	int i ;

	//Get the length of the array
	
	int length = sizeof(ages) / sizeof(ages[0]);

	//Create a lowest age variable and assign the
	//first array element of ages to it
	
	int lowestAge = ages[0];

	//Loop through the elemnts of the ages array
	//to find the loqeat age
	
	for (i = 0; i < length; i++) {

		//Check if the current age is smaller
		//than the current the 'lowestAge'
		
		if (lowestAge > ages[i]) {

			//If smaller age is found
			//update lowestAge with that
			//element
			lowestAge = ages[i];
		}
	}
	//Output the value of the lowestAge
	printf("The lowest age in the array is: %d",lowestAge);


return(0);
	  
}
