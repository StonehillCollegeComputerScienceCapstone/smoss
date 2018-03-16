import java.util.*;

public class CarnivalGame {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int wins = 0;
        for (int i = 0; i < 100; i++) {
            int total = dieRoll(6) + dieRoll(4) + dieRoll(12) + dieRoll(8) + dieRoll(20);
            if (total < 20 || total > 35) {
                wins += 1;
            }
        }
        System.out.println(wins + " wins.");
    }

    public static int dieRoll(int x) {
        return (int) ((Math.random() * x) + 1);
    }
}
