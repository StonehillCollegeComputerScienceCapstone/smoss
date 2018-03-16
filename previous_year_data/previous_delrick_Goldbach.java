import static java.lang.Math.sqrt;
import java.util.Scanner;
public class Goldbach
{
public static void main(String[] args)
{
  Scanner keyboard = new Scanner(System.in);
  int n;
 
 System.out.println("Enter an even positive integer greater than two:");
   n = keyboard.nextInt();
 if(n<3 || (n % 2) != 0){
   System.out.println("Enter an even positive integer greater than two:");
   n = keyboard.nextInt();
   }
 if(n>2 && n % 2 == 0){
   goldbach(n);
   System.out.println("Again? 1 for yes:");
   }

 goldbach(n);
 
 
}
 public static boolean goldbach(int n)
 {  
  for(int i = 3; i < n/2; ++i){
   if (isPrime(i) && isPrime(n - i)){ 
   return true;
   }
    if else{
    return false;
    }
   }
 }
 public static boolean isPrime(int n)
 {
  boolean primeNum = true;
  if(n <= 1)
       return false;
  if(n == 2)
       return true;
  for(int i = 2;i < Math.sqrt(n) + 1; ++i)
  {
   if(n % i == 0)
   return false;
  }//end loop
}
}
