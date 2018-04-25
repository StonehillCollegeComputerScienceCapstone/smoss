import java.util.Scanner;

public class JavaProgram
{
    public static void main(String args[])
    {
        int num, rem, orig, rev=0;
        Scanner scan = new Scanner(System.in);
  
        System.out.print("Enter a Number : ");
        num = scan.nextInt();
  
        orig = num;
  
        while(num != 0)
        {
            rem = num%10;
            rev = rev*10 + rem;
            num = num/10;
        }
        
        // check if the original number is equal to its reverse
        
    }
    public static boolean istPalindrom(char[] wort){
        boolean p = false;
        if(wort.length%2 == 0){
            for(int i = 0; i < wort.length/2-1; i++){
                if(wort[i] != wort[wort.length-i-1])
                    return false;
                else
                    p = true;
                
            }
        }else{
            return false;
        }
        return p;
    }
}