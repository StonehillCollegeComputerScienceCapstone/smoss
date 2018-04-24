import java.util.*;
import java.math.*;

//This is for assignment 5, this problem is the Palindrome
//My name is Sam Bradford
//I am in CSC 103, paul kearns helped me by suggesting to look at not as a half and a half,
//but as flipping the whole number

public class Palindrome
{
  public static boolean isPalindrome(int n)
  {
    if (n == -1)
      return false;
    int a=1;
    int count=0;
    do
    {
      a=a*10;
      count++;
    }while(a<n);
    a=a/10;
    
    int ten=1;
    int digit=1;
    int sum=0;
    int part=1;
    
    do
    {
      part = n/a;
      digit= part%10;
      sum=sum+digit*ten;
      a=a/10;
      ten=ten*10;
    }while(a>0); 
    
    if(n == sum)
      return true;
    
    else
      return false;
    
  }
  public static void main(String[] args)
  {
    Scanner input = new Scanner(System.in);
    int number = -1;
    do
    {
      System.out.println("Enter a positive integer (-1 to quit): ");
      number = input.nextInt();
      if (isPalindrome(number))
        System.out.println("PALINDROME");
      
      else if(number!=-1)
        System.out.println("NOT PALINDROME");
      
      
    }while (n!=-1);
    System.out.println("A Santa spits tips at NASA... bye!");
  }
}