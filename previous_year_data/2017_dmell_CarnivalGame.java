import java.util.Random;
public class CarnivalGame
{
  public static void main(String[] args)
  {
    int sum , win = 0;
    for(int c = 0; c <=100; ++c)
    {
    sum = dieRoll(6) + dieRoll(8) + dieRoll(12) + dieRoll(20) + dieRoll(4);
    if(sum < 20 || sum > 35)
      ++win;
    }
    System.out.println("You won " + win + " times!");
    
  }//end main
  
  public static int dieRoll(int b)
  {
    int n;
    Random rng = new Random();
      return rng.nextInt(b) + 1;
  }//end method
    
  
  
}//end class