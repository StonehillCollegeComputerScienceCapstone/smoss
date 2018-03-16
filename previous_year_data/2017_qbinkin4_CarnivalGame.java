import java.util.*;
public class CarnivalGame
{
public static void main(String[] args)
{
int wins = 0, lose = 0;
for (int i = 1; i<=100; i++)
{
int total = rollDie(4) + rollDie(6) + rollDie(8) + rollDie(12) + rollDie(20);
System.out.println("Your score is " + total);
if (total < 20 || total > 35){
 System.out.println("You win!");
 wins++;}
else{ 
 System.out.println("You lose.");
 lose++;}
 }//end for 
 System.out.println("You won " + wins + " games and lost " + lose + " games.");
}//end main

public static int rollDie(int x)
{
Random roll = new Random();
return roll.nextInt((x) + 1);
}//end method
}//end class