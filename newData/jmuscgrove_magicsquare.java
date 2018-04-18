// credit: https://stackoverflow.com/questions/36040292/creating-a-magic-square-in-java/36040493

public class MagicSquare {


public static void main(String[] args) {

    System.out.print("Give an odd number: ");
    int n = console.nextInt();
    int[][] magicSquare = new int[n][n];

    int number = 1;
    int row = 0;
    int column = n / 2;
    int curr_row;
    int curr_col;
    while (number <= n * n) {
        magicSquare[row][column] = number;
        number++;
        curr_row = row;
        curr_col = column;
        row -= 1;
        column += 1;
        if (row == -1) {
            row = n - 1;
        }
        if (column == n) {
            column = 0;
        }
        if (magicSquare[row][column] != 0) {
            row = curr_row + 1;
            column = curr_col;
            if (row == -1) {
                row = n - 1;
            }
        }
    }

    for (int i = 0; i < magicSquare.length; i++) {
        for (int j = 0; j < magicSquare.length; j++) {
            System.out.print(magicSquare[i][j] + " ");
        }
        System.out.println();
    }
}
}