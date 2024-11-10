#include <stdio.h>

int main(){


	int x=0;
	int y=0;
	int c=0;

	printf("Please enter the value of x:");
	scanf("%d", &x);
        printf("Please enter the value of y:");
        scanf("%d", &y);
        c=(x%=y);
	printf("%d\n",c);


return(0);
}
