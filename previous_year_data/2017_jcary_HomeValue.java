import java.util.Scanner;
import java.util.*;
public class HomeValue
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Enter the amount of years of the investment.");
   int years = keyboard.nextInt();  
    int x, y, z, i, j, k;
    if(years == 2)
    {
      System.out.println("Please enter the percent annual increase or decrease");
      x = keyboard.nextInt();
      y = keyboard.nextInt();
      System.out.println("The average annual increase or decrease is  " + geometricMean2(x, y));
    }
    else  if(years == 3)
    {
      System.out.println("Please enter the percent annual increase or decrease");
      x = keyboard.nextInt();
      y = keyboard.nextInt();
      z = keyboard.nextInt();
      System.out.println("The average annual increase or decrease is  " + geometricMean3(x, y, z));
    }
     else  if(years == 4)
    {
      System.out.println("Please enter the percent annual increase or decrease");
      x = keyboard.nextInt();
      y = keyboard.nextInt();
      z = keyboard.nextInt();
      i = keyboard.nextInt();
      System.out.println("The average annual increase or decrease is  " + geometricMean4(x, y, z, i));
    }
      else  if(years == 5)
    {
      System.out.println("Please enter the percent annual increase or decrease");
      x = keyboard.nextInt();
      y = keyboard.nextInt();
      z = keyboard.nextInt();
      i = keyboard.nextInt();
      j = keyboard.nextInt();
      System.out.println("The average annual increase or decrease is  " + geometricMean5(x, y, z, i, j));
    }
       else  if(years == 6)
    {
      System.out.println("Please enter the percent annual increase or decrease");
      x = keyboard.nextInt();
      y = keyboard.nextInt();
      z = keyboard.nextInt();
      i = keyboard.nextInt();
      j = keyboard.nextInt();
      k = keyboard.nextInt();
      System.out.println("The average annual increase or decrease is  " + geometricMean6(x, y, z, i, j, k));
    }
  
  }//end main
  
  public static double toDecimal(double n)
  {
    double i;
  if(n<0)
  {
    i = 1+ (n/100);
  }
  else 
    i = 1+(n/100);
  
  return i;
  }
  
  public static double geometricMean2(int x, int y)
  {
    double mean;
    mean = toDecimal(x) * toDecimal(y);
    mean = power(mean, 0.5);
    return mean;
  }
  public static double geometricMean3(int x, int y, int z)
  {
    double mean;
    mean = toDecimal(x) * toDecimal(y) * toDecimal(z);
    mean = power(mean, 0.33333);
    return mean;
  }
  public static double geometricMean4(int x, int y, int z, int i)
  {
      double mean;
    mean = toDecimal(x) * toDecimal(y) * toDecimal(z) * toDecimal(i);
    mean = power(mean, 0.25);
    return mean;
  }
  public static double geometricMean5(int x, int y, int z, int i, int j)
  {
       double mean;
    mean = toDecimal(x) * toDecimal(y) * toDecimal(z) * toDecimal(i) * toDecimal(j);
    mean = power(mean, 0.2);
    return mean;
  }
  public static double geometricMean6(int x, int y, int z, int i, int j, int k)
  {
     double mean;
    mean = toDecimal(x) * toDecimal(y) * toDecimal(z) * toDecimal(i) * toDecimal(j) * toDecimal(k);
    mean = power(mean, 0.166666);
    return mean;  
  }

  public static double power(double x, double y)
  {
  double mean;
  mean = Math.pow(x, y);
  return mean;
  }
  
  
  
  
  
  
  
  
  
}//end class