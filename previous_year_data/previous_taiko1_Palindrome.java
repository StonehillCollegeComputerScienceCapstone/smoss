import java.util.Scanner;
public class Palindrome
{
  public static void main(String[] args)
  {
    int again;
    do{
    Scanner keyboard = new Scanner(System.in);
    int number, length;
    boolean check;
    System.out.println("Please enter an integer");
    number = keyboard.nextInt();
    String x = Long.toString(number);
    length = x.length();
    
    System.out.println(x);  
    
    check = isPalindrome(x, length);
    if(check == true)
      System.out.println("PALINDROME");
    if(check == false)
      System.out.println("NOT A PALINDROME");
      System.out.println("Press 1 to test again");
      again = keyboard.nextInt();
    }while( again == 1);
    
  }//end main
public static boolean isPalindrome (String n, int y)
{
 int start = 0, end = y - 1;
 
if(n.charAt(start) == n.charAt(end))
{
do{
     ++start;
     --end;
   } while (start != y - 1 && end != 0);
   return true;
}
else
   return false;
}

}//end class