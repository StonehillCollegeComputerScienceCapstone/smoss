import java.util.Scanner;
public class Warmup
{
  public static void main(String[] args)
  {
   Scanner input = new Scanner(System.in);
   System.out.println("Enter number of times to repeat:");

   int N = input.nextInt();
   versionOfRecursion(N);
  }//end main
  public static int versionOfRecursion (int x)
  {
if (x == 0)
{
return 0;
}
 else 
   System.out.println("This is a version of recursion");
    return versionOfRecursion(x - 1);
}
}  