import java.Util.Scanner;
02
 
03
public class MagicSquare
04
{
05
 
06
    public static void main (String[] args)
07
    {
08
        Scanner sc= new scanner (System.in);
09
        System.out.print (" Enter dimension:");
10
        int dimension =sc.nextInt();
11
        System.out.print (" Enter row 1:");
12
        int row1 =sc.nextInt();
13
        System.out.print (" Enter row 2:");
14
        int row2 =sc.nextInt();
15
        System.out.print (" Enter row 3:");
16
        int row3 =sc.nextInt();
17
 
18
 
19
 
20
        int N = Integer.parseInt(args[0]);
21
        if (N % 2 == 0) throw new RuntimeException("N must be odd");
22
 
23
        int[][] magic = new int[N][N];
24
 
25
        int row = N-1;
26
        int col = N/2;
27
        magic[row][col] = 1;
28
 
29
        for (int i = 2; i <= N*N; i++) {
30
            if (magic[(row + 1) % N][(col + 1) % N] == 0) {
31
                row = (row + 1) % N;
32
                col = (col + 1) % N;
33
            }
34
            else {
35
                row = (row - 1 + N) % N;
36
                 
37
            }
38
            magic[row][col] = i;
39
        }
40
 
41
         
42
        for (int i = 0; i < N; i++) {
43
            for (int j = 0; j < N; j++) {
44
                if (magic[i][j] < 10)  System.out.print(" "); 
45
                if (magic[i][j] < 100) System.out.print(" "); 
46
                System.out.print(magic[i][j] + " ");
47
            }
48
            System.out.println();
49
        }
50
 
51
    }
52
}
