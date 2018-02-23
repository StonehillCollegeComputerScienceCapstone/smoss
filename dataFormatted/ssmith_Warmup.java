import java.util.Scanner;
public class Warmup5
{
public static void main(String[] args)
{
   Scanner input = new Scanner(System.in);
   System.out.println("Enter number of times to repeat:");

   int N = input.nextInt();
   versionOfRecursion(N);
}//end main

public static int versionOfRecursion(int n)
{
  if(n == 0)
  {
   return 0; 
  }
  else
  {
  System.out.println("There is a version of recursion."); 
   return versionOfRecursion(n - 1);
  }
}
}//end class