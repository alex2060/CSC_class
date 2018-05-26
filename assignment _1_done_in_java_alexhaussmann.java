/*
interactive average program 

This program askes the user to askes the user to imput to real numbers 
caclulats and prints the avererag and prints th numbers 
alex haussmann 
program #1 cs 1050 section 1

*/


import java.util.Scanner;

public class alexhaussmann_S_0_1{
	public static void main(String[]args){
		Scanner console = new Scanner(System.in);
		double num1 = 0.0;    											//input value 1
		double num2 = 0.0;    											//input value 1
		double avererag = 0.0;    										//Average of input values
																
		System.out.println("this program averages two numbers");		// gives explanation to user

		System.out.print("enter first number: ");						// input two numbers
		num1=console.nextDouble();
		System.out.print("enter first number: ");
		num2=console.nextDouble();
		avererag=(num1+num2)/2;

		System.out.print("the avererag of "+num1);						// outputs
		System.out.print(" and "+num2+ " is " + avererag);
		System.out.println("alex haussmann");

		console.close();
		System.exit(0);
	}																	// end of main
}																		// end of alexhaussmann_S_0_1



