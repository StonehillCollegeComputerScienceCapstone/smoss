import java.util.Scanner;
public class Warmup
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number of times to repeat:");

        int N = input.nextInt();
        versionOfRecursion(N);

    }//end main

    public static void versionOfRecursion(int N)
    {
        if(N != 0)
        {
            System.out.println("This is a version of recursion");
            versionOfRecursion(N-1);
        }

    }
}//end class