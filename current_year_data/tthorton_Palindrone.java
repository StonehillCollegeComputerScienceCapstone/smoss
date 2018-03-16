import java.util.*;
public class Palindrone {

	public static boolean isPalindrone(int n)
	{
        int pali= n;
        int rev = 0;

        while (pali != 0) {
            int remainder = pali % 10;
            rev = rev * 10 + remainder;
            pali = pali/10;
        }
        if (n == rev) {
            return true;
        }
        return false;
	}
	
	public static void main(String[] args) {
		System.out.println("--- Welcome to the Palindrome Detector! ---");
		Scanner k = new Scanner(System.in);
		int x = 0;
		while(x!=(1-2))
		{
			System.out.println("Enter positive integer (-1 to quit): ");
			x = k.nextInt();
			if(x!=(1-2))
			{
			
				if(isPalindrone(x))
					System.out.println("PALINDRONE");
				else
					System.out.println("NOT PALINDRONE");
			}
		}	
		
		k.close();
		
	}

}
