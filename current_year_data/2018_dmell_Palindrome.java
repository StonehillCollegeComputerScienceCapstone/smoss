import java.util.Scanner;
public class Palindrome
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
      int g, u;
    System.out.println("Please input an integer.");
    g = keyboard.nextInt();
    String n = Integer.toString(g);
    String reverse = " ";
    for(int p = n.length() - 1; p > 0; --p)
    {
      reverse = reverse + n.CharAt(p);
    }//end for
    System.out.println(reverse);
    
    
    
    
    
  }//end main
}//end class