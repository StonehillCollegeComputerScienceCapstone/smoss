package lzq.leetcode.initial.normal;

import java.util.ArrayList;

public class PascalsTriangle {
	/**
	 * Given numRows, generate the first numRows of Pascal's triangle.
	 * 
	 * For example, given numRows = 5, Return
	 * 
	 * [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
	 * 
	 * @param numRows
	 * @return
	 */
	public ArrayList<ArrayList<Integer>> generate(int numRows) {
		// Start typing your Java solution below
		// DO NOT write main() function
		if (numRows <= 0) {
			return new ArrayList<ArrayList<Integer>>();
		}
		ArrayList<ArrayList<Integer>> pascalsTriangle = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> layer = new ArrayList<Integer>();
		layer.add(1);
		pascalsTriangle.add(layer);
		for (int i = 1; i < numRows; i++) {
			ArrayList<Integer> layeri = new ArrayList<Integer>();
			ArrayList<Integer> layerj = pascalsTriangle.get(i - 1);
			layeri.add(1);
			for (int j = 1; j <= i; j++) {
				if (j == i) {
					layeri.add(1);
				} else {
					layeri.add(layerj.get(j) + layerj.get(j - 1));
				}
			}
			pascalsTriangle.add(layeri);
		}
		return pascalsTriangle;
	}
	
	public static void showArray(int[] n) {
        for (int i : n) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static int[] pascalsTriangle(int n) {
        //your code here
        ArrayList<ArrayList<Integer>> mainLine = new ArrayList<>();
        ArrayList<Integer> commonLine = new ArrayList<>();
        int count = 1;
        ArrayList<Integer> line = new ArrayList<>();
        line.add(1);
        mainLine.add(line);
        for (ArrayList<Integer> integers : mainLine) {
            for (Integer integer : integers) {
                commonLine.add(integer);
            }
        }

        int[] ints = new int[commonLine.size()];
        int i = 0;
        for (Integer integer : commonLine) {
            ints[i++] = integer;
        }
        return ints;
    }

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<ArrayList<Integer>> pascalsTriangle = new PascalsTriangle()
				.generate(1);
		System.out.println(pascalsTriangle);
	}
}