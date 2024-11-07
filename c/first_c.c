// Create an int and a char variable

#include <stdio.h>

int main()  {
	
    int myNum;
    char myChar;

    // Ask the user to type a number AND a character
    printf("Type a number, a char and press enter: \n");

    // Get and save the number and  char the user types
    scanf("%d %c", &myNum, &myChar);

    // Print the number
    printf("Your number is: %d\n", myNum);

    // Print the character
    printf("Your character is: %c\n", myChar);

return 0;

}
