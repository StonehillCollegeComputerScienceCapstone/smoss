import java.util.Random;
public class CarnivalGame
{
    public static void main(String[] args)
    {
        int gamesWon = 0;
       for(int i = 1; i <= 100; ++i)
       {
           int sum = dieRoll(6) + dieRoll(20) + dieRoll(8) + dieRoll(4) + dieRoll(12);
           if(sum > 35 || sum < 20)
           {
               ++gamesWon;

           }
           System.out.println(sum);

       }


        System.out.println("Games Won: " + gamesWon);

    }//end main
    public static int dieRoll(int x)
    {
        Random rng = new Random();
        int num = rng.nextInt(x) + 1;
        return num;

    }//end method
}//end class
