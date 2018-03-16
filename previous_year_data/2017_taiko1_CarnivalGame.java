import java.util.Random;
import java.util.Scanner;
public class CarnivalGame
{
  public static void main(String[] args)
  {
   int sum, die20 = 0, die12 = 0, die8 = 0, die6 = 0, die4 = 0, wins= 0, losses = 0, count = 0;
   // 20 12 6 8 4
   do
   {
   die20 = dieRol(20);
   die12 = dieRol(12);
   die8 = dieRol(8);
   die6 = dieRol(6);
   die4 = dieRol(4);
   
   sum = die20 + die12 + die8 + die6 + die4;
   
   System.out.println(sum);
   
   if (sum > 20 && sum < 35)
     ++wins;
   else
     ++losses;
   count++;
    }
   while(count != 100);
    
    System.out.println("Wins: " + wins);
    System.out.println("Losses: " + losses);
  }//end main
  
public static int dieRol (int x)
{
  int value;
  Random rng = new Random(); 
  value = rng.nextInt(x) + 1;
  return value;
}//end DR
}//end class