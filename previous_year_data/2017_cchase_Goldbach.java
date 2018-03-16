import java.util.Scanner;

public class Goldbach
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    goldbach(keyboard.nextInt(), 2);
    
    
    
    
    
    
  }//end main
  
  public static void goldbach(int n, int j)
  {
      boolean isPrime1 = PrimeNumber.isPrime(j);
      boolean isPrime2 = PrimeNumber.isPrime(n - j);
      if (j == n)
        System.out.println ("Done");
      else if(isPrime1 && isPrime2)
      {
        System.out.println(n + " = " + j + " + " + (n - j));
       goldbach (n, j + 1);
      }
       else
        goldbach(n, j + 1);
    
  }//end method goldbach

  
  
  
  
  
  
  
  
  
}//end class