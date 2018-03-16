import java.util.Scanner;

public class HomeValue
{
public static void main(String[] args)
  {
  Scanner keyboard= new Scanner(System.in);
  
  int time, again;
  double total;
  
   do
  {
    
  System.out.println("Enter the length of time of the investment(1-6): ");
  time= keyboard.nextInt();
  
  
  if(time == 1)
  {
  double yearOne;  
  System.out.println("Enter the length of time of the investment(1-6): ");
  yearOne= keyboard.nextDouble();  
  if(yearOne<0)
  {
    yearOne= 1- (yearOne/100);
  }
   if(yearOne>=0)
  {
    yearOne= 1 + (yearOne/100);
  }  
   
   System.out.println("Average change in real estate investment: " + yearOne);
  }
  
  if(time==2)
  {
  double yearOne, yearTwo;  
  System.out.println("Enter the percent increase or decrease for each year: ");
  yearOne= keyboard.nextDouble();
  yearTwo=keyboard.nextDouble();
  total= geometricMean(yearOne, yearTwo);
  System.out.println("Average change in real estate investment: " + total);
  }
  
  if(time==3)
  {
  double yearOne, yearTwo, yearThree;  
  System.out.println("Enter the percent increase or decrease for each year: ");
  yearOne= keyboard.nextDouble();
  yearTwo=keyboard.nextDouble();
  yearThree=keyboard.nextDouble();
  total= geometricMean(yearOne, yearTwo, yearThree);
  System.out.println("Average change in real estate investment: " + total);
  }
  
  if(time==4)
  {
  double yearOne, yearTwo,yearThree, yearFour;  
  System.out.println("Enter the percent increase or decrease for each year: ");
  yearOne= keyboard.nextDouble();
  yearTwo=keyboard.nextDouble();
  yearThree=keyboard.nextDouble();
  yearFour=keyboard.nextDouble();
  total= geometricMean(yearOne, yearTwo, yearThree, yearFour);
  System.out.println("Average change in real estate investment: " + total);
  }
  
  if(time==5)
  {
  double yearOne, yearTwo,yearThree, yearFour, yearFive;  
  System.out.println("Enter the percent increase or decrease for each year: ");
  yearOne= keyboard.nextDouble();
  yearTwo=keyboard.nextDouble();
  yearThree=keyboard.nextDouble();
  yearFour=keyboard.nextDouble();
  yearFive=keyboard.nextDouble();
  total= geometricMean(yearOne, yearTwo, yearThree, yearFour, yearFive);
  System.out.println("Average change in real estate investment: " + total);
  }
  
  if(time==6)
  {
  double yearOne, yearTwo,yearThree, yearFour, yearFive, yearSix;  
  System.out.println("Enter the percent increase or decrease for each year: ");
  yearOne= keyboard.nextDouble();
  yearTwo=keyboard.nextDouble();
  yearThree=keyboard.nextDouble();
  yearFour=keyboard.nextDouble();
  yearFive=keyboard.nextDouble();
  yearSix=keyboard.nextDouble();
  total= geometricMean(yearOne, yearTwo, yearThree, yearFour, yearFive, yearSix);
  System.out.println("Average change in real estate investment: " + total);
  }
    
  System.out.println("To run again type 1:");
    again= keyboard.nextInt();
  }while(again==1);
     
     
 
  }//end main



public static double geometricMean(double a, double b)
{
double total,mean;
  if(a<0)
    {
     a= 1- (a/100);
    }
  if(b<0)
    {
     b= 1- (b/100);
    }
   if(a>=0)
    {
     a= 1 + (a/100);
    }
   if(b>=0)
    {
      b= 1 + (b/100);
    }
total= a*b;   
mean= Math.pow(total,(.5));
return mean;  
}//end method

public static double geometricMean(double a, double b, double c)
{
double total,mean;
if(a<0)
    {
     a= 1- (a/100);
    }
if(a>=0)
    {
     a= 1 + (a/100);  
    }
if(b<0)
    {
     b= 1- (b/100);
    }
if(b>=0)
    {
      b= 1 + (b/100);
    }
if(c<0)
    {
     c= 1- (c/100);
    }
if(c>=0)
    {
      c= 1 + (c/100);
    }
total= a*b*c;  
mean= Math.pow(total,(.3333));
return mean; 

}//end method

public  static double geometricMean(double a, double b, double c, double d)
{
double mean, total;
if(a<0)
    {
     a= 1- (a/100);
    }
if(a>=0)
    {
     a= 1 + (a/100); 
    }
if(b<0)
    {
     b= 1- (b/100);
    }
if(b>=0)
    {
      b= 1 + (b/100);
    }
if(c<0)
    {
     c= 1- (c/100);
    }
if(c>=0)
    {
      c= 1 + (c/100);
    }
if(d<0)
    {
     d= 1- (d/100);
    }
if(d>=0)
    {
      d= 1 + (d/100);
    }
total= a*b*c*d;   
mean= Math.pow(total,(.25));
return mean;
}//end method

public static double geometricMean(double a, double b, double c, double d, double e)
{
double total,mean;
if(a<0)
    {
     a= 1- (a/100);
    }
if(a>=0)
    {
     a= 1 + (a/100); 
    }
if(b<0)
    {
     b= 1- (b/100);
    }
if(b>=0)
    {
      b= 1 + (b/100);
    }
if(c<0)
    {
     c= 1- (c/100);
    }
if(c>=0)
    {
      c= 1 + (c/100);
    }
if(d<0)
    {
     d= 1- (d/100);
    }
if(d>=0)
    {
      d= 1 + (d/100);
    }
if(e<0)
    {
     e= 1- (e/100);
    }
if(e>=0)
    {
      e= 1 + (e/100);
    }
total= a*b*c*d*e;    
mean= Math.pow(total,(.2));
return mean;
}//end method


public static double geometricMean(double a, double b, double c, double d, double e, double f)
{
double total,mean; 
if(a<0)
    {
     a= 1- (a/100);
    }
if(a>=0)
    {
     a= 1 + (a/100);  
    }
if(b<0)
    {
     b= 1- (b/100);
    }
if(b>=0)
    {
      b= 1 + (b/100);
    }
if(c<0)
    {
     c= 1- (c/100);
    }
if(c>=0)
    {
      c= 1 + (c/100);
    }
if(d<0)
    {
     d= 1- (d/100);
    }
if(d>=0)
    {
      d= 1 + (d/100);
    }
if(e<0)
    {
     e= 1- (e/100);
    }
if(e>=0)
    {
      e= 1 + (e/100);
    }
if(f<0)
    {
     f= 1- (f/100);
    }
if(f>=0)
    {
      f= 1 + (f/100);
    }
total= a*b*c*d*e*f;  
mean= Math.pow(total,(.1667));  
return mean;
}//end method




}// end class