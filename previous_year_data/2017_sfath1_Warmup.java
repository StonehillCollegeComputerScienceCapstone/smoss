import java.util.*;

public class Warmup {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number of times to repeat: ");
        int n = input.nextInt();
        versionOfRecursion(n);
    }

    public static void versionOfRecursion(int repeat) {
        for (int i = 0; i < repeat; i++) {
            System.out.println("There is a version of recursion.");
        }
    }
}
