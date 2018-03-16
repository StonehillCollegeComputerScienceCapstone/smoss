import java.util.Scanner;

public class warmup
{
  public static void main(String[] args)
{
   Scanner input = new Scanner(System.in);
   System.out.println("Enter number of times to repeat:");

   int N = input.nextInt();
   versionOfRecursion(N);
}
  
  public static int versionOfRecursion(int n)
  {
   if(n == 0)
     return 0; 
   else{
    System.out.println("Version of recursion");
    return versionOfRecursion(n-1);
   }
     
    
  }
  
  
  
}