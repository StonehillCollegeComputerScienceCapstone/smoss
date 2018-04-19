// credit: https://www.java-forums.org/new-java/50650-checking-2d-arrays-determine-if-they-magic-squares-all-sums-same.html
public class MagicSquare {

    public static boolean allNumbers(int[][] arrTwoD) {
        int[] numbers = new int[arrTwoD.length * arrTwoD.length];
        boolean flag = true;
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = 0;
        }
        for (int j = 0; j < arrTwoD.length; j++) {
            for (int k = 0; k < arrTwoD[j].length; k++) {
                int m = arrTwoD[j][k];
                if (m < 1 || m > arrTwoD.length * arrTwoD.length) {
                    flag = false;
                } else if (numbers[m - 1] == 0) {
                    numbers[m - 1] = 1;
                } else if (numbers[m - 1] == 1) {
                    flag = false;
                }
            }
        }
        return flag;
    }

    public static int sumLRDiag(int[][] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum = arr[i][i] + sum;
        }
        return sum;
    }

    public static int sumRLDiag(int[][] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum = sum + arr[i][arr.length - 1 - i];
        }
        return sum;
    }

    public static int sumRow(int[][] arr, int i) {
        int sum = 0;
        for (int j = 0; j < arr[i].length; j++) {
            sum = sum + arr[i][j];
        }
        return sum;
    }

    public static int sumCol(int[][] arr, int j) {
        int sum = 0;
        for (int i = 0; i < arr[j].length; i++) {
            sum = sum + arr[i][j];
        }
        return sum;
    }

    public static void main(String[] args) {
        int[][] arr = {{16, 2, 3, 5}, {13, 11, 10, 8},
            {9, 7, 6, 12}, {4, 14, 15, 1}};
        boolean flag = allNumbers(arr);
        if (flag == true) {
            int value = sumLRDiag(arr);
            if (sumRLDiag(arr) != value) {
                flag = false;
            } else {
                for (int i = 0; i < arr.length; i++) {
                    int sum = sumRow(arr, i);
                    if (sum != value) {
                        flag = false;
                    }
                }
                if (flag == true) {
                    for (int j = 0; j < arr.length; j++) {
                        int sum = sumCol(arr, j);
                        if (sum != value) {
                            flag = false;
                        }
                    }
                }
            }
        }
        if (flag == true) {
            System.out.println("The matrix contains a perfect square.");
        } else {
            System.out.println("The matrix is not a perfect square.");
        }
    }
}