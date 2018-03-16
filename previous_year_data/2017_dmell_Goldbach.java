import java.util.Scanner;
public class Goldbach
{
public static void main(String[] args)
{
  Scanner keyboard = new Scanner(System.in);
    long n;
  n = keyboard.nextLong();
  goldbach(n);
}//end main


 public static void goldbach(long n)
 {
    long m, g, c, t;
   if ( n > 2)
   {
     for( int i = 1; i < n; ++i)
     {
         m = n % i;
         System.out.println(m);
     }//end for
   }//end if
 }//end method
 
}//end class
         
   