import java.util.Scanner;

public class WarmUp5
{
public static void main(String[] args)
 {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter number of times to repeat:");

    int N = input.nextInt();
    versionOfRecursion(N);
 }

public static void versionOfRecursion(int n)
{
  if (n>0){
       System.out.println("There is a version of recursion.");
       versionOfRecursion(n-1);
  }
}//end method

     
  
}// end class