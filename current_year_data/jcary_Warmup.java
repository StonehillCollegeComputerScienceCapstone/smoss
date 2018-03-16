import java.util.Scanner;

public class Warmup5
{
public static void main(String[] args)
{
   Scanner keyboard = new Scanner(System.in);
   System.out.println("Enter number of times to repeat:");

   int n = keyboard.nextInt();
   versionOfRecursion(n);
}// end main

public static void versionOfRecursion(int n)
{
  System.out.println("This is a version of recursion");
  if(n>1)
  {
    versionOfRecursion(n-1);
  }
}
}//end class