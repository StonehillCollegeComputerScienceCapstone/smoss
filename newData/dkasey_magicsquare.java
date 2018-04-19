// credit: https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/
import java.util.*;
public class MagicSquare{
  public static void main(String args[]){
    int[][] q=new int[3][3];
    String s=new String();
    Scanner k=new Scanner(System.in);
    boolean magic=false;
    System.out.println("Row 1, numbers (0-9) divided by spaces.");
    s=k.nextLine();
    for(int a=0;a<3;a++)
      q[a][0]=Integer.parseInt(s.substring(a*2,(a*2)+1));
    System.out.println("Row 2, numbers (0-9) divided by spaces.");
    s=k.nextLine();
    for(int a=0;a<3;a++)
      q[a][1]=Integer.parseInt(s.substring(a*2,(a*2)+1));
    for(int a=0;a<10;a++){
      q[2][2]=a;
      for(int b=0;b<10;b++){
        q[1][2]=b;
        for(int c=0;c<10;c++){
          q[0][2]=c;
          if(q[0][0]+q[1][0]+q[2][0]==15&&q[0][1]+q[1][1]+q[2][1]==15&&q[0][2]+q[1][2]+q[2][2]==15&&
             q[0][0]+q[0][1]+q[0][2]==15&&q[1][0]+q[1][1]+q[1][2]==15&&q[2][0]+q[2][1]+q[2][2]==15&&
             q[0][0]+q[1][1]+q[2][2]==15&&q[0][2]+q[1][1]+q[2][0]==15){
            System.out.println("Possible solution: "+c+" "+b+" "+a);
            magic=true;
          }
        }
      }
      if((a==9)&&(magic==false))
        System.out.println("Your square sucks");
    }
  }
}