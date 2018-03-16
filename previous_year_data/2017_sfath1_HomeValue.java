import java.util.*;

public class HomeValue {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int investLen = 0;
        while (true) {
            while (true) {
                System.out.print("Length of time for the investment: ");
                investLen = s.nextInt();
                if (investLen >= 1 && investLen <= 6) {
                    break;
                }
            }
            double[] percents = new double[investLen];
            for (int i = 1; i <= investLen; i++) {
                System.out.print("Percent increase (- for deacrease) for year " + i + ": ");
                percents[i - 1] = s.nextDouble();
            }
            geometricMean(percents);
            System.out.print("\nAgain? (1 for yes): ");
            if (s.nextInt() != 1) {
                break;
            }
        }
    }

    public static void geometricMean(double[] percentsTest) {
        double multiplied = 1;
        for (int i = 0; i < percentsTest.length; i++) {
            multiplied = multiplied * (1 + (percentsTest[i] / 100));
        }
        double geoMean = Math.pow(multiplied, (1.0/percentsTest.length));
        geoMean = (geoMean - 1) * 100;
        System.out.println("Average change: " + geoMean + "%");
    }
}
