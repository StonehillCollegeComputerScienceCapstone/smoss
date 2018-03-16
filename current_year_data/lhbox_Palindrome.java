import java.util.Scanner;

public class Palindrome
{
public static void main(String[] args)
 {
    Scanner input = new Scanner(System.in);
   
  System.out.println("---Welcome to the Palidrome Detector!---");
  int integer;
  
  do
   {
     System.out.print("Enter positive integer(-1 to quit): ");
     integer = input.nextInt();
     System.out.println(integer);
     
     if(isPalindrome(integer)==true)
      {
        System.out.println("PALINDROME");
      }
     if(isPalindrome(integer)==false)
      {
        System.out.println("NOT PALINDROME");
      }
     System.out.println();
   }while(integer!= -1);
    
    System.out.println("A Santa spits tips at NASA...bye!");
    
 }//end main method

public static boolean isPalindrome(int n)
{
  int initialValuen = n; //to save intial value of n
  int backwards= 0;
  int left;
  
  while(n!=0)
  {
    left = n%10;
    backwards= (backwards * 10) + left;
    n= n/10;
  }
 
  if(initialValuen == backwards)
  {
    return true;
  }
  else
  {
    return false;
  }
}//end method

     
     
 
}// end class