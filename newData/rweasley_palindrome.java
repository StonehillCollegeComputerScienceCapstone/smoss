import java.util.Scanner;

public class JavaProgram
{
    public static void main(String args[])
    {
        int num, rem, orig, rev=0;
        Scanner scan = new Scanner(System.in);
  
        System.out.print("Enter a Number : ");
        num = scan.nextInt();
  
        orig = num;
  
        while(num != 0)
        {
            rem = num%10;
            rev = rev*10 + rem;
            num = num/10;
        }
        
        // check if the original number is equal to its reverse
        
        if(rev==orig)
        {
            System.out.print("This is a Palindrome Number");
        }
        else
        {
            System.out.print("This is not a Palindrome Number");
        }
    }
}