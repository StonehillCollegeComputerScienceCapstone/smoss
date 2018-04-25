package pascalsTriangle;

import java.util.ArrayList;

/*
4       [1,1,1,1,2,1,1,3,3,1]
int example01 = 10;
        int example11 = 1;
        int example21 = 2;
        int example31 = 4;
        int example41 = 6;
 */
public class PascalsTriangle {
    public static void main(String[] args) {
        showArray(pascalsTriangle(10));
        showArray(pascalsTriangle(1));
        showArray(pascalsTriangle(2));
        showArray(pascalsTriangle(4));
        showArray(pascalsTriangle(6));
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
        for (int i = 1; i < n; i++) {
            ArrayList<Integer> lines = new ArrayList<>();
            lines.add(1);
            for (int j = 1; j <= count; j++) {
                int halfOfCount = count % 2 == 0 ? count / 2 : count / 2 + 1;
                if (i != 1 && j <= halfOfCount) {
                    lines.add(mainLine.get(i - 1).get(j - 1) + mainLine.get(i - 1).get(j));
                } else
                    lines.add(lines.get(count - j));
            }
            mainLine.add(lines);
            count++;
        }

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
}