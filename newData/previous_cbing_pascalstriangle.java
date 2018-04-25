import java.util.*;
public class Main{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		long[] facTwo = new long[33];
		for(int i = 0; i <= 32; i++)
		{
			facTwo[i] = (long) Math.pow(2, i);
		}
		for(int i = 0; i < tc; i++)
		{
			int a = sc.nextInt();
			long ans = 0;
			for(int j = 0; j < a; j++)
			{
				ans += facTwo[j];
			}
			System.out.println(ans);
		}
	}
		public static List<List<Integer>> generate(int numRows) {
		List<List<Integer>> pascalsTriangle = new ArrayList<List<Integer>>();

		if (numRows > 0) {
			ArrayList<Integer> previousRow = null;

			for (int i = 0; i < numRows; i++) {
				ArrayList<Integer> newRow = new ArrayList<>();

				for (int j = 0; j <= i; j++) {
					if (j == 0 || j == i) {
						newRow.add(1);
					} else {
						newRow.add(previousRow.get(j - 1) + previousRow.get(j));
					}
				}

				previousRow = newRow;

				pascalsTriangle.add(newRow);
			}
		}

		return pascalsTriangle;
	}

	// I like this one more for some reason...
	public static List<List<Integer>> generateSlow(int numRows) {
		List<List<Integer>> pascalsTriangle = new ArrayList<List<Integer>>();

		BigInteger[] factorialArray = new BigInteger[numRows + 1];
		generateFactorials(factorialArray);

		if (numRows > 0) {
			for (int i = 0; i < numRows; i++) {
				ArrayList<Integer> newRow = new ArrayList<>();

				for (int j = 0; j <= i; j++) {
					newRow.add(
							factorialArray[i].divide((factorialArray[j].multiply(factorialArray[i - j]))).intValue());
				}

				pascalsTriangle.add(newRow);
			}
		}

		return pascalsTriangle;
	}
}