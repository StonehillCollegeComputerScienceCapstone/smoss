import java.util.Scanner;
public class Goldbach
{
  public static void main (String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    int again;
    do{
    int integer;
    boolean check;
    do
    {
    integer = getNum();
    check = (test(integer));
    }
    while(check != true);
    if (check == true)
      goldbach(integer);
    System.out.println("Press 1 to test again");
    again = keyboard.nextInt();
    }while (again == 1);
    
  }// main
  
public static int getNum ()
{
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Please enter a positive integer greater than 2");
    int n = keyboard.nextInt(); 
    return n;
}//end GN

public static boolean test (int x)
{
  if (x % 2 == 0 && x > 1)
  return true;
  else
    return false;
}//end T
public static boolean isPrime(int n)
{
  if(n==1)
    return false;
    for(int i=2;i<n;i++) 
    {
        if(n%i==0)
        return false;
    }
    return true;
}// end IP

public static void goldbach(int n)
{
  int y;
for(int i=2; i < n; ++i)
{
  y = (n - i);
  if (isPrime(y) == true && isPrime(i) == true && y > i)
    System.out.println(n + " = " + y + " + " + i);
} 
}// end GB

}// end class