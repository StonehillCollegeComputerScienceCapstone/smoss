import java.util.Scanner; 
import java.util.Random;

public class CarnivalGame
{
  private static int totalScore; 
  private static int numWins; 
  
  public static void main(String args[])
  {
   for(int i=0; i < 100; i++)
   {
   Carnival();
   }
    System.out.println("You won " + numWins + " times out of 100!");
  }
  
  public static void Carnival()
  {
   System.out.println("Welcome to the carnival, rolling dice now... ");
   rollDice(); 
   if(totalScore > 35 || totalScore < 20)
   {
     System.out.println("You win!, your score was " + totalScore);
     numWins++;
    
  }
   else{
     System.out.println("Sorry, you lose your score was " + totalScore);  
   }
   totalScore = 0;
  }
  
  public static int dieRoll(int x)
  {
    Random random = new Random();
    return random.nextInt(x - 1 +1) + 1;
    
  }
  
  public static void rollDice()
  {
   totalScore += dieRoll(6); 
   totalScore += dieRoll(20);
   totalScore += dieRoll(8);
   totalScore += dieRoll(4);
   totalScore += dieRoll(12);
    
  }
  
  
  
  
  
}