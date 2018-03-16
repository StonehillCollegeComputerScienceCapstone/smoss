import java.util.Scanner;


public class Galdbach
{
  public static void main(String[] args)
  {
    
    Scanner keyboard = new Scanner(System.in);
    int even;
    int again;
  
   do
    {
    
     do
     {
      System.out.println("Enter an even positive integer greater than 2: ");
      even = keyboard.nextInt();  
     }while(even<=2 || even%2!=0);
   
     goldbach(even);
            
     System.out.println("Again? Type 1 for yes: ");
     again = keyboard.nextInt();
   
   }while(again==1);
     
 }//end main
  
 public static void goldbach(int n)
  { 
   int P=0, Q=0;
   for(int p=2; p<n ; ++p)
   {
     int q; 
     q= n-p;
     
   if (p>=q && isPrime(p)==true && isPrime(q)==true)
     {
      P=p;
      Q=q;
   }// end if
   }//end for loop
   System.out.println(n + " = " + P + " + " + Q);
  }//end method
   
 
 public static boolean isPrime(int n)
  {
    boolean primeNum= true;
    if (n<=1)
      return false;
    if (n==2)
      return true;
    for(int i=2; i<n ; ++i) 
    {
      if (n % i == 0)
      {
        return false;
      }
    }//end for loop
    return primeNum;
  }//end method 
     
   

}// end class
