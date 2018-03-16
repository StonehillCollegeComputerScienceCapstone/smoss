import java.util.Scanner;
public class Goldbach
{
public static void main(String[] args)
{
 Scanner keyboard = new Scanner(System.in);
 boolean again = false;
 do{
 System.out.println("Please enter an even integer greater than 2");
 int n = keyboard.nextInt();
 if (n%2 == 0)
  {
  goldbach(n);
 System.out.println("Again? Type 1 for yes, any other number for no.");
 int t = keyboard.nextInt();
  if (t==1)
   again = true;
  else 
   again = false;
 }//end if 
}while(again); //end do while  
}//end main

public static void goldbach(int n)
{
for (int j=2; j <= n/2; j++)
{
if (isPrime(j) && isPrime(n-j))
 {
 System.out.println(j + " + " + (n-j));
 }
} 
}//end method

public static boolean isPrime(int n)
{
for (int i = 2; i < n; i++)
 {
 if (n%i==0)
  {
  return false;
  }
 }//end for
 return true;
}//end method

}//end class