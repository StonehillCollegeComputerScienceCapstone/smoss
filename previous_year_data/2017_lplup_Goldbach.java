import java.util.Scanner;

public class Goldbach
{
 public static void main(String args[])
 {
  Scanner sc = new Scanner(System.in); 
  System.out.println("Enter an even positive integer greater than 2: ");
  int goldb = sc.nextInt();
   
 }
  
  
  public static void goldback(int n)
  {
    if(n < 2)
    {
     System.out.println("Error must be greater than 2");
    }
    else{
      
     int fitstN = nextPrime(n);
     int secN = nextPrime(n-1);
     System.out.println("Your numbers are " + firstN + " and " + secN);
      
      
      
    }
    
    
  }
  
  public static int nextPrime(int n)
  {
   for(int x=n+1;;x++)
   {
    for(int y=2;y<=x;y++)
    {
     if(x%y!=0)
     {
       return x;
    }
      
    }
   }
    
  }
  
  public static boolean isPrime(int n)
  {
   if(n%2 == 0)
     return false; 
   else 
     return true;
    
  }
  
  
  
  
}