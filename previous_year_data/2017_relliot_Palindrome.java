import java.util.Scanner;
public class Palindrome
{
public static void main(String[] args)
{
int B = 0;
do
{
System.out.println("Welcome to the Palindrome Detector!");
System.out.println("Enter positive integer (-1 to quit):");
Scanner input = new Scanner(System.in);
int n = input.nextInt();

String N = Integer.toString(n);

//Math.pow

//reverse and compare

String reverse = "";
for(int i = N.length() - 1; i >= 0; --i)
{
reverse = reverse + N.charAt(i);

}
if(reverse.equals(N))
System.out.println("Palindrome");
else
System.out.println("Not palindrome");

System.out.println("Again? -1 to quit:");
B = input.nextInt(); 
}while(B != -1);

}//end main

}