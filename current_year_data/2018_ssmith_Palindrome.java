import java.util.Scanner;
import java.util.*;

public class Palindrome
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    int num;
   
    do
    {
    System.out.println("Enter a positive integer, or -1 to quit: ");
    num = keyboard.nextInt();
      if(num > 0)
    {
      boolean isPal = isPalindrome(num);
      if(isPal == true)
      {
        System.out.println("Palindrome");
      }//end if
      else
      {
        System.out.println("Not palindrome");
      }//end else
    }//end if
    else
    {
      System.out.println("A Santa spits tips at NASA... bye!");
    }//end else
    }while(num > 0);
  }//end main
  
  
  public static boolean isPalindrome(int n)
  {
    boolean pal = false, equal;
    String number = Integer.toString(n);
    String backwardNumber = "";
    
    for(int i = number.length() - 1; i >= 0; i--)
    {
    backwardNumber = backwardNumber + number.charAt(i);
    }//end for
    equal = number.equals(backwardNumber);
    if(equal == true)
    {
      pal = true;
    }//end if
    return pal;
  }//end method
  
}//end class