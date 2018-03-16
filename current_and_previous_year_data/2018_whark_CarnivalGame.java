import java.util.Random;
public class CarnivalGame
{
    public static void main(String[]args)
    {   
       
       int win=0, totalFromDice = 0;
       
       for (int i=0; i<100; i++)
       {
           totalFromDice = dieRoll(4)+dieRoll(6)+dieRoll(8)+dieRoll(12)+dieRoll(20);
           System.out.println(totalFromDice);
           if (totalFromDice >35 || totalFromDice < 20)
           win++;
       }
            System.out.println("Number of times you won out of 100: "+ win);

       }
    public static int dieRoll(int n)
    {
     Random rng = new Random();
     
       return (rng.nextInt(n));
     
        
       
    }

      
}//end class
    
    
   
 