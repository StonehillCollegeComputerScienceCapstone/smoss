import java.util.Scanner;
public class Palindrome {

    public static void main(String args[]){
        
        System.out.println("Enter a number : ");
        Scanner keyboard = new Scanner(System.in);
        int possiblePalindrome = 0; 
        possiblePalindrome = keyboard.nextInt();
        
        
        if(isPalindrome(possiblePalindrome)){
            System.out.println(possiblePalindrome + " is a palindrome");
        }else{
            System.out.println(possiblePalindrome + " is not a palindrome");
        }       
        
    }
  
    public static boolean isPalindrome(int number) {
        int possiblePalindrome = number; 
        int reversed = 0;

        while (possiblePalindrome != 0) {
            int remainder = possiblePalindrome % 10;
            reversed = reversed * 10 + remainder;
            possiblePalindrome = possiblePalindrome / 10;
        }
        if (number == reversed) {
            return true;
        }
        return false;
        
    }

}//end class


