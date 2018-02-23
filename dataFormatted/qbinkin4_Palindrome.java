import java.util.*;
public class Palindrome
{

public static void main(String[] args)
{
Scanner keyboard = new Scanner(System.in);
System.out.println("Enter a number with more than one digit.");
String x = keyboard.nextLine();
System.out.println(isPalindrome(x));
}//end main

public static boolean isPalindrome(String s)
{
String opp = ""; 
for(int i = s.length()-1; i >= 0; --i)
{
opp = opp + s.charAt(i);
}//end for 
if (s.equals(opp))
 return true;
else 
 return false;
}//end method

}//end class