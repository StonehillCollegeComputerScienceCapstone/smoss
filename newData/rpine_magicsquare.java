// credit: https://coderanch.com/t/673319/java/array-magic-square
public class SandBox{
  public static void main (String[] args){
   int [][] square = {

      {16, 3, 2, 13},
      {5, 10, 11, 8},
      {9, 6, 7, 12 },
      {4, 15, 14, 1}
      };
   System.out.println("Is magic square: " + magicSquare(square));
 }
   private static boolean magicSquare(int[][] square){

   //calculate the sum of the first row and assign it to n
       int n = sumOfRow(square[0]);

       for (int[] row : square)
       {
          int sum = sumOfRow(row);
          if (sum != n)
          return false;
       }


       int sum = 0;
       for (int i = 0; i < square.length; i++)
       {
          sum += square[i][i];
       }
       if (sum != n)
          return false;


       sum = 0;
       for (int i = 0; i < square.length; i++)
       {
          sum += square[i][square.length - 1 - i];
       }
       if (sum != n)
          return false;
       return true;
    }

   //returns the sum of the elements in the row
   private static int sumOfRow(int[] row){
      int sum = 0;
      for(int el : row){
         sum += el;
      }
      return sum;
   }

}