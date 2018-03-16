import java.util.Scanner;
import java.util.ArrayList;
public class Goldbach{
   public static void main (String [] args){
      Scanner input = new Scanner(System.in);
      System.out.println("Enter an even positive integer greater than 2:");
      int userInput = input.nextInt();
      int s = userInput;
      if (userInput>2&&userInput%2==0){
         System.out.println(goldbach(userInput,s));
      
      }
      else{
         System.out.println("Enter an even positive integer greater than 2:");
         userInput = input.nextInt();
         if (userInput>2&&userInput%2==0){
            System.out.println(goldbach(userInput,s));
         
         }
      }
      
   
   
   }//end nloop

 

   public static int goldbach(int userInput, int s){
      int x=0;
      int counter=0;
      ArrayList<Integer>p= new ArrayList<>();
      if (userInput>2){
         for(int i = 1; i<=userInput; i++)
         {
            if(isPrime(userInput)){
               
            
               p.add(16);
               counter++;
               userInput-=i;
               
               return goldbach(userInput,s);}
            else{
               userInput--;
               return goldbach(userInput,s);
            }
            
            }
         return userInput;}
         System.out.println(p);
      /*while (x!=userInput){
         System.out.println(userInput);
        
         System.out.println();
         for(int i=0;i< p.size() ;i++){
            for(int h=0;h<p.size();h++){
               int temp=p.get(i)+p.get(h);
               if (temp==s){
                  int first= p.get(i);
                  int second = p.get(h);
                  i=p.size();
                  h=p.size();
                  System.out.println(i+"+"+h+"="+s);
               }}}}
     */
      return s;  }  
   
   public static boolean isPrime(int userInput){
      boolean primeNum = true;
      if(userInput <= 1){
         return false;}
      if(userInput == 2){
         return true;}  
      for(int i = 2;i < Math.sqrt(userInput) + 1; ++i)
      {
         if(userInput % i == 0){
            return false;}
      } // returns true if n is prime, false if not
      return primeNum;
   
   }


}
