import java.util.Scanner;
public class Palindrome
{
 public static void main(String[] args){
 Scanner keyboard = new Scanner(System.in);
 int n;
 
 System.out.println("--- Welcome to the Palindrome Detector! ---");
 System.out.println("Enter positive integer (-1 to quit):");
 n = keyboard.nextInt();
 if(n == -1){
 System.exit(0);
 }
 if(isPalindrome(n))
  System.out.println("PALINDROME");
  else
   System.out.println("NOT PALINDROME");
  
 }
 public static boolean isPalindrome(int n){
 int reversedN = 0;
 int x = n;
 while(x !=0){
  int remainder = x%10;
  reversedN = reversedN * 10 + remainder;
  x = x/10;
  }
  if(n == reversedN){
  return true;
  }
  else
   return false;
  }
}