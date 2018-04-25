import java.util.*;
import java.math.*;

public class Palindrome
{
  public static boolean isPalindrome(int number) {
    int palindrome = number; // copied number into variable
    int reverse = 0;
    
    while (palindrome != 0) {
      int remainder = palindrome % 10;
      reverse = reverse * 10 + remainder;
      palindrome = palindrome / 10;
    }
    
    // if original and reverse of number is equal means
    // number is palindrome in Java
    if (number == reverse) {
      return true;
    }
    return false;
  }
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    int input = 0;
    while(input!=-1)
    {
      input = keyboard.nextInt();
        
      if(isPalindrome(input))
        System.out.print("PALINDROME");
      else if(input!=-1)
        System.out.println("Not a palindrome);
    }
  }
}