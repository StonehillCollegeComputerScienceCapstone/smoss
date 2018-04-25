/*
 * @file
 * @par File Name:
 * PascalsTriangle.java
 * @author Yoichiro Shimizu
 * @date Created on 2013/08/05
 * @par Copyright:
 * Ricoh IT Solutions, LTD.
 */

package ex07_03;

/**
 * 
 * @author budou-gumi
 * 
 */
public class PascalsTriangle {
	private int pascal[][];

	public PascalsTriangle(int num) {
		pascal = new int[num][];
		for (int i = 0, j = 0; i < pascal.length; i++) {
			pascal[i] = new int[i + 1];
			pascal[i][j] = 1;
			pascal[i][i] = 1;
		}
		calc();
	}

	public int[][] calc() {
		for (int j = 2; j < pascal.length; j++)
			for (int i = 1; i < pascal[j].length - 1; i++) {
				pascal[j][i] = pascal[j - 1][i - 1] + pascal[j - 1][i];
			}
		return pascal;
	}

	public void show() {
		for (int j = 0; j < pascal.length; j++) {
			int[] array = pascal[j];
			for (int i = 0; i < pascal.length - j; i++) {
				System.out.printf("   ");
			}
			for (int i : array) {
				System.out.printf("%4d ", i);
			}

			System.out.println();
		}
	}

	public static void main(String[] args) {
		PascalsTriangle pt = new PascalsTriangle(12);
		pt.show();
		pt = new PascalsTriangle(20);
		pt.show();
	}
}