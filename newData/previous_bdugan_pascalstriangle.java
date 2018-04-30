// Display method inspired by:
//http://www.quickprogrammingtips.com/java/program-to-print-pascal-triangle-in-java.html

public class Pascal {
public void showTriangle(int n) {
    System.out.println();
		int rows = n;
    for (int i = 0; i < rows; i++) {
			System.out.print("n(" + i + ")" + "\t");
			System.out.format("%" + (rows - i) * 2 + "s", "");
			for (int j = 0; j <= i; j++) {System.out.format("%4d", binomialCoefficient(i, j));}
			System.out.println();}
		System.out.println();}
	public void showAddTriangle(int n) {
		System.out.println();
		int rows = n;
		for (int i = 0; i < rows; i++) {
			int number = 1;
			System.out.print("n(" + i + ")" + "\t");
			System.out.format("%" + (rows - i) * 2 + "s", "");
			for (int j = 0; j <= i; j++) {
				System.out.format("%6d", number);
				System.out.print(" ");
				number = number * (i - j) / (j + 1);}
			System.out.println();}
		System.out.println();}
	public void showEvenOddTriangle(int n) {
		System.out.println();
		int rows = n;
		for (int i = 0; i < rows; i++) {
			int number = 1;
			System.out.print("n(" + i + ")" + "\t");
			System.out.format("%" + (rows - i) * 2 + "s", "");
			for (int j = 0; j <= i; j++) {
				String symbol = spotEvenNumber(number);
				System.out.format("%4s", symbol);
				number = number * (i - j) / (j + 1);}
			System.out.println();}
		System.out.println();}
	public int factorial(int n) {
		int result = 1;
		for (int i = 1; i <= n; n--) {result *= n;}
		return result;}
	public int binomialCoefficient(int n, int k) {
		int result = 0;
		result = factorial(n) / (factorial(k) * factorial(n - k));
		return result;}
	public String spotEvenNumber(int n) {
		if (n % 2 == 1) {
			return "o";}
			 else {return " ";}}
	public int test1(int n) {
		int result = 0;
		for (int i = 0; i <= n; i++) {
			result += binomialCoefficient(n, i);}
		return result;}
	public int test2(int n) {
		int result = 0;
		for (int i = 0; i <= n; i++) {
			result += Math.pow(-1, i) * binomialCoefficient(n, i);}
		return result;}
	public int test3(int n, int m) {
		int result = 0;
		for (int i = m; i <= n; i++) {result += binomialCoefficient(i, m);}
		return result;}
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
		System.out.println("Test number 3: " + ((myPascal.test3(5, 3)) == (myPascal.binomialCoefficient(5 + 1, 3 + 1))));
		System.out.println();
		System.out.println("We can check whether a number is even or not ");
		System.out.println("Odd numbers display as o and even numbers as white space");
		System.out.println("This is 3: " + myPascal.spotEvenNumber(3));
		System.out.println("This is 4: " + myPascal.spotEvenNumber(4));
		System.out.println();
		System.out.println("This means that we can also display Pascal's triangle like this");
		System.out.println("Here it is for n = 3:");
		myPascal.showEvenOddTriangle(3);
		System.out.println();
		System.out.println("And here it is for n = 24 - We see a pattern!:");
		myPascal.showEvenOddTriangle(24);
		System.out.println("This is as far as the triangle can go with addition:");
		myPascal.showAddTriangle(29);}}