import java.util.Scanner;

public class Goldbach
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Enter an even positive integer greater than 2.");
    int j = keyboard.nextInt();
    System.out.println(goldbach(j));
    
  }//end main
  
  public static int goldbach(int i)
  {
    int x = 0, y = 0;
    while( x<i && y<i)
    {
      if(x+y ==i)
        System.out.println(x + "+" + y);
    }
  return 0;
  
  }//end method
  public static boolean isPrime(int n)
  { 
    int j;
    for(j =2; j<n; j++)
     if(n%j==0)
    {
     return false;
    }
  return true;
  } //end method
  
}//end class