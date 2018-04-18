// credit: http://www.cs.ucf.edu/~dmarino/ucf/introjava/MagicSquare_wMethods.java
//
// Skyler Goodell
// 7/9/2011
// Converted from a C program written without methods.
// Determines if a 3x3 grid of numbers is a magic square.

import java.util.*;

public class MagicSquare_wMethods {

    public static void main(String[] args) {

        // Create a 2D Array to store the square.
        int[][] square = new int[3][3];

        Scanner input = new Scanner(System.in);

        // Read in the user's magic square.
        System.out.println("Please enter your magic square.");
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                square[i][j] = input.nextInt();

        // Use our two methods to make sure the the square has
        //      the correct numbers and the 'magic' sums.
        // Output if the square is magic or not.
        if (checkFrequency(square) && checkSums(square))
            System.out.println("You have a magic square");
        else
            System.out.println("Not a magic square");
    }

    /* checkFrequency:
     * Make sure that each number 1 through 9 is in the square exactly once.
     *
     * returns: true if each number (1-9) appears exactly once, false otherwise.
     */
    private static boolean checkFrequency(int[][] square)
    {
        // Create an array to store the number of times each number appears.
        int[] freq = new int[10];

        // Set each frequency to zero initially.
        // Note: We will NOT use index 0 and we will store how many 1s we see
        //       in index 1, etc.
        for (int i = 1; i < 10; i++)
            freq[i] = 0;

        // Loop through each value in the square.
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

    /* checkSums:
     * Check that the sum of the rows, columns and diagonals all equal 15.
     *
     * returns: true is all rows, columns and diagonals equal 15, false otherwise.
     */
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

        // Check forward diagonal.
        if (square[0][0] + square[1][1] + square[2][2] != 15)
            return false;

        // Check backward diagonal.
        if (square[0][2] + square[1][1] + square[2][0] != 15)
            return false;

        return true;
    }

}
