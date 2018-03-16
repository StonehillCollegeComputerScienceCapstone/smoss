import java.util.Scanner;
public class WarmUpFive
{
public static void main(String[] args)
{
Scanner input = new Scanner(System.in);

   System.out.println("Enter number of times to repeat:");

   int N = input.nextInt();
   versionOfRecursion(N);
   
}//end main

public static int versionOfRecursion(int X)
{

if (X == 0)
{
return 0;
}
else
{ 

System.out.println("There is a version of recursion.");
return versionOfRecursion(X - 1);
}
}}


