import java.util.Scanner;
public class Goldbach
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Please enter an even positive number");
    int n = keyboard.nextInt();
    
    goldbach(n);
    
  }//end main
  
  public static void goldbach(int n)
  {
    int p = 0, q = 0;
    
    for(int i = 0; i < n; i ++)
    {
      if (isPrime(i))
      {
        for (int k = 0; k < i; k++)
        {
          if (isPrime(k) && (k + i == n))
          {
              p = k;
              q = i;
            }
          }
        }
      }
      
        
    
    isPrime(p);
    isPrime(q);
    if(n == p + q)
    System.out.println(n + " = " + p + q);
    
    
  }//end method
  
  public static boolean isPrime(int n)
  {
    for(int i = 1; i < n; ++i)
    {
      int m = n % i;
      return m == 0;
    }//end for\
    
    return false;
    
    
  }//end method
  
  
  }//end class