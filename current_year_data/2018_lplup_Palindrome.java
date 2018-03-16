import java.util.Scanner; 

public class PalinDrome
{
  private static String palindrome;
  
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Etner a positive integer: "); 
    int num = sc.nextInt(); 
    isPalindrome(num);
    if(isPalindrome(num) == true)
    {
      System.out.println("PALINDROME"); 
    }
    else
    {
      System.out.println("NOT PALINDROME");
    }
  }
  
  public static boolean isPalindrome(int n)
  {
   palindrome = Integer.toString(n);
   
   String reverse = ""; 
   for(int i = palindrome.length()-1; i>0;i--)
   {
    reverse+=palindrome.charAt(i); 
   }
   return palindrome.equals(reverse);
     
    
  }
  
  
  
  
}