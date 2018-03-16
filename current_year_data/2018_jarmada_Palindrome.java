import java.util.Scanner;
public class Palindrome
{
public static void main(String[] args)
{
System.out.println("Welcome to the palindrome detector!");
int num;
do
{

Scanner keyboard = new Scanner(System.in);
System.out.println("Please enter a positive integer -1 to quit");
num = keyboard.nextInt();


int reverse = isPalindrome(num);
System.out.println(reverse);

if(num == reverse)
System.out.println("Palindrome");

else
System.out.println("Not Palindrome");

}while (num <=0 && num != -1);

}//end main



public static int isPalindrome(int x)
{
String a = Integer.toString(x);
int length = a.length();
//System.out.println(length);
int reverse =0;
for(int i=1; i<=length; ++i)
{
int b = length -i;
//System.out.println(b);
int z= x/((int)Math.pow(10, b));
//System.out.println(z);
int w= z%10;
//System.out.println(w);
int q = (int)Math.pow(10, i-1);
int y= w*q;
//System.out.println(y);
reverse = reverse + y;
}//end for loop
return reverse;
}//end method
}//end main
