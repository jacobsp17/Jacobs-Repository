/*
Jacob Price
Lab#5
09/26/24
This program will ask the user for some inputs and then useing those inputs
it will generate interactive stories.
*/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>

//begin the main function 
int main()
{
	//initialize variables to hold user inputs 
	//name, age, favorite color
	//randomnum variable to add randomness 
	char name[10];
	int age;
	char favcolor[10];
	int randomnum = 0, i;
	
	
	
	// ask the user for their name
	printf("What is your name? ");
	//assign the string to the array name
	scanf("%s", &name);
	//ask the user for their age
	printf("\nHow old are you? ");
	//assign that input to age
	scanf("%d", &age);
	//ask the user for their favorite color
	printf("\nWhat is your favorite color? ");
	// assign that string to the array favcolor
	scanf("%s", &favcolor);
	
	// include the time function for randomness
	srand(time(NULL));
	
	// initialize the array vehicles with 4 strings inside
	char *vehicles[4] = {"Ford Mustang","Chevy Camaro","Audi R8","BMW M4"};
	// initialize the array favplaces with 4 strings inside 
	char *favplaces[4] = {"Speed Art Museum","Waterfront Park","Louisville Zoo",
						  "Kentucky Derby Museum"};
	
	// assign randomnum a random number between 0 and 3 for the amount
	// of elements in the arrays 
	randomnum = (rand() % 4);
	
	// display the interactive story 
	printf("\nHello my name is %s, and I am %d years old.\n"
			, name, age);
	printf("I have a %s that is %s. One of my favorite places"
			,(vehicles[randomnum]), favcolor);
	printf(" to \ntake my car to in Louisville Kentucky is the %s."
			,(favplaces[randomnum]));
	
	
	
}