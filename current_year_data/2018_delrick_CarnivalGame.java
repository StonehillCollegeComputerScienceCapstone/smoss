import java.util.Random;
public class CarnivalGame
{
 public static void main(String[] args)
 {
 for(int i=1; i<=100; ++i){
 dieRoll(6);
 dieRoll(20);
 dieRoll(8);
 dieRoll(4);
 dieRoll(12);
 if((dieRoll(6) + dieRoll(20) + dieRoll(8) + dieRoll(4) + dieRoll(12) >35 || (dieRoll(6) + dieRoll(20) + dieRoll(8) + dieRoll(4) + dieRoll(12) <20))){
  System.out.println("You win");
  }
  else
  System.out.println("You lose");
  }
 }
 public static int dieRoll(int x)
 {
  Random rng = new Random();
  int num;
  return num = rng.nextInt(x);
}
}