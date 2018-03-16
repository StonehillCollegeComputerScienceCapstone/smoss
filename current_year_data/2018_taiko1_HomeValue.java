import java.util.Scanner;
public class HomeValue
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    int length, count = 0; 
    double precentage;
    double z = 0, x = 0, c = 0, v = 0, b = 0, n = 0;
    double total = 0;
    System.out.println("Please enter the length of your investment, 1 - 6 years.");
    length = keyboard.nextInt();
    int check;

    do{    
if(length == 1)
{
z = getPrecentage();
total = (z *.01 + 1);
}
if(length == 2)
{
  z = getPrecentage();
  x = getPrecentage();
  total = geometricMean(z,x);
  }
if(length == 3)
{
  z = getPrecentage();
  x = getPrecentage();
  c = getPrecentage();
  total = geometricMean(z,x,c);
  }
if(length == 4)
{
  z = getPrecentage();
  x = getPrecentage();
  c = getPrecentage();
  v = getPrecentage();
  total = geometricMean(z,x,c,v);
  }
if(length == 5)
{
  z = getPrecentage();
  x = getPrecentage();
  c = getPrecentage();
  v = getPrecentage();
  b = getPrecentage();
  total = geometricMean(z,x,c,v,b);
  }
if(length == 6)
{
  z = getPrecentage();
  x = getPrecentage();
  c = getPrecentage();
  v = getPrecentage();
  b = getPrecentage();
  n = getPrecentage();
  total = geometricMean(z,x,c,v,b,n);
  }
System.out.printf("%1.4f", total);
System.out.println(" ");// line break
System.out.println("Press one to test another instance");
check = keyboard.nextInt();
}while (check != 1);
  }
  
  public static double getPrecentage()
  {
    Scanner keyboard = new Scanner(System.in);
    double t;
    System.out.println("Please enter the precent increase or decrease for each year.");
    t = keyboard.nextDouble();
 return t;   
  }//end GP
  
    public static double geometricMean(double a, double b )
  {
   double total = 0, y = 0;
  y = ((1 + a * .01) * (1 + b * .01)); 
  total = (Math.pow(y,(1.0/2.0)));
      return total;
  }//2
    public static double geometricMean(double a, double b, double c )
  {
   double total = 0, y = 0;
   y = ((1 +(a * .01)) *(1 +(b * .01)) * (1 +(c * .01))); 
      total = (Math.pow(y,(1.0/3.0)));
      return total;
  }//3
    public static double geometricMean(double a, double b, double c, double d)
  {
  double total = 0, y = 0;
  y = ((1 +(a * .01)) * (1 +(b * .01)) * (1 +(c * .01)) * (1 +(d * .01)));
       total = (Math.pow(y,(1.0/4.0)));
       return total;
  }//4
    public static double geometricMean(double a, double b, double c, double d, double e)
  {
  double total = 0, y = 0;
    y = ((1 +(a * .01)) *(1 +(b * .01)) * (1 +(c * .01)) * (1 +(d * .01)) * (1 +(e * .01)));
       total = (Math.pow(y,(1.0/5.0)));
       return total;
  }//5
    public static double geometricMean(double a, double b, double c, double d, double e, double f )
  {
  double total = 0, y = 0;
      y = ((1 +(a * .01)) *(1 +(b * .01)) * (1 +(c * .01)) * (1 +(d * .01)) * (1 +(e * .01)) * (1 +(f * .01)));
      total = (Math.pow(y,(1.0/6.0)));
      return total;
    }//6
  }//end class