// credit: http://www.mrpudaloff.com/uploads/1/4/0/1/14010214/arrays_-_magic_square.docx
/**
 * @author (your name)
 */
import java.util.*;

public class MagicSquare
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter size of Magic square (must be odd): ");
        int n = s.nextInt();
        if (n % 2 == 0) throw new RuntimeException("N must be odd");

        int[][] magic = new int[n][n];



        // YOUR CODE HERE!!!!!
        // HAVE FUN !!!!!




        // prints out results will align up to 3 digit #s
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (magic[i][j] < 10)
System.out.print(" "); // extra space for alignment
                if (magic[i][j] < 100)
System.out.print(" ");  // extra space for alignment
                System.out.print(magic[i][j] + " ");
            }
            System.out.println();
        }

    }
}