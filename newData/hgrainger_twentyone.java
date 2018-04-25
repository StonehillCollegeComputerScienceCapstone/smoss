import java.util.*;

public class TwentyOne
{
  public static void main(String[] args)
  {
    //I need these variables at the end of the program so I declared them early on
    int win=0;
    int lose=0;
    do
    {
    Scanner input = new Scanner(System.in);
    int total=0;
    int roll=0;
    int yes;
    do
    {
      System.out.println("Enter 1 to roll or 2 to quit : ");
      yes = input.nextInt();
      if (yes==1)
      {
        if (total<14)
        {
          roll = roll() + roll();
        }
        if (total>=14)
        {
          roll = roll();
        }
        total = total + roll;
        System.out.println("You rolled a "+roll+". Score is "+total);
      }
    }while((yes==1)&&(total<22));
    //this do while loop is good for both the above user and the below computer
    //liked these better than for loops
    //for loops seem best for when you have an certain number of loops to execute
    if(total>21)
    {
      System.out.println("Computer wins");
      lose=lose+1;
      //this if statement allows me to shut down the game if user exceeds 21
      //that way the computer doesn't have to roll
    }
    else
    {
    System.out.println("Computer rolls");
    int total2 = 0;
    int roll2 = 0;
    do
    {
      if (total2<14)
      {
        roll2 = roll() + roll();
      }
      if (total2>=14)
      {
        roll2 = roll();
      }
      total2 = total2 + roll2;
      System.out.println("Computer rolled a "+roll2+". Score is "+total2);
    }while((total2<total+1)&&(total2<22));
    System.out.println("Computer Stops. Score is "+total2);
      if (total>=total2)
    {
      System.out.println("You win");
      win=win+1;
    }
    if ((total2>total)&&(total2<22))
    {
      System.out.println("Computer wins");
      lose=lose+1;
    }
    if (total2>21)
    {
      System.out.println("You win");
      win=win+1;
    }
    }
    }while (askPlayer());
    System.out.println("Games won: "+win);
    System.out.println("Games lost: "+lose);
  }
  public static int roll()
  {
    int result = (int)((Math.random()*6)+1);
    return result;
    //used this method instead of always writing out the random number generator
    //very useful, still getting use to methods
  }
  public static boolean askPlayer()
  {
    Scanner input = new Scanner(System.in);
    System.out.println("Play again? Enter 1 for yes: ");
    int yes = input.nextInt();
    if (yes==1)
    {
      return true;
    }
    else
    {
      return false;
    }
    //found this method useful in organizing when the program shuts down
  }
}