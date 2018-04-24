import java.util.*;

public class MagicSquare_wMethods {

    public static void main(String[] args) {

        int[][] square = new int[3][3];

        Scanner input = new Scanner(System.in);

        System.out.println("Please enter your magic square.");
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                square[i][j] = input.nextInt();
        if (checkFrequency(square) && checkSums(square))
            System.out.println("You have a magic square");
        else
            System.out.println("Not a magic square");
    }
    private static boolean checkFrequency(int[][] square)
    {
        int[] freq = new int[10];

        for (int i = 1; i < 10; i++)
            freq[i] = 0;

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                // Invalid number - all values must be between 1 - 9.
                if (square[i][j] < 1 || square[i][j] > 9)
                    return false;

                // Increase the frequncy for this number.
                freq[square[i][j]]++;
            }
        }

        // If any number does not appear exactly once then the square is not magic.
        for (int i = 1; i < 10; i++)
            if (freq[i] != 1)
                return false;

        return true;
    }
    private static boolean checkSums(int[][] square)
    {
        // Check each row.
        for (int i = 0; i < 3; i++)
        {
            // Find the sum of row #i.
            int sum = 0;
            for (int j = 0; j < 3; j++)
                sum += square[i][j];

            // If this row does not equal 15, then it is not a magic square
            if (sum != 15)
                return false;
        }

        // Check each column.
        for (int j = 0; j < 3; j++)
        {
            // Find the sum of column #j.
            int sum = 0;
            for (int i = 0; i < 3; i++)
                sum += square[i][j];

            // If this column does not equal 15, then it is not a magic square
            if (sum != 15)
                return false;
        }
        
        if (square[0][0] + square[1][1] + square[2][2] != 15)
            return false;
        if (square[0][2] + square[1][1] + square[2][0] != 15)
            return false;

        return true;
    }
 public static void recursiveTriangle(int n)
  {
    if (n!=0)
    {
    recursiveCol(n);
    recursiveTriangle(n-1);
    }
  }
  public static void recursiveCol(int n)
  {
    if (n==1)
    {
      System.out.println("x");
    }
    if (n>1)
    {
      System.out.print("x");
      recursiveCol(n-1);
    }
  }
}