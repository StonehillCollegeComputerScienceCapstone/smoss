// credit: http://www.dreamincode.net/forums/topic/138723-java-check-magic-square/

public class MagicSquare{
    static int rowSum1;
    static int rowSum2;
    static int rowSum3;
    static int rowSum4;
   int [][] square = {

      {16, 3, 2, 13},
      {5, 10, 11, 8},
      {9, 6, 7, 12 },
      {4, 15, 14, 1}
      };
   System.out.println("Is magic square: " + magicSquare(square));

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

   System.out.println("Enter the numbers for a " + SIZE + "x" + SIZE + " magic square.");
   for (int i = 0; i < SIZE * SIZE; i++)
   {
   System.out.print(i + 1 + ": ");
   if (in.hasNextInt())
   {
   ms.add(in.nextInt());
   }
   }

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

        if ((rowSum1 == rowSum2) && (rowSum1 == rowSum3) && (rowSum1 == rowSum4) && (rowSum1 == columnSum1)
                && (rowSum1 == columnSum2) && (rowSum1 == columnSum3) && (rowSum1 == columnSum4)){
            System.out.println("Congradulations, you have a magic square!!!!");
        } else {
            System.out.println("You Fail!!!!!!");
        }
    }
}