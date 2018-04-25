/*
 * Given numRows, generate the first numRows of Pascal's triangle.
 */

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Solution118 {
	public static void main(String[] args) {
		List<List<Integer>> list = generate(5);

		printTriangle(list);
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

	private static void generateFactorials(BigInteger[] factorialArray) {
		factorialArray[0] = BigInteger.valueOf(1);

		for (int i = 1; i < factorialArray.length; i++) {
			factorialArray[i] = factorialArray[i - 1].multiply(BigInteger.valueOf(i));
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
} 