/**
 * Pascal's Triangle:
 * This is a small application to generate a Pascal's Triangle and print it to System out.
 *
 * For more information:
 * @see <a href="https://en.wikipedia.org/wiki/Pascal%27s_triangle">Pascal's triangle - Wikipedia</a>
 *
 * @author Steven Mackay
 */
public class PascalsTriangle {
    /**
     * Main entry point in to the application.
     * Call this application with 1 argument to output a Pascal's triangle for n number of rows or 2 arguments to get
     * the value at position (n, k).
     *
     * @param args The array of command-line arguments.
     */
    public static void main(String args[]) {
        System.out.println("PASCAL'S TRIANGLE");
        System.out.println("");

        try {
            if (args.length == 1) {
                //get the number of rows from args
                int rows = Integer.parseInt(args[0]);

                //generate the triangle
                int [][] pascalsTriangle = get(rows);

                //calculate the length of the longest number in the triangle array.
                int numberLength = String.valueOf(pascalsTriangle[rows - 1][(rows - 1) / 2]).length();
                numberLength += (numberLength % 2) + 2;

                //calculate the length of the longest/last row.
                int rowLength = rows * numberLength;

                //output the triangle to system out
                for (int n = 0; n < pascalsTriangle.length; n++) {
                    //calculate left padding
                    int leftPadding = ((rowLength - ((n + 1) * numberLength)) / 2);
                    if (leftPadding != 0) System.out.print(String.format("%" + leftPadding + "s", ""));

                    //output the left values
                    for (int k = 0; k < pascalsTriangle[n].length; k++) {
                        System.out.print(String.format("%-" + numberLength + "d",pascalsTriangle[n][k]));
                    }

                    //output the right values
                    for (int k = pascalsTriangle[n].length - ((n + 1) % 2) - 1; k >= 0; k--) {
                        System.out.print(String.format("%-" + numberLength + "d",pascalsTriangle[n][k]));
                    }
                    System.out.println("");
                }
                System.out.println("");
                System.out.println(rows + " rows.");
            } else if (args.length == 2) {
                //get the args
                int n = Integer.parseInt(args[0]);
                int k = Integer.parseInt(args[1]);

                //get the value at (n, k)
                int value = get(n, k);

                System.out.println("Value at (" + n + ", " + k + ") is: " + value);
            } else {
                throw new Exception("Incorrect number of arguments.");
            }
        } catch (NumberFormatException ne) {
            System.out.println("Invalid argument(s): " + ne.getMessage());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    /**
     * Get the value for position (n (row), k (column)).
     *
     * A recursive method to get the value by only calculating the necessary elements.
     *
     * @param n The row of the value in the triangle array.
     * @param k The column of the value in the triangle array.
     * @return The value of position (n, k)
     * @throws IndexOutOfBoundsException If the position (n, k) of out of the triangles bounds.
     */
    public static int get(int n, int k) throws IndexOutOfBoundsException {
        if (n < 0 || k < 0 || k > n)
            throw new IndexOutOfBoundsException();
        if (n == 0 || k == 0 || k == n)
            return 1;
        else
            return get(n - 1, k - 1) + get(n - 1, k);
    }

    /**
     * Get a two-dimensional array containing a Pascal's triangle for the number of rows specified. If the number of
     * rows is greater than 34 the method with throw an Exception. This is due to the limitations of Java's 32 bit integer.
     *
     * This method technically only generates half of the triangle to save time since both sides are the same.
     *
     * @param rows The number of rows to return
     * @return A two-dimensional array containing a Pascal's triangle.
     * @throws Exception An exception is thrown if the number of rows exceeds 34.
     */
    public static int[][] get(int rows) throws Exception {
        if (rows > 34) throw new Exception("This application can only support up to 34 rows.");
        int[][] pascalsTriangle = new int[rows][];
        for (int n = 0; n < rows; n++) {
            pascalsTriangle[n] = new int[(n / 2) + 1];
            for (int k = 0; k <= n / 2; k++) {
                if (k == 0) //first column of each row
                    pascalsTriangle[n][k] = 1;
                else if (k == n / 2 && n % 2 == 0) //columns at the middle on even rows
                    pascalsTriangle[n][k] = pascalsTriangle[n - 1][k - 1] + pascalsTriangle[n - 1][k - 1];
                else //all other columns
                    pascalsTriangle[n][k] = pascalsTriangle[n - 1][k - 1] + pascalsTriangle[n - 1][k];
            }
        }
        return pascalsTriangle;
    }
}