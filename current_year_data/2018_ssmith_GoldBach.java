import java.util.Scanner;
public class GoldBach
{
  public static void main(String[] args)
  {
    int num, again;
   Scanner keyboard = new Scanner(System.in);
   
   do
   {
   do
   {
   System.out.println("Enter an even positive integer greater than 2: ");
   num = keyboard.nextInt();
   if(num % 2 != 0)
   {
     System.out.println("Not an even number. Enter a new number.");
   }//end if
   }while(num % 2 != 0);
   goldbach(num);
   System.out.println("Again? Enter 1 for yes.");
   again = keyboard.nextInt();
   }while(again == 1);
    
  }//end main
  
  public static void goldbach(int n)
  {
    for(int x = 2; x < n; x++)
    {
      if(isPrime(x) == true)
      {
        for(int y = 2; y < n; y++)
        {
         if(isPrime(y) == true)
         {
          if((x + y) == n)
          {
           System.out.println(n + " = " + x + " + " + y); 
          }//end if
         }//end if
        }//end for
      }//end if
    }//end for
  }//end method
  
  public static boolean isPrime(int n)
  {
    boolean prime = true;
    
    if(n <= 1)
    {
      return false;
    }//end if
    if(n == 2)
    {
      return true;
    }//end if
    
    for(int i = 2; i < Math.sqrt(n) + 1; i++)
    {
      if(n % i == 0)
      {
        return false;
      }//end if
    }//end for
    return prime;
  }//end method
  
}//end class