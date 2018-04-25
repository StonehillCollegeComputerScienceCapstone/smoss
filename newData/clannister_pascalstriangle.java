/**
 * Defines Pascal's Triangle
 */
public class PascalsTriangle {
    private final long[][] triangle;

    /**
     * Sole constructor
     *
     * @param depth the depth of the triangle
     */
    PascalsTriangle(int depth) {
        triangle = new long[depth][];
        long upperLeft;
        long upperRight;

        for (int i = 0; i < depth; i++) {
            triangle[i] = new long[i + 1];

            for (int j = 0; j < i + 1; j++) {
                if(i == 0) {
                    triangle[i][j] = 1; //seed the triangle
                }
                else {
                    try {
                        upperLeft = triangle[i - 1][j - 1];
                    } catch (ArrayIndexOutOfBoundsException e) {
                        upperLeft = 0; //upperLeft is 0 if not found
                    }

                    try {
                        upperRight = triangle[i - 1][j];
                    } catch (ArrayIndexOutOfBoundsException e) {
                        upperRight = 0; //upperRight is 0 if not found
                    }

                    triangle[i][j] = upperLeft + upperRight;
                }
            }
        }
    }

    /**
     * Prints the triangle to System.out
     */
    public void printTriangle() {
        for (long[] iTriangle : triangle) {
            for (long jTriangle : iTriangle) {
                System.out.printf("%d ", jTriangle);
            }
            System.out.println();
        }
    }
    
    private static void generateFactorials(BigInteger[] factorialArray) {
		factorialArray[0] = BigInteger.valueOf(1);
		int i=1;
		while(i < factorialArray.length) {
			factorialArray[i] = factorialArray[i - 1].multiply(BigInteger.valueOf(i));
			i++;
		}
	}

	private static void printTriangle(List<List<Integer>> triangle) {
		for (List<Integer> row : triangle) {
			for (int i : row) {
				System.out.print(i + " ");
			}
			System.out.println("");
		}
	}

    /**
     * Main method - create and print a triangle
     */
    public static void main(String[] arg) {
        PascalsTriangle triangle = new PascalsTriangle(10);
        triangle.printTriangle();
    }
}