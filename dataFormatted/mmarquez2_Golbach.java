import java.util.Scanner;
public class Golbach
{
    public static void main(String[] args)
    {
        int again = 1;
        while (again == 1)
        {
            int posInt = 0;
            while (posInt <= 2 || posInt % 2 != 0)
            {
                Scanner keyboard = new Scanner(System.in);
                System.out.println("Enter an even positive integer greater than 2: ");
                posInt = keyboard.nextInt();
            }
            goldbach(posInt);
            Scanner keyboard = new Scanner(System.in);
            System.out.println("Again? 1 for yes: ");
            again = keyboard.nextInt();

        }



    }//end main
    public static void goldbach(int n)
    {


        for(int i = 1; i <= n/2; ++i )
        {
            if(isPrime(i) && isPrime(n - i) )
            {
                System.out.println(n + "=" + i + "+" + (n - i));
                break;

            }


        }

    }//end method
    public static boolean isPrime(int n)
    {
        boolean primeNum = true;
        if(n <= 1)
            return false;
        if(n == 2)
            return true;
        for(int i = 2; i < Math.sqrt(n) + 1; ++i)
        {
            if(n % i == 0)
                return false;
        }
        return true;

    }//end method
}//end class
