import java.util.Scanner;
public class palindrome  
{
  public static void main(String[] args)
  {
Scanner keyboard = new Scanner(System.in);    
System.out.println("Enter a palindrome"); 
int x;
x = keyboard.nextInt();
String n = "";
n = Integer.toString(x);
String reverse = "";

for(int i = n.length() - 1; i >= 0; i--)
{
  reverse = reverse + n.charAt(i);
  }
  if(reverse.equals(n))
  {
 System.out.println("Palindrome"); 
  }
 else
  System.out.println("not Palindrome");
}
}