import java.util.Scanner;
public class HomeValue
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    int years;
    double price = 300000, finalPrice;
    
    System.out.println("Enter the number of years that the investment is held, from 1 to 6 years: ");
    years = keyboard.nextInt();
    
    if(years == 1)
    {
      double change1;
      System.out.println("Enter the annual change after 1 year: ");
      change1 = keyboard.nextDouble();
      finalPrice = price * change1;
      System.out.println("$" + finalPrice);
    }
    if(years == 2)
    {
      double change1, change2, gM;
      System.out.println("Enter the annual change after 1 year: ");
      change1 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 2 years: ");
      change2 = keyboard.nextDouble();
      
      gM = geometricMean(change1, change2);
      finalPrice = (gM * gM) * price;
      System.out.println("$" + finalPrice);
    }
    if(years == 3)
    {
      double change1, change2, change3, gM;
      System.out.println("Enter the annual change after 1 year: ");
      change1 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 2 years: ");
      change2 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 3 years: ");
      change3 = keyboard.nextDouble();
      
      gM = geometricMean(change1, change2, change3);
      finalPrice = (gM * gM * gM) * price;
      System.out.println("$" + finalPrice);
    }
    if(years == 4)
    {
      double change1, change2, change3, change4, gM;
      System.out.println("Enter the annual change after 1 year: ");
      change1 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 2 years: ");
      change2 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 3 years: ");
      change3 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 4 years: ");
      change4 = keyboard.nextDouble();
      
       gM = geometricMean(change1, change2, change3, change4);
      finalPrice = (gM * gM * gM * gM) * price;
      System.out.println("$" + finalPrice);
    }
    if(years == 5)
    {
      double change1, change2, change3, change4, change5, gM;
      System.out.println("Enter the annual change after 1 year: ");
      change1 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 2 years: ");
      change2 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 3 years: ");
      change3 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 4 years: ");
      change4 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 5 years: ");
      change5 = keyboard.nextDouble();
      
      gM = geometricMean(change1, change2, change3, change4, change5);
      finalPrice = (gM * gM * gM * gM * gM) * price;
      System.out.println("$" + finalPrice);
    }
    if(years == 6)
    {
      double change1, change2, change3, change4, change5, change6, gM;
      System.out.println("Enter the annual change after 1 year: ");
      change1 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 2 years: ");
      change2 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 3 years: ");
      change3 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 4 years: ");
      change4 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 5 years: ");
      change5 = keyboard.nextDouble();
      System.out.println("Enter the annual change after 6 years: ");
      change6 = keyboard.nextDouble();
      
      gM = geometricMean(change1, change2, change3, change4, change5, change6);
      finalPrice = (gM * gM * gM * gM * gM * gM) * price;
      System.out.println("$" + finalPrice);
    }
    
  }//end main
  
  public static double geometricMean(double a, double b)
  {
   double changes, gMean;
   changes = (a * b);
   gMean = Math.pow(changes, (double)1/2);
    return gMean;
  }
  
  public static double geometricMean(double a, double b, double c)
  {
   double changes, gMean;
   changes = (a * b * c);
   gMean = Math.pow(changes, (double)1/3);
    return gMean;
  }
  
  public static double geometricMean(double a, double b, double c, double d)
  {
   double changes, gMean;
   changes = (a * b * c * d);
   gMean = Math.pow(changes, (double)1/4);
    return gMean;
  }
  
  public static double geometricMean(double a, double b, double c, double d, double e)
  {
   double changes, gMean;
   changes = (a * b * c * d * e);
   gMean = Math.pow(changes, (double)1/5);
    return gMean;
  }
  
  public static double geometricMean(double a, double b, double c, double d, double e, double f)
  {
   double changes, gMean;
   changes = (a * b * c * d * e * f);
   gMean = Math.pow(changes, (double)1/6);
    return gMean;
  }
}//end class