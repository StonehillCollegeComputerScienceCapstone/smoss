import java.util.*;
public class CarnivalGame
{
  public static void main(String[] args)
  {
    int wins = 0, losses = 0;
    for(int i = 1; i <= 100; i++)
    {
      int die6 = dieRoll(6);
      int die20 = dieRoll(20);
      int die8 = dieRoll(8);
      int die4 = dieRoll(4);
      int die12 = dieRoll(12);
      int sumOfDice = die6 + die20 + die8 + die4 + die12;
      
    System.out.println(i + ": " + die6 + " + " + die20 + " + " + die8 + " + " + die4 + " + " + die12 + " = " + sumOfDice);
    if(sumOfDice > 35 || sumOfDice < 20)
    {
      wins = wins + 1;
    }//end if
    else
    {
     losses = losses + 1; 
    }//end else
    }//end for loop
    
    System.out.println("Wins: " + wins);
    System.out.println("Losses: " + losses);
  }//end main
  
  public static int dieRoll(int x)
  {
    Random rng = new Random();
  int roll = 0;
  roll = roll + rng.nextInt(x) + 1;
   return roll;
  }//end method
    
}//end class