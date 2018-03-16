import java.util.Scanner;
public class HomeValue
{

public static void main(String[] args)
  {
  
  Scanner keyboard = new Scanner(System.in);
  
  int valueOfHome = 300000,p1=0 ,p2=0 ,p3=0 ,p4=0 ,p5= 0,p6= 0;
  
    
  System.out.println("How long is the investment(1-6 years)");
  int lengthOfInvestment = keyboard.nextInt();
  
  
  if(lengthOfInvestment >=1 ){
  System.out.println("What is the percent increase or decrease for the 1st year: ");
  p1=keyboard.nextInt();
  geometricMean(p1);
  double numberMean = geometricMean((int)p1);
  System.out.println(numberMean);
  percentDifference(numberMean);
  }
  
  if(lengthOfInvestment >=2 ){
  System.out.println("What is the percent increase or decrease for the 2nd year: ");
  p2=keyboard.nextInt(); 
  double numberMean = geometricMean((double)p1, (double)p2);
  System.out.println(numberMean);
  percentDifference(numberMean);
  
  }
  
  if(lengthOfInvestment >=3 ){
  System.out.println("What is the percent increase or decrease for the 3rd year: ");
  p3=keyboard.nextInt();
  geometricMean(p1, p2, p3);
  double numberMean = geometricMean((double)p1, (double)p2,(double)p3 );
  System.out.println(numberMean);
  percentDifference(numberMean);
  
  }
  if(lengthOfInvestment >=4) {
  System.out.println("What is the percent increase or decrease for the 4th year: ");
  p4=keyboard.nextInt();
  geometricMean(p1, p2, p3, p4);
  double numberMean = geometricMean((double)p1, (double)p2,(double)p3,(double)p4 );
  System.out.println(numberMean);
  percentDifference(numberMean);
  }
  if(lengthOfInvestment >=5){
  System.out.println("What is the percent increase or decrease for the 5th year: ");
  p5=keyboard.nextInt();
  geometricMean(p1, p2, p3, p4, p5);
  double numberMean = geometricMean((double)p1, (double)p2,(double)p3,(double)p4,(double)p5 );
  System.out.println(numberMean);
  percentDifference(numberMean);
  }
  if(lengthOfInvestment >=6){
  System.out.println("What is the percent increase or decrease for the 6th year: ");
  p6=keyboard.nextInt();  
  geometricMean(p1, p2, p3, p4, p5,p6);
  double numberMean = geometricMean((double)p1, (double)p2,(double)p3,(double)p4,(double)p5,(double)p6 );
  System.out.println(numberMean);
  percentDifference(numberMean);
  }
 }
  public static double geometricMean(int p1)
  {
  double sum1=0;
  sum1 = 300000+(1+(p1/100)*300000);
    return(sum1);

  }
  public static double geometricMean(double p1, double p2)
 {
 double sum2=0;
   sum2 = (1+(p1/100))*(1+(p2/100));
   return Math.pow(sum2, (double)1/2);
   //sum2 = (Math.pow((1+(p1/100)*1+(p2/100)),(double)(1/2)));
    //return (sum2);
   

  }
   public static double geometricMean(double p1, double p2, double p3)
 {
 double sum3=0;
   sum3 = (1+(p1/100))*(1+(p2/100))*(1+(p3/100));
   return Math.pow(sum3, (double)1/3);
   //sum3 = (Math.pow(1+(p1/100)*1+(p2/100)*1+(p3/100),(double)(1/3)));
    //return(300000 * (3*sum3));

  }
  public static double geometricMean(double p1, double p2, double p3, double p4)
 {
 double sum4=0;
   sum4 = (1+(p1/100))*(1+(p2/100))*(1+(p3/100))*(1+(p4/100));
   return Math.pow(sum4, (double)1/4);
   //sum4 = (Math.pow(1+(p1/100)*1+(p2/100)*1+(p3/100)*1+(p4/100),(double)(1/4)));
   // return(300000 * (4*sum4));

  }
    public static double geometricMean(double p1, double p2, double p3, double p4, double p5)
 {
 double sum5=0;
 sum5 = (1+(p1/100))*(1+(p2/100))*(1+(p3/100))*(1+(p4/100))*(1+(p5/100));
   return Math.pow(sum5, (double)1/5);
 
  // sum5 = (Math.pow(1+(p1/100)*1+(p2/100)*1+(p3/100)*1+(p4/100)*1+(p5/100),(double)(1/5)));
  //  return(300000 * (5*sum5));

  }
  public static double geometricMean(double p1, double p2, double p3, double p4, double p5, double p6)
 {
 double sum6=0;
  sum6 = (1+(p1/100))*(1+(p2/100))*(1+(p3/100))*(1+(p4/100))*(1+(p5/100))*(1+(p6/100));
   return Math.pow(sum6, (double)1/6);
  
  // sum6 = (Math.pow(1+(p1/100)*1+(p2/100)*1+(p3/100)*1+(p4/100)*1+(p5/100)*1+(p6/100),(double)(1/6)));
  //  return(300000 * (6*sum6));

  }

public static void percentDifference(double m){
if(m>1)
System.out.println((m-1)*100 + " = PERCENT INCREASE");
else if (m<1)
System.out.println(((1-m)*100)+ " = PERCENT DECREASE");


}
 
  

   















}//end class
