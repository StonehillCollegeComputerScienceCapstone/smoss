import java.util.Random;

public class CarnivalGame
{
  public static void main(String[] args)
  {
    int win=0, loss=0;
    for(int i =1; i<=100; i++)
          {
      System.out.println("Game " + i + ":    " + play(i));
      if(play(i) >35 || play(i) < 25)
      {
        win++;
      }
      else
        loss++;
    }
    
        
        System.out.println("Wins:  " + win);
      System.out.println("Losses:  " + loss);
  }//end main
  
  public static int dieRoll(int x)
  {
    Random rng = new Random(); 
    int num = rng.nextInt((x) + 1);
    return num;
  }
  
  public static int play(int i)
  {
  int sum;
  sum = dieRoll(6) + dieRoll(20) + dieRoll(12) + dieRoll(4) + dieRoll(8);
  return sum;
  }
  
  
}//end class