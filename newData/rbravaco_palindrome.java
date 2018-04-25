//credit https://www.programmingsimplified.com/java/source-code/java-program-check-palindrome for this code


package com.javacodegeeks.core.palindrome;
import java.util.*;

class Palindrome
{
   public static void main(String args[])
   {
      String first, back = ""; // Objects of String class
      Scanner in = new Scanner(System.in);

      System.out.println("Enter a string to check if it is a palindrome");
      first = in.nextLine();

      int length = first.length();

      for ( int i = length - 1; i >= 0; i-- )
      {
         back = back + first.charAt(i);
         }

      if (first.equals(back))
      {
         System.out.println("Type in the palindrome.");
         }
      else
      {
         System.out.println("type in non palindrome.");
         }

   }
}