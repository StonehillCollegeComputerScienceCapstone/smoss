import java.util.Scanner;

/*
 In mathematics, Pascal's triangle is a geometric arrangement of the binomial
 coefficients in a triangle.
  (x + y)^0 = 1
  (x + y)^1 = 1*1x+1*y
  (x + y)^2 = x^2 + 2xy + y^2 = 1*x^2y^0 + 2*x^1y^1 + 1*x^0y^2.
  (x + y)^n = a_0*x^n + a_1*x^(n-1)*y + a_2*x^(n-2)*y^2 + … + a_(n-1)*x*y^(n-1) + a_n*y_n,

 An example of pascal traingle:
  1
  1 1
  1 2 1
  1 3 3 1
  1 4 6 4 1
  1 5 10 10 5 1


  1 c_{i,0}=c_{i,i}=1
  2 C_{ij} = C_{i-1, j-1} + C_{i-1, j}
*/
public class PascalTriangle {
    public static void main(String[] args) {

        int[][] pascalTriangle;
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the height of the pascal triangle: ");
        int triangleHeight = sc.nextInt();

		// Compute the triangle
        pascalTriangle = new int[triangleHeight][];
        for (int row = 0; row < pascalTriangle.length; row = row + 1) {
            pascalTriangle[row] = new int[row+1];

            pascalTriangle[row][0] = 1;
            pascalTriangle[row][row] = 1;
            for (int column = 1; column < row; column = column + 1) {
                pascalTriangle[row][column] =
                        pascalTriangle[row-1][column] + pascalTriangle[row-1][column-1];
            }
        }

		// Print the triangle
        for (int row = 0; row < pascalTriangle.length; row = row + 1) {
            for (int column = 0; column < pascalTriangle[row].length; column = column + 1) {
                System.out.print(" " + pascalTriangle[row][column]);
            }
            System.out.println();
        }
    }

}