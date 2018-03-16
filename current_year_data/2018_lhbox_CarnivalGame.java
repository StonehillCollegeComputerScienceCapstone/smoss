import java.util.Scanner;
import java.util.Random;

public class CarnivalGame
{
  public static void main(String[] args)
 {
   int gamesWon=0;
   int gamesLost=0;
   int total;
   int four, six, eight, twelve, twenty;
  
   
   for(int i=0; i<100; ++i)
   {
    four = dieRoll(4);
    six = dieRoll(6); 
    eight = dieRoll(8); 
    twelve = dieRoll(12);  
    twenty = dieRoll(20);
    
    total = four + six + eight + twelve + twenty;
    
    if(total>35 || total<20)
    {
      gamesWon= gamesWon+1;
    }
    if(total>=20 && total<=35)
      gamesLost= gamesLost+1;
   }
   
   System.out.println("Games won: " + gamesWon);
   System.out.println("Games lost: " + gamesLost);
     
  }//end main
  
  public static int dieRoll(int x)
  {
    Random rng = new Random();
    int roll;
    roll= rng.nextInt(x) + 1;
    return roll;
  }//end method
  
  
}// end class