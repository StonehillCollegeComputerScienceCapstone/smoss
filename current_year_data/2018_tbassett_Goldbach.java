import java.util.Scanner;
public class Goldbach
{
public static void main(String[] args)
{

System.out.println("Enter an even positive integer greater than 2: ");
Scanner user = new Scanner(System.in);
int n = user.nextInt();
if(n % 2 > 0)
{
System.out.println("Run again. Number must be even");
}
int a = goldbach();
int b = goldbach();

if(isPrime(a) == true)
System.out.println(a);
if(isPrime(b) == true)
System.out.println(b);

}//end main

public static int goldbach(int n)
{

for(int i = 2; i < n; i++)
{
int a = a + 1;
int b = b + 1;
}
if(a + b == n)
{
return a;
return b;
}
else
{
return 0;
}

}//end goldbach

public static boolean isPrime(int n)
{
boolean primeNum = true;
if(n <= 1)
return false;
if(n == 2)
return true;
for(int i = 2; i < Math.sqrt(n) + 1; ++i)
{
if(n % i == 0)
return false;
}//end loop
return true;
}//end isPrime

}//end class