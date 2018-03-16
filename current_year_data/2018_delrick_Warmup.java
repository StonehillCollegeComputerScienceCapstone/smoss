import java.util.Scanner;
public class Warmup05
{

public static void main(String[] args)
{
   Scanner input = new Scanner(System.in);
   System.out.println("Enter number of times to repeat:");
   int N = input.nextInt();
   versionOfRecursion(N);
}

public static void versionOfRecursion(int N)
{
 if(N == 1)
   System.out.println("There is a version of recursion.");
  else{ 
   System.out.println("There is a version of recursion.");
   versionOfRecursion(N-1);
   
}//end method

}//end class

 
 
 