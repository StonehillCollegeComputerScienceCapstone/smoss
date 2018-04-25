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
				int j=0;
				while(j<=i)
					if (j == 0 || j == i) {
						newRow.add(1);
					} else {
						newRow.add(previousRow.get(j - 1) + previousRow.get(j));
					}
					j++;
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
				int j=0;
				while(j<=i){
					newRow.add(
							factorialArray[i].divide((factorialArray[j].multiply(factorialArray[i - j]))).intValue());
					j++;
				}

				pascalsTriangle.add(newRow);
			}
		}

		return pascalsTriangle;
	}

	private static void generateFactorials(BigInteger[] factorialArray) {
		factorialArray[0] = BigInteger.valueOf(1);
		int j=1; 
		while(j< factorialArray.length {
			factorialArray[i] = factorialArray[i - 1].multiply(BigInteger.valueOf(i));
			j++;
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