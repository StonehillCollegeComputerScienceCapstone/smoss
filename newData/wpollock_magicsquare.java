// Credit: https://introcs.cs.princeton.edu/java/14array/MagicSquare.java
/******************************************************************************
 *  Compilation:  javac MagicSquare.java
 *  Execution:    java MagicSquare n
 *
 *  Generates a magic square of order n. A magic squares is an n-by-n
 *  matrix of the integers 1 to n^2, such that all row, column, and
 *  diagonal sums are equal.
 *
 *  One way to generate a magic square when n is odd is to assign
 *  the integers 1 to n^2 in ascending order, starting at the
 *  bottom, middle cell. Repeatedly assign the next integer to the
 *  cell adjacent diagonally to the right and down. If this cell
 *  has already been assigned another integer, instead use the
 *  cell adjacently above. Use wrap-around to handle border cases.
 *
 *
 *  % java MagicSquare 3
 *   4  9  2
 *   3  5  7
 *   8  1  6
 *
 *  % java MagicSquare 5
 *  11 18 25  2  9
 *  10 12 19 21  3
 *   4  6 13 20 22
 *  23  5  7 14 16
 *  17 24  1  8 15
 *
 *  Limitations
 *  -----------
 *   - n must be odd
 *
 ******************************************************************************/

public class MagicSquare {

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        if (n % 2 == 0) throw new RuntimeException("n must be odd");

        int[][] magic = new int[n][n];

        int row = n-1;
        int col = n/2;
        magic[row][col] = 1;

        for (int i = 2; i <= n*n; i++) {
            if (magic[(row + 1) % n][(col + 1) % n] == 0) {
                row = (row + 1) % n;
                col = (col + 1) % n;
            }
            else {
                row = (row - 1 + n) % n;
                // don't change col
            }
            magic[row][col] = i;
        }

        // print results
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (magic[i][j] < 10)  System.out.print(" ");  // for alignment
                if (magic[i][j] < 100) System.out.print(" ");  // for alignment
                System.out.print(magic[i][j] + " ");
            }
            System.out.println();
        }

    }
}
