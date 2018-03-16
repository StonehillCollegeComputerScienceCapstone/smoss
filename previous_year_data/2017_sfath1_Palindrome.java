import java.util.*;

public class Palindrome {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("--- Welcome to the Palindrome Detector! ---");
        while (true) {
            System.out.print("Enter positive integer (-1 to quit): ");
            int num = s.nextInt();
            if (num == -1) {
                System.out.println("A Santa spits tips at NASA... bye!");
                break;
            } else {
                if (isPalindrome(num)) {
                    System.out.println("PALINDROME\n");
                } else {
                    System.out.println("NOT PALINDROME\n");
                }
            }
        }
    }

    public static boolean isPalindrome(int numTest) {
        boolean trueFalse = true;
        String stringNum = Integer.toString(numTest);
        char[] charArray = stringNum.toCharArray();
        for (int i = 0; i < (charArray.length/2); i++) {
            if (charArray[i] != charArray[charArray.length-1-i]) {
                trueFalse = false;
            }
        }
        return trueFalse;
    }
}
