import java.util.Random;
public class CarnivalGame
{

public static void main(String[] args)
{
int die1, die2, die3, die4, die5, total, wins, roll, loss;
wins=0;
loss=0;

for (int i=0; i<10; ++i)
{
total = dieRoll(4)+dieRoll(6)+dieRoll(8)+dieRoll(12) +dieRoll(20);
System.out.println(total);
if(total <20 || total >35)
{
wins++;
}

}

System.out.println("You won " + wins + " games");
System.out.println("You lost " + (10-wins) + " games");
}//end main

public static int dieRoll(int n)
{
Random rng = new Random();
return  rng.nextInt(n) +1;
}


}//end class