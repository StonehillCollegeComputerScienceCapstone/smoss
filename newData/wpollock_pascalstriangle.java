/*****************************/
/***** By Dillon Dommer ******/
/** Tuesday, April 21, 2009 **/
/*****************************/

import java.io.*;  //Needed for input stream.

public class DillonPascal 
{
	
 public static void main(String[] args) 	
 {
   triangle();
 }

 public static int factorial (int n) //Recursion
 {	 
   if (n == 0)
     return 1;   
   else if (n > 0 && n < 13) //If n >= 13, error occurs in printing pascal's triangle.
	 return n*factorial(n-1);  
   else 
     throw new RuntimeException("Error "+n); //This shouldn't need to be thrown, but it doesn't 
                                             //hurt to implement it in case of unsolved error.
 }
 
 public static void triangle() //Triangle creation.
 {
   BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //Set up input.
   System.out.println("Enter the desried number of rows, between 0 and 13 exclusive, +" +
   		"of Pascal's triangle, " + "-1 to exit.");
	   
   try 
   {	
	 String input = br.readLine();	       //Store user input.
	 int number = Integer.parseInt(input); //Parse input string into an int to work with.   
	  
	 while (number != -1 && number < 13)
     { 
	   int[][] output = new int[number+1][number+1]; //number+1 to include the 0th row. 
	   String[] spaces = new String[number+1];       //used for organizing the triangle via spaces.
	   spaces[number] = "";                          //No space on the last row.
	   
	   for (int c = number-1; c >= 0; c--) 
	   {
	     spaces[c] = spaces[c+1] + "  ";  //Assign appropriate Strings to spaces[].
	   }
	   
       for (int i = 0; i <= number; i++)
	   {                                //i is the number of rows (input/number), 
    	                                //r is the number of items in each row.
	     for (int r = 0; r <= i; r++)
         {	 
		   output[i][r] = factorial(i)/(factorial(r)*factorial(i-r)); //formula for values in 
		   															  //Pascal's triangle. 
		   if (r == 0)
		   { 	                         
		     System.out.print(spaces[i] + output[i][r]); //Use spaces[] to organize numbers 	 	                                         
		   }                                             //into a triangular shape.
		      	   		   
		   else  //If number isn't the first of each row in Pascal's triangle... 
		   {  
		     if (output[i][r] > 0 && output[i][r] <= 9)
		     {
			   System.out.print("   " + output[i][r]);             
		     }                                          //The spaces will organize the triangle.
		   
		     else if (output[i][r] > 9 && output[i][r] <= 99)
		     {
		       System.out.print("  " + output[i][r]);  
		     }  
		   
		     else 									//If number is greater than 99, put one space
		     {                                      //before output.
		       System.out.print(" " + output[i][r]);
		     }	
		     
		   }
		   
         } 	   
	     
	     System.out.println();   //Start a new line every time "i" counter increases.
       }
		
	   System.out.println("\nEnter the desried number of rows, (> than 0), of Pascal's triangle, " +
	   "zero to exit.");
	  
	   input = br.readLine();	              //Store user input.
	   number = Integer.parseInt(input);      //Parse input string into an int to work with.
		
	   output = new int[number+1][number+1]; /*Reset the size of the array to make it*/
     }                                       /*suitable for next output.*/
 
	 if (number == -1)
	   System.out.println("Good bye!"); //If number = 0, exit. 
	 
	 else if (number >= 13 || number < -1) 	  
	 {
       System.out.println("Number must be > 0 and < 13.\n");        
	   triangle();                       //Recall the method.
	 }	 
	 
   }	
		
   catch (IOException one) 
   {
     System.out.println(one);  //This exception has never occured while making this program.
   } 
		
   catch (NumberFormatException two)
   {	
	 System.out.println("Input must be a valid integer!\n"); //This exception should never occur.	
     triangle(); //Recall the method.
   }
		
   catch (ArrayIndexOutOfBoundsException three)
   {
	 System.out.println("Array is too small!\n"); //This exception should never occur.
   }
		
   catch (NegativeArraySizeException four)
   {
     System.out.println("Input must be positive!\n"); //This exception should never occur.
     triangle(); //Recall the method.
   } 
   
 } 
 
}