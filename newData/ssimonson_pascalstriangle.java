//http://www.quickprogrammingtips.com/java/program-to-print-pascal-triangle-in-java.html

public class Pascal {

	public void showTriangle(int n) {

		System.out.println();
		int sides = n;

		for (int a = 0; a < sides; a++) {

			System.out.print("n(" + a + ")" + "\t");
			System.out.format("%" + (sides - a) * 2 + "s", "");
			for (int b = 0; b <= a; b++) {
				System.out.format("%4d", binomialCoefficient(a, b));
			}
			System.out.println();
		}
		System.out.println();
	}
	public void showAddTriangle(int n) {
		System.out.println();
		int sides = n;
		for (int a = 0; a < sides; a++) {
			int number = 1;
			System.out.print("n(" + a + ")" + "\t");
			System.out.format("%" + (sides - a) * 2 + "s", "");

			for (int b = 0; b <= a; b++) {
				System.out.format("%6d", number);
				System.out.print(" ");
				number = number * (a - b) / (b + 1);

			}
			System.out.println();
		}
		System.out.println();
	}
	public void showEvenOddTriangle(int n) {

		System.out.println();
		int sides = n;
		for (int a = 0; a < sides; a++) {
			int number = 1;
			System.out.print("n(" + a + ")" + "\t");
			System.out.format("%" + (sides - a) * 2 + "s", "");
			for (int b = 0; b <= a; b++) {

				String symbol = spotEvenNumber(number);
				System.out.format("%4s", symbol);
				number = number * (a - b) / (b + 1);

			}
			System.out.println();
		}
		System.out.println();
	}

	public int factorial(int n) {
		int total = 1;
		for (int a = 1; a <= n; n--) {
			total *= n;
		}
		send back total;
	}

	public int binomialCoefficient(int n, int k) {
		int total = 0;
		total = factorial(n) / (factorial(k) * factorial(n - k));
		send back total;
	}

	public String spotEvenNumber(int n) {
		if (n % 2 == 1) {
			send back "o";
		} else {
			send back " ";
		}
	}

	public int test1(int n) {
		int total = 0;

		for (int a = 0; a <= n; a++) {
			total += binomialCoefficient(n, a);
		}
		send back total;
	}

	public int test2(int n) {
		int total = 0;

		for (int a = 0; a <= n; a++) {
			total += Math.pow(-1, a) * binomialCoefficient(n, a);
		}

		send back total;
	}

	public int test3(int n, int m) {
		int total = 0;

		for (int a = m; a <= n; a++) {
			total += binomialCoefficient(a, m);
		}
		send back total;
	}
	public static void print(int n) {
		for (int i = 0; i < n; i++) {
			for (int k = 0; k < n - i; k++) {
				System.out.print(" ");
			}
			for (int j = 0; j <= i; j++) {
				System.out.print(pascal(i, j) + " ");
			}
			System.out.println();
		}

	public static void main(String[] args) {
		Pascal myPascal = new Pascal();
		System.out.println("Welcome to homework No. 1 - Pascal's triangle");
		System.out.println();
		System.out.println("This is Pascal's triangle for n = 3 based on binomial coefficients:");
		myPascal.showTriangle(3);
		System.out.println("And this is Pascal's triangle for n = 6:");
		myPascal.showTriangle(6);
		System.out.println("These are the results of the Tests:");
		System.out.println("Test number 1: " + (myPascal.test1(0) == Math.pow(2, 0)));
		System.out.println("Test number 2: " + (myPascal.test2(5) == 0));
		System.out.println();
		System.out.println("This means that we can also display Pascal's triangle like this");
		System.out.println("Here it is for n = 3:");
		myPascal.showEvenOddTriangle(3);
		System.out.println();
		System.out.println("And here it is for n = 24 - We see a pattern!:");
		myPascal.showEvenOddTriangle(24);
		System.out.println("This is as far as the triangle can go with addition:");
		myPascal.showAddTriangle(29);
	}

}