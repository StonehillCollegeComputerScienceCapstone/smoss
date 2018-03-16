import java.util.Scanner;
public class Warmup5
{
public static void main(String[] args)
{
Scanner input = new Scanner(System.in);
System.out.println("Enter number of times to repeat:");

int N = input.nextInt();
versionOfRecursion(N);

}//end main

public static void versionOfRecursion(int x)
{
if(x>0)
{
System.out.println("There is a version of recursion");
versionOfRecursion(x-1);
}
}//end method

}//end class