import java.util.Random;
public class CarnivalGame{
public static void main(String [] args){
 System.out.println("total wins is "+dieRoll(100));
}
public static int dieRoll(int x){
int counter=0;
for (int i=0;i<=x;i++){
Random rng = new Random();
 int r = rng.nextInt(6)+1;
 int r2 = rng.nextInt(20)+1;
 int r3 = rng.nextInt(8)+1;
 int r4 = rng.nextInt(4)+1;
 int r5 = rng.nextInt(12)+1;
 int total=r+r2+r3+r4+r5;

 if(total<35||total<20){
 counter++;
 }
  System.out.println(total);
 }
 return counter;
 
}





}