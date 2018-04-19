// credit: http://www.dreamincode.net/forums/topic/138723-java-check-magic-square/

public class MagicSquare{
    static int rowSum1;
    static int rowSum2;
    static int rowSum3;
    static int rowSum4;

    static int columnSum1;
    static int columnSum2;
    static int columnSum3;
    static int columnSum4;

    public static void main(String [] args)
    {
        int square[][]={{16,3,2,13},
            {5,10,11,8},
            {9,6,7,12},
            {4,15,14,1}};

        // get each rows total
        for (int i =0; i < 4;i++){
            rowSum1 += square[0][i];
        }

        for (int i =0; i < 4;i++){
            rowSum2 += square[1][i];
        }

        for (int i =0; i < 4;i++){
            rowSum3 += square[2][i];
        }

        for (int i =0; i < 4;i++){
            rowSum4 += square[3][i];
        }

        // get each columns totals
        for (int i =0; i < 4;i++){
            columnSum1 += square[i][0];
        }


        for (int i =0; i < 4;i++){
            columnSum2 += square[i][1];
        }

        for (int i =0; i < 4;i++){
            columnSum3 += square[i][2];
        }

        for (int i =0; i < 4;i++){
            columnSum4 += square[i][3];
        }

        // print out, just to make sure it's working correctly
        System.out.println(rowSum1);
        System.out.println(rowSum2);
        System.out.println(rowSum3);
        System.out.println(rowSum4 + "\n");

        System.out.println(columnSum1);
        System.out.println(columnSum2);
        System.out.println(columnSum3);
        System.out.println(columnSum4);

        if ((rowSum1 == rowSum2) && (rowSum1 == rowSum3) && (rowSum1 == rowSum4) && (rowSum1 == columnSum1)
                && (rowSum1 == columnSum2) && (rowSum1 == columnSum3) && (rowSum1 == columnSum4)){
            System.out.println("Congradulations, you have a magic square!!!!");
        } else {
            System.out.println("You Fail!!!!!!");
        }
    }
}