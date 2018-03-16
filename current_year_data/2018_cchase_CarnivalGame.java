import java.util.Random;

public class CarnivalGame
{
  public static void main(String[] args)
  {
    int wins = 0;
    for (int i = 1; i<100; i++)
    {playGame();
    if (playGame())
        wins++;
    }
    System.out.println(wins + " wins");
  }//end main
  
  public static int dieRoll(int x)
  {
    Random die = new Random();
    return die.nextInt() + 1;
  }//end method dieRoll
  
  public static boolean playGame()
  {
    int sum = dieRoll(6) + dieRoll(20) + dieRoll(8) + dieRoll(4) +dieRoll(12);
    if (sum > 35 || sum < 20)
      return true;
    return false;
    
  }//end method playGame
  
  
  
  
  
  
  
  
  
}//end class