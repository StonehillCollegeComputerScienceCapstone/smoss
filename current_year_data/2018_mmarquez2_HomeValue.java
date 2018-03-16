import java.util.Scanner;
public class HomeValue
{
    public static void main(String[] args)
    {
        int again = 1;
        while(again == 1)
        {
            Scanner keyboard = new Scanner(System.in);
            System.out.println("Length of Investment (between 1 and 6 inclusive): ");
            double length = keyboard.nextDouble();
            System.out.println("Enter Percent Increase or Decrease for each year: ");
            if(length == 1)
            {
                double percentOne = keyboard.nextDouble();
                double geometricMean = (percentOne/100) + 1;
                System.out.println("The geometric mean is: " + geometricMean);
            }
            else if(length == 2)
            {
                double percentOne = keyboard.nextDouble();
                double percentTwo = keyboard.nextDouble();
                geometricMean(percentOne, percentTwo);
            }
            else if(length == 3)
            {
                double percentOne = keyboard.nextDouble();
                double percentTwo = keyboard.nextDouble();
                double percentThree = keyboard.nextDouble();
                geometricMean(percentOne, percentTwo, percentThree);
            }
            else if(length == 4)
            {
                double percentOne = keyboard.nextDouble();
                double percentTwo = keyboard.nextDouble();
                double percentThree = keyboard.nextDouble();
                double percentFour = keyboard.nextDouble();
                geometricMean(percentOne, percentTwo, percentThree, percentFour);
            }
            else if(length == 5)
            {
                double percentOne = keyboard.nextDouble();
                double percentTwo = keyboard.nextDouble();
                double percentThree = keyboard.nextDouble();
                double percentFour = keyboard.nextDouble();
                double percentFive = keyboard.nextDouble();
                geometricMean(percentOne, percentTwo, percentThree, percentFour,percentFive);
            }
            else if(length == 6)
            {
                double percentOne = keyboard.nextDouble();
                double percentTwo = keyboard.nextDouble();
                double percentThree = keyboard.nextDouble();
                double percentFour = keyboard.nextDouble();
                double percentFive = keyboard.nextDouble();
                double percentSix = keyboard.nextDouble();
                geometricMean(percentOne, percentTwo, percentThree, percentFour,percentFive, percentSix);
            }
            System.out.println("Run Again? (1 for yes): ");
            again = keyboard.nextInt();
        }



    }//end main
    public static void geometricMean(double a, double b)
    {
        double geometricMean = Math.pow((((a/100) + 1)) *(((b/100) + 1)), 0.5);
        System.out.println("The geometric mean is: " + geometricMean);

    }
    public static void geometricMean(double a, double b, double c)
    {
        double geometricMean = Math.pow((((a/100) + 1) *((b/100) + 1) * ((c/100) + 1)), 0.333);
        System.out.println("The geometric mean is: " + geometricMean);

    }
    public static void geometricMean(double a, double b, double c, double d)
    {
        double geometricMean = Math.pow((((a/100) + 1)) *(((b/100) + 1)) * (((c/100) + 1)) * (((d/100) + 1)), 0.25);
        System.out.println("The geometric mean is: " + geometricMean);

    }
    public static void geometricMean(double a, double b, double c, double d, double e)
    {
        double geometricMean = Math.pow((((a/100) + 1)) *(((b/100) + 1)) * (((c/100) + 1)) * (((d/100) + 1)) * (((e/100) + 1)), 0.2);
        System.out.println("The geometric mean is: " + geometricMean);

    }
    public static void geometricMean(double a, double b, double c, double d, double e, double f)
    {
        double geometricMean = Math.pow((((a/100) + 1)) *(((b/100) + 1)) * (((c/100) + 1)) * (((d/100) + 1)) * (((e/100) + 1)) * (((f/100) + 1)), 0.1666);
        System.out.println("The geometric mean is: " + geometricMean);

    }
}//end class
