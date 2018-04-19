// java program for palindrome
// taken from https://examples.javacodegeeks.com/core-java/palindrome-program-in-java/
// author:  Nikos Maravitsas

package com.javacodegeeks.core.palindrome;

public class PalindromeExample {

    private static final String STR1 = "abbcbba";
    private static final String STR2 = "isdovosjd";
    public static void main(String[] args) {
        System.out.println("String :"+STR1+" is a palindrome :"+PalindromeExample.isPalindrome(STR1));
        System.out.println("String :"+STR2+" is a palindrome :"+PalindromeExample.isPalindrome(STR2));
    }
    public static boolean isPalindrome(String str){
        String reverse = new StringBuffer(str).reverse().toString();
        if (reverse.equals(str))
            return true;
        return false;
}

}
