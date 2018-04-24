import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MagicSquare {

    public static void main(String[] args) throws IOException {
        System.out.println("Enter the dimension of the matrix (Odd dimension only): ");
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        if(n%2!=0) {
        int box[][]=new int[n][n];
        System.out.println("Enter the first element:");
        int firstEle=Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                box[i][j]=0;
            }
        }
        int row=0;
        int col=n/2;
        for (int p = 0; p < n*n; p++) {
                box[row][col]=firstEle;
                firstEle++;
                row--;
                col++;
                if(row==-1)
                   row=n-1;
                if(col==n)
                   col=0;
                if(row==n-1 && col==0)
                {
                    row=1;
                    col=n-1;
                }
              if((box[row][col]!=0)) {
                   row+=2;
                   col--;
                 if(row&gt;n) row=0;
                if(col==-1) col=0;
            }
        }
        System.out.println("Magic Box");
         for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(box[i][j]/10==0)
                    System.out.print( box[i][j]+"    ");
                else
                    System.out.print( box[i][j]+"   ");
            }
             System.out.println("");
        }
    }
}
}