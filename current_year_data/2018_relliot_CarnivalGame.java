import java.util.*;
public class CarnivalGame
{
public static void main(String[] args)
{
int win = 0, lose = 0;
for(int i = 0; i < 100; i++)
{
int roll6 = dieRoll(6), 
roll20 = dieRoll(20), 
roll8 = dieRoll(8), 
roll4 = dieRoll(4), 
roll12 = dieRoll(2);
int sum = roll6 + roll20 + roll8 + roll4 + roll12;

System.out.println(roll6 + " + " + roll20 + " + " + roll8 + " + " + roll4 + " + " + roll12);

if(sum < 20 || sum > 35)
{
win = win + 1;
}//end if
else
{
lose = lose + 1;
}
}
System.out.println("Wins: " + win);
System.out.println("Loses: " + lose);

}//end main

public static int dieRoll(int x)
{
int roll = (int)(Math.random() * x + 1);
return roll;
}






}//end class