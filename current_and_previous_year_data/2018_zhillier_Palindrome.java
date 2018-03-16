import java.util.Scanner;
public class Palindrome
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    int reverse = 0;
    System.out.println("Please enter a number");
    int n = keyboard.nextInt();
    String StringN = Integer.toString(n);
    
  isPalindrome(n);
    
    if(true)
      System.out.println("Palindrome");
    else
      System.out.println("Not a Palindrome");
    
    
  }//end main
  
  public static boolean isPalindrome(int n)
  {
   String StringN = Integer.toString(n);
    int reverse = 0;
    for(int i = StringN.length() - 1; i > 0; --i)
    {
      reverse = reverse + StringN.charAt(i);
    }
    if(n == reverse)
      return true;
    else
      return false;
    
  }//end method
  
  
}//end class