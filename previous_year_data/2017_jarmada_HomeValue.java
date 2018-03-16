import java.util.Scanner;
public class HomeValue
{

public static void main(String[] args)
{
int again=1;
do
{
double percent1, percent2, percent3, percent4, percent5, percent6, mean =1;
int years;
Scanner keyboard = new Scanner(System.in);
System.out.println("How many years are you investing? Please enter 1-6");
years = keyboard.nextInt();

switch(years)
{
case 1:
System.out.println("What is the percentage increase or decrease for that year? ex 0.2 for 20%, -.09 for -9%");
percent1 = keyboard.nextDouble()+1;
System.out.println("The home's value after 1 year is " + (300000* percent1));
break;
case 2:
System.out.println("What are the percentage increase or decrease for those years? ex 0.2 for 20%, -.09 for -9%");
percent1 = keyboard.nextDouble()+1;
percent2 = keyboard.nextDouble()+1;
double result2 = (300000* geometricMean(percent1, percent2));
System.out.printf("The home's value after 2 years is %1.2f" , result2);
break;
case 3:
System.out.println("What are the percentage increase or decrease for those years? ex 0.2 for 20%, -.09 for -9%");
percent1 = keyboard.nextDouble()+1;
percent2 = keyboard.nextDouble()+1;
percent3 = keyboard.nextDouble()+1;
double result3 = (300000* geometricMean(percent1, percent2, percent3));
System.out.printf("The home's value after 3 years is %1.2f" , result3);
break;
case 4:
System.out.println("What are the percentage increase or decrease for those years? ex 0.2 for 20%, -.09 for -9%");
percent1 = keyboard.nextDouble()+1;
percent2 = keyboard.nextDouble()+1;
percent3 = keyboard.nextDouble()+1;
percent4 = keyboard.nextDouble()+1;
double result4 = (300000* geometricMean(percent1, percent2, percent3, percent4));
System.out.printf("The home's value after 4 years is %1.2f" , result4);
break;
case 5:
System.out.println("What are the percentage increase or decrease for those years? ex 0.2 for 20%, -.09 for -9%");
percent1 = keyboard.nextDouble()+1;
percent2 = keyboard.nextDouble()+1;
percent3 = keyboard.nextDouble()+1;
percent4 = keyboard.nextDouble()+1;
percent5 = keyboard.nextDouble()+1;
double result5 = (300000* geometricMean(percent1, percent2, percent3, percent4, percent5));
System.out.printf("The home's value after 5 years is %1.2f" , result5);
break;
case 6:
System.out.println("What are the percentage increase or decrease for those years? ex 0.2 for 20%, -.09 for -9%");
percent1 = keyboard.nextDouble()+1;
percent2 = keyboard.nextDouble()+1;
percent3 = keyboard.nextDouble()+1;
percent4 = keyboard.nextDouble()+1;
percent5 = keyboard.nextDouble()+1;
percent6 = keyboard.nextDouble()+1;
double result6 = (300000* geometricMean(percent1, percent2, percent3, percent4, percent5, percent6));
System.out.printf("The home's value after 6 years is %1.2f" , result6);
break;
}

System.out.println("\nWant to enter again? 1 for yes");
again = keyboard.nextInt();
}while(again ==1);
}//end main


public static double geometricMean(double p1, double p2)
{
double mean, exp = 1.0/2.0;
mean = Math.pow((p1*p2),exp); 
return mean;
}//end method

public static double geometricMean(double p1, double p2, double p3)
{
double mean, exp = 1.0/3.0;
mean = Math.pow((p1*p2*p3),exp); 
return mean;
}//end method

public static double geometricMean(double p1, double p2, double p3, double p4)
{
double mean, exp = 1.0/4.0;
mean = Math.pow((p1*p2*p3*p4),exp); 
return mean;
}//end method

public static double geometricMean(double p1, double p2, double p3, double p4, double p5)
{
double mean, exp = 1.0/5.0;
mean = Math.pow((p1*p2*p3*p4*p5),exp); 
return mean;
}//end method

public static double geometricMean(double p1, double p2, double p3, double p4, double p5, double p6)
{
double mean, exp = 1.0/6.0;
mean = Math.pow((p1*p2*p3*p4*p5*p6),exp); 
return mean;
}//end method
}//end class