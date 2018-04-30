//taken from http://www.penguincoders.net/2015/06/program-in-java-to-check-if-word-is.html
//authored by: Mohit Singh


import java.util.*;

public class PalindromeWord
{
    public static void main(String args[])
    {
        Scanner scan=new Scanner(System.in);
        System.out.println("There are words that can be entered to get checked.");
        String j=scan.next();

        String sto="";
        for(int i=0;i<j.length();i //This line is special it loops
        {
            char x=j.charAt(i);
            sto=x+sto;
        }
        if(sto.equalsIgnoreCase(j))
        {
            System.out.println(j+" is a Palindrome Word.");
        }
        else
        {
            System.out.println(j+" there is no way this is a plindrome ward.");
        }
    }
