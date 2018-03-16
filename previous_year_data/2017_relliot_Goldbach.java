import java.util.Scanner;
public class Goldbach
{
public static void main(String[] args)
{
Scanner input = new Scanner(System.in);
int N = 0, B;
do
{
do
{
System.out.println("Enter an even positive integer greater than 2:");
N = input.nextInt();
}
while(N % 2 != 0);
goldbach(N);
System.out.println("Again? 1 for yes:");
B = input.nextInt(); 
}while(B == 1);

}//end main

public static void goldbach(int n)
{
for (int x = 2; x < n; x++)
{
if (isPrime(x) == true)
{
 for (int y = 2; y < n; y++)
  {
   if (isPrime(y) == true)
    {
     if((x + y) == n)
      {
       System.out.println(n + " = " + x + " + " + y);
      }
     }
     
    }
    
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

return primeNum;
}//end method




}//end class