import java.util.Scanner;
import java.util.*;
public class Palindrome{
   public static void main (String[] args){
      System.out.println("--- Welcome to the Palindrome Detector! ---");
      Scanner keybord= new Scanner(System.in);
    
     System.out.println("Enter positive integer (-1 to quit):");
      int g=keybord.nextInt();
      String r = Integer.toString(g);
   //int i=i.length();
      System.out.println(isPalindrome(g,r));
   }


   public static boolean isPalindrome(int g,String r){
      boolean isPalindrome = false ;
      String rev="";
      int i;
     for (i = r.length() - 1;i>=0;i--){
         rev+=r.charAt(i);
   // returns true if n is prime, false if not
      }
     
      if (r.equals(rev)){
            return true;
         }
         
      else{
         return false;
      }
   }
}

   



