import java.util.Scanner;
public class Goldbach
{
public static void main(String[] args)
{

int n, factor1, factor2;
int again;
do
{

Scanner keyboard = new Scanner(System.in);
do
{
System.out.println("Enter an even positive integer greater than 2: ");
n = keyboard.nextInt();
}while (n%2!=0 || n<=2);

goldbach(n);
 
System.out.println("Want to play again? 1 for yes");
again = keyboard.nextInt();
}while(again == 1);

}//end main

public static void goldbach(int n)
{
int q;
for(int p=2; p<n; ++p)
{
q=n-p;

if(isPrime(p) ==true && isPrime(q)== true)
{
System.out.println(n + " = " + p + " + " + q);
break;
}
}//end for loop

}//end method 

public static boolean isPrime(int n)
{
boolean primeNum = true; 
if(n<=1)
{
return false;
}
if(n==2)
{
return true;
}
for(int i= 2; i<Math.sqrt(n) +1; ++i)
if(n % i ==0)
{
return false;
}//end for loop
return primeNum;
}//end method

}//end class