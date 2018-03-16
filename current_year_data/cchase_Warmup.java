import java.util.Scanner;
public class VersionOfRecursionProg
{
  public static void main(String[] args)
{
Scanner input = new Scanner(System.in);
System.out.println("Enter number of times to repeat:");
int n = input.nextInt();
versionOfRecursion(n);
}
  
  public static void versionOfRecursion(int n)
  {
    if (n == 1)
      System.out.println("There is a version of recursion.");
    else
    {
      System.out.println("There is a version of recursion.");
      versionOfRecursion(n - 1);
    }
    
    
    
    
    
    
    
  }//end method
  
  
  
  
  
  
  
  
}//end class