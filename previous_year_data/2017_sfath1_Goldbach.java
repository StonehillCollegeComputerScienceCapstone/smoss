import java.util.*;

public class Goldbach {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        while (true) {
            while (true) {
                System.out.print("Enter an even positive integer greater than 2: ");
                int num = s.nextInt();
                if (num > 2 && num % 2 == 0) {
                    goldbach(num);
                    break;
                }
            }
            System.out.print("Again? 1 for yes: ");
            if (s.nextInt() != 1) {
                break;
            }
        }
    }

    public static void goldbach(int n) {
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                int m = n-i;
                if (isPrime(m)) {
                    System.out.println(n + " = " + i + " + " + m);
                    break;
                }
            }
        }
    }

    public static boolean isPrime(int n) {
        boolean prime = true;
        for (int i = 3; i < n; i++) {
            if (n % i == 0) {
                prime = false;
            }
        }
        return prime;
    }
}
