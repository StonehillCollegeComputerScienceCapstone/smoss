////taken from http:////www.penguincoders.net/2015/06/program-in-java-to-check-if-word-is.html
////authored by: Mohit Singh


import java.util.*;
public class PalindromeWord
{
    public static void main(String args[])
    {
        Scanner ob=new Scanner(System.in);
        System.out.println("Enter the word to be checked.");
        String m=ob.next();

        String go="";
        for(int i=0;i<m.length();i////Loop for reversing the string.
        {
            char x=m.charAt(i);
            go=x+go;
        }
        if(go.equalsIgnoreCase(m))
        {
            System.out.println(m+" is m Palindrome Word.");
        }
        else
        {
            System.out.println(m+" is not m Palindrome Word.");
        }
         public static boolean isPalindrome(int n)
  {
    int m=1;
    int add=0;
    do
    {
      m=m*10;
      add++;
    }while(m<n);
    m=m/10; 
    
    int ten=1;
    int num=1;
    int total=0;
    int space=1;
    
    do
    {
      space = n/m;
      num= space%10;
      total=total+num*ten;
      m=m/10;
      ten=ten*10;

    }while(m>0); ////once m is less than 0 it stops because it would be undefined
    
    if (n==total)
    {
    return true;
    }
    else
    {
      return false;
    }
  }
    }