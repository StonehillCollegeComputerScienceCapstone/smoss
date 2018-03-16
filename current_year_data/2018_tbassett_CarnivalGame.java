import java.util.Random;
public class CarnivalGame
{
  public static void main(String[] args)
  {
    int wins = 0;
    for(int i = 1; i <=100; i++)
    {
    int die4 = dieRoll4(); 
    int die6 = dieRoll6();
    int die8 = dieRoll8();
    int die12 = dieRoll12();
    int die20 = dieRoll20();
    int sum = die4 + die6 + die8 + die12 + die20;
    if(sum > 35 || sum < 20)
    {
      wins = wins + 1;
  }
 
    }
    System.out.println("You won " + wins + " times out of 100!");
  }
   public static int dieRoll4()
  { 
  Random n = new Random();
  int x = n.nextInt(4);
      return x;
  }
   public static int dieRoll6()
  { 
  Random n = new Random();
  int x = n.nextInt(6);
      return x;
  }
   public static int dieRoll8()
  { 
  Random n = new Random();
  int x = n.nextInt(9);
      return x;
  }
   public static int dieRoll12()
  { 
  Random n = new Random();
  int x = n.nextInt(12);
      return x;
  }
   public static int dieRoll20()
  { 
  Random n = new Random();
  int x = n.nextInt(20);
      return x;
  }
}