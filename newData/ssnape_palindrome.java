import java.util.*;
import java.math.*;

public class Palindrome
{
  public static void main(String[] args)
  {
    Scanner input = new Scanner(System.in);
    int n=0;
    do
    {
      System.out.println("Enter a positive integer (-1 to quit): ");
      n= input.nextInt();
      if (n!=-1) 
      {
      if (isPalindrome(n))
      {
        System.out.println("PALINDROME");
      }
      else
      {
        System.out.println("NOT PALINDROME");
      }
      }
    }while (n!=-1);
    System.out.println("A Santa spits tips at NASA... bye!");
  }
  public static boolean isPalindrome(int n)
  {
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

    }while(a>0); //once a is less than 0 it stops because it would be undefined
    
    if (n==sum)
    {
    return true;
    }
    else
    {
      return false;
    }
  }
}