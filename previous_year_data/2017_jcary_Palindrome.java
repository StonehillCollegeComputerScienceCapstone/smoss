import java.util.Scanner;

public class Palindrome
{
 public static void main(String[] args)
 {
   Scanner keyboard = new Scanner(System.in);
   System.out.println("Enter an integer.");
   int i = keyboard.nextInt();
   
   if(palindrome(i))
   {
   System.out.println("This is a palindrome.");
   }
   else
     System.out.println("This is not a palindrome.");
   
 }//end main
  
  public static boolean palindrome(int x )
  {
    int forwardNum = x;
    int reverseNum = 0, remainder;
    
    while( forwardNum >0)
    {
      remainder = forwardNum%10;
      reverseNum = reverseNum * 10 + remainder;
      forwardNum = forwardNum / 10;
    }
    if(reverseNum == x)
    {
    return true;
    }
    return false;

 
  }//end palindrome
  
  
  
  
  
}