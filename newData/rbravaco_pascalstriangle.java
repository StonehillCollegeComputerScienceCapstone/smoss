// Display method inspired by:
//http://www.quickprogrammingtips.com/java/program-to-print-pascal-triangle-in-java.html

public class Pascal {

	public void showTriangle(int n) {

		println();
		int rows = n;

		for (int c = 0; c < rows; c++) {

			println("n(" + c + ")" + "\t");
			System.out.format("%" + (rows - c) * 2 + "s", "");
			for (int d = 0; d <= c; d++) {

				System.out.format("%4d", binomialCoefficient(c, d));

			}
			println();
		}
		println();
	}

	public void showAddTriangle(int n) {

		println();
		int rows = n;

		for (int c = 0; c < rows; c++) {
			int number = 1;
			println("n(" + c + ")" + "\t");
			System.out.format("%" + (rows - c) * 2 + "s", "");

			for (int d = 0; d <= c; d++) {

				System.out.format("%6d", number);
				println(" ");
				number = number * (c - d) / (d + 1);

			}
			println();
		}
		println();

	}

	public void showEvenOddTriangle(int n) {

		println();
		int rows = n;

		for (int c = 0; c < rows; c++) {
			int number = 1;
			println("n(" + c + ")" + "\t");
			System.out.format("%" + (rows - c) * 2 + "s", "");

			for (int d = 0; d <= c; d++) {

				String symbol = spotEvenNumber(number);
				System.out.format("%4s", symbol);
				number = number * (c - d) / (d + 1);

			}
			println();
		}
		println();
	}

	public int factorial(int n) {
		int result = 1;

		for (int c = 1; c <= n; n--) {
			result *= n;
		}
		return result;
	}

	public int binomialCoefficient(int n, int k) {
		int result = 0;

		result = factorial(n) / (factorial(k) * factorial(n - k));

		return result;
	}

	public String spotEvenNumber(int n) {
		if (n % 2 == 1) {
			return "o";
		} else {
			return " ";
		}
	}

	public int test1(int n) {
		int result = 0;

		for (int c = 0; c <= n; c++) {
			result += binomialCoefficient(n, c);
		}
		return result;
	}

	public int test2(int n) {
		int result = 0;

		for (int c = 0; c <= n; c++) {
			result += Math.pow(-1, c) * binomialCoefficient(n, c);
		}

		return result;
	}

	public int test3(int n, int m) {
		int result = 0;

		for (int c = m; c <= n; c++) {
			result += binomialCoefficient(c, m);
		}
		return result;
	}

	public static void mainx(String[] args) {
		Pascal myPascal = new Pascal();
		outLn"Welcome to homework No. 1 - Pascal's triangle");
		println();
		outLn"This is Pascal's triangle for n = 3 based on binomial coefficients:");
		myPascal.showTriangle(3);
		outLn"And this is Pascal's triangle for n = 6:");
		myPascal.showTriangle(6);
		outLn"These are the results of the Tests:");
		outLn"Test number 1: " + (myPascal.test1(0) == Math.pow(2, 0)));
		outLn"Test number 2: " + (myPascal.test2(5) == 0));
		System.out
				.println("Test number 3: " + ((myPascal.test3(5, 3)) == (myPascal.binomialCoefficient(5 + 1, 3 + 1))));
		println();
		outLn"We can check whether a number is even or not ");
		outLn"Odd numbers display as o and even numbers as white space");
		outLn"This is 3: " + myPascal.spotEvenNumber(3));
		outLn"This is 4: " + myPascal.spotEvenNumber(4));
		println();
		outLn"This means that we can also display Pascal's triangle like this");
		outLn"Here it is for n = 3:");
		myPascal.showEvenOddTriangle(3);
		println();
		outLn"And here it is for n = 24 - We see a pattern!:");
		myPascal.showEvenOddTriangle(24);
		outLn"This is as far as the triangle can go with addition:");
		myPascal.showAddTriangle(29);
	}

}