import java.util.Scanner;
public class Warmup5
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Please enter the numver of times you want it to repeat");
    int n = keyboard.nextInt();
    
    versionOfRecursion(n);
    
  }//end main
  
  public static void versionOfRecursion(int i)
  {
    if(i == 1)
     System.out.println("There is a version of Recursion");
  else
  {
     System.out.println("There is a version of Recursion");
    versionOfRecursion(i - 1);
  }
  }//end method
 
}//end class