import java.util.Scanner;
import java.lang.Math;

public class Palindrome
{
  public static void main(String[] args)
  {
    Scanner input = new Scanner(System.in);
    int userInt;
    do
    {
    System.out.println("Enter positive integer (-1 to quit): ");
    userInt = input.nextInt();
    if (userInt > 0)
    testPalindrome(userInt, userInt, 0, initialMultiplier(userInt));
    }while (userInt > 0);
  }//end main

  public static void testPalindrome(int userInput, int original, int sum, int multiplier)
  {
    //System.out.println(userInput + " " + sum);
   if (userInput < 10 && sum == 0)
     System.out.println("Palindrome");
   if (userInput == 0 && original != sum)
     System.out.println("Not Palindrome");
   else if(userInput == 0 && original == sum)
     System.out.println("Palindrome");
   else
   {
     testPalindrome(userInput/10, original, sum + (userInput%10) * power(multiplier), multiplier - 1);
   }
    
    
  }//end method testPalindrome

public static int power(int m)
{
  int mult = 1;
  if (m == 0)
    return 1;
  else
  {
    for (int i = 0; i < m; i++)
  {
    mult = mult * 10;
  }//end for
  return mult;
}//end else
}//end method power

public static int initialMultiplier(int input)
{
  int multi = -1;
    while (input > 0)
  {
   input = input/10;
   multi++;
  }//end while
  return multi;
  
  
}//end method initialMultiplier


}//end class