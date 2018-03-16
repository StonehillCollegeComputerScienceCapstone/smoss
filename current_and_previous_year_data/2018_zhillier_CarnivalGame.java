import java.util.Random;
public class CarnivalGame
{
  public static void main(String[] args)
  {
    int d1, d2, d3, d4, d5, sum, winTotal = 0;
    
  for(int i = 1; i < 101; ++i)
  {
    d1 = diceRoll(6);
    d2 = diceRoll(20);
    d3 = diceRoll(8);
    d4 = diceRoll(4);
    d5 = diceRoll(12);
    sum = d1 + d2 + d3 + d4 + d5;
    System.out.println(sum);
    
    if(sum < 20 || sum > 35)
      winTotal = winTotal + 1;
  }
  System.out.println("You won this many games: " + winTotal);
  }//end main
  
  public static int diceRoll(int n)
  {
  
    Random rng = new Random();
     return rng.nextInt(n); 
  }//end method 
}//end class