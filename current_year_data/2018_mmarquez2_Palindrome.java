import java.util.Scanner;
public class Palindrome
{
    public static void main(String[] args)
    {
        int posInt = 0;
        System.out.println("--- Welcome to the Palindrome Detector! ---");

        while(posInt != -1)
        {
            Scanner keyboard = new Scanner(System.in);
            System.out.println("Enter positive integer (-1 to quit): ");
            posInt = keyboard.nextInt();
            if(posInt != -1)
            {
                isPalindrome(posInt);
            }
            else
                System.out.println("A Santa spits tips at NASA... bye!");
        }





    }//end main
    public static boolean isPalindrome(int n)
    {
       String j = Integer.toString(n);
       String reverse = "";
        for(int i = j.length() - 1; i >= 0; --i)
        {
            reverse = reverse + j.charAt(i);
        }
        if(reverse.equals(j))
        {
            System.out.println("Palindrome");
            return true;
        }
        else
        {
            System.out.println("Not Palindrome");
            return false;
        }

    }//end method

}//end class
