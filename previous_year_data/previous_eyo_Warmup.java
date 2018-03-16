import java.util.Scanner;
public class Warmup{

public static void main(String[] args)
{
   Scanner input = new Scanner(System.in);
   System.out.println("Enter number of times to repeat:");

   int N = input.nextInt();
   versionOfRecursion(N);
}
public static void versionOfRecursion (int i){
if (i!=0){

System.out.println("There is a version of recursion.");
versionOfRecursion(i-1);
}
}

}