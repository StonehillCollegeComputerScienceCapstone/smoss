// credit: http://blog.amila.co/how-to-generate-n-n-magic-square-java/
public class MagicSquare {

	public MagicSquare(int n) {
		if (n % 2 == 0) {
			System.out.println("Enter an Odd Number.");
			return;
		}
		else if (n == 1) {
			System.out.println("1");
			return;
		}

		System.out.println("\n"+n+" * "+n+" Magic Square");
		System.out.println("********************\n");

		int[][] square = new int[n][n];
		int counter = 1;
		int row = 0;
		int col = (n - 1) / 2;
		square[row][col] = counter;

		while (true) {
				if (square[(row - 1) < 0 ? (row - 1 + n) : row - 1][(col + 1) % n] == 0) {
				row = (row - 1) < 0 ? (row - 1 + n) : row - 1;
				col = (col + 1) % n;
			} else { row = (row + 1) % n; }

			counter = counter + 1;
			square[row][col] = counter;
			if (counter == n * n) break;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (square[i][j] < 10 && (n * n) > 10) System.out.print("0");
				if (square[i][j] < 100 && (n * n) > 100) System.out.print("0");
				if (square[i][j] < 1000 && (n * n) > 1000) System.out.print("0");
				System.out.print(square[i][j] + " ");
			}
			System.out.println();
		}

		System.out.println("\nMagical No : " + (n * n * n + n) / 2);
	}

	public static void main(String args[]) {

		try {
			int n = Integer.parseInt(args[0]);
			new MagicSquare(n);
		} catch (Exception e) {
			System.out.println("Enter a Valid Number");
			System.out.println("Usage : java MagicSquare OddNumber");
		}
	}
}