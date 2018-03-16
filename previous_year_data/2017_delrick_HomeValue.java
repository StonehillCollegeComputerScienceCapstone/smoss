import java.util.Scanner;
public class HomeValue
{
 public static void main(String[] args){
 //do
 //{
 Scanner keyboard = new Scanner(System.in);
 int Change1 = 0, Change2= 0, Change3= 0, Change4=0, Change5=0, Change6=0;
 System.out.println("Enter the length of time of the investment (an integer between 1 and 6 inclusive):");
 int numYears = keyboard.nextInt();
 int Nyears = numYears * 100000;
 System.out.println("Enter the percent change for each of the years on seperate lins(if decrease enter as negative):");
 int pChange1 = keyboard.nextInt();
 int pChange2 = keyboard.nextInt();
 int pChange3 = keyboard.nextInt();
 int pChange4 = keyboard.nextInt();
 int pChange5 = keyboard.nextInt();
 int pChange6 = keyboard.nextInt();
 if(pChange1 > 0){
 Change1 = 1 + (pChange1/100);
 }
 if(pChange1 < 0){
 
 Change1 = 1 - (pChange1/100);
 }
 if(pChange2 > 0){
 Change2 = 1 + (pChange2/100);
 }
 if(pChange2 < 0){
 Change2 = 1 - (pChange2/100);
 }
  if(pChange3 > 0){
 Change3 = 1 + (pChange3/100);
 }
 if(pChange3 < 0){
 Change3 = 1 - (pChange3/100);
 }
  if(pChange4 > 0){
 Change4 = 1 + (pChange4/100);
 }
 if(pChange4 < 0){
 Change4 = 1 - (pChange4/100);
  if(pChange5 > 0){
 Change5 = pChange5/100;
 }
 if(pChange5 < 0){
 Change5 = 1 - (pChange5/100);
  }
  if(pChange6 > 0){
 Change6 = 1 + (pChange6/100);
 }
 if(pChange6 < 0){
 Change6 = 1 - (pChange6/100);
  }
  }
 int average = (Change1 * Change2 * Change3 * Change4 * Change5 * Change6 * Nyears);
 System.out.println("The average anuual change is " + average);
 //System.out.println("Run again? 1 for yes:");
 //int another = keyboard.nextInt();
 //}while(another == 1);
 
 }
 }




