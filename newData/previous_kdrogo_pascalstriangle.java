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

 public static int fact (int n) //Recursion
 {	 
   if (n == 0)
     return 1;   
   else if (n > 0 && n < 13) //If n >= 13, error occurs in printing pascal's triangle.
	 return n*fact(n-1);  
   else 
     throw new RuntimeException("Error "+n); //This shouldn't need to be thrown, but it doesn't 
                                             //hurt to implement it in case of unsolved error.
 }
 
 public static void triangle() //Triangle creation.
 {
   BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //Set up input.
   System.out.println("Enter the desried num of rows, between 0 and 13 exclusive, +" +
   		"of Pascal's triangle, " + "-1 to exit.");
	   
   try 
   {	
	 String input = br.readLine();	       //Store user input.
	 int num = Integer.parseInt(input); //Parse input string into an int to work with.   
	  
	 while (num != -1 && num < 13)
     { 
	   int[][] output = new int[num+1][num+1]; //num+1 to include the 0th row. 
	   String[] sp = new String[num+1];       //used for organizing the triangle via sp.
	   sp[num] = "";                          //No space on the last row.
	   
	   for (int c = num-1; c >= 0; c--) 
	   {
	     sp[c] = sp[c+1] + "  ";  //Assign appropriate Strings to sp[].
	   }
	   
       for (int i = 0; i <= num; i++)
	   {                                //i is the num of rows (input/num), 
    	                                //r is the num of items in each row.
	     for (int r = 0; r <= i; r++)
         {	 
		   output[i][r] = fact(i)/(fact(r)*fact(i-r)); //formula for values in 
		   															  //Pascal's triangle. 
		   if (r == 0)
		   { 	                         
		     System.out.print(sp[i] + output[i][r]); //Use sp[] to organize nums 	 	                                         
		   }                                             //into a triangular shape.
		      	   		   
		   else  //If num isn't the first of each row in Pascal's triangle... 
		   {  
		     if (output[i][r] > 0 && output[i][r] <= 9)
		     {
			   System.out.print("   " + output[i][r]);             
		     }                                          //The sp will organize the triangle.
		   
		     else if (output[i][r] > 9 && output[i][r] <= 99)
		     {
		       System.out.print("  " + output[i][r]);  
		     }  
		   
		     else 									//If num is greater than 99, put one space
		     {                                      //before output.
		       System.out.print(" " + output[i][r]);
		     }	
		     
		   }
		   
         } 	   
	     
	     System.out.println();   //Start a new line every time "i" counter increases.
       }
		
	   System.out.println("\nEnter the desried num of rows, (> than 0), of Pascal's triangle, " +
	   "zero to exit.");
	  
	   input = br.readLine();	              //Store user input.
	   num = Integer.parseInt(input);      //Parse input string into an int to work with.
		
	   output = new int[num+1][num+1]; /*Reset the size of the array to make it*/
     }                                       /*suitable for next output.*/
 
	 if (num == -1)
	   System.out.println("Good bye!"); //If num = 0, exit. 
	 
	 else if (num >= 13 || num < -1) 	  
	 {
       System.out.println("num must be > 0 and < 13.\n");        
	   triangle();                       //Recall the method.
	 }	 
	 
   }	
		
   catch (IOException one) 
   {
     System.out.println(one);  //This exception has never occured while making this program.
   } 
		
   catch (numFormatException two)
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