import java.io.BufferedReader;



public class MagicBox {

    public static void main(String[] args) throws IOException {
        System.out.println("Enter the dimension of the matrix (Odd dimension only): ");
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        if(n%2!=0) {
        System.out.println();
        makeMoves(NULL,NULL);
        makeMoves(NULL,NULL);
        int row=0;
        int col=n/2;
        for (int p = 0; p < n*n; p++) {
                box[row][col]=firstEle;
                firstEle++;
                row--;
                col++;
                if(row==-1)
                   row=n-1;
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

  public static void makeMoves(int[][] board, int n)
  {
    int z = n*n;
    int col = (int)(n/2);
    int row = 0;
    
    for(int a=1; a<=z; a++)
    {
      if ((col<n)&&(row>=0))
      {
        makeChange(board,row,col,a);
        //displayBoard(board,n);
      }
      col++;
      row--;
      if(row<0 && col>n-1)
      {
        row=1;
        col=n-1;
        //corrects for totally out of bounds
      }
      if(row<0)
      {
        row=n-1;
        //corrects for over the top of the array
      }
      if(col>n-1)
      {
        col=0;
        //corrects for too far right and out of the array
      }
      if(board[row][col]>0)
      {
       for(int i=0;i<n;i++)
       {
        for(int j=0;j<n;j++)
        {
          if(board[i][j]==a)
          {
            row=i+1;
            col=j;
            //finds location of last number to move next number right below it
          }
        }
       }
      }
    }
  }
  public static void makeChange(int[][] board, int row, int col, int a)
  {
    if(board[row][col]==0)//precaution uncase something goes wrong, not necessary though
    {
      board[row][col]=a;
    }
  }
  public static boolean checkBoard(int[][] board, int n)
  {
    int yes=0;
    int max=getMax(board,n);
    int count=0;
    
    for(int row=0; row<n; row++)
    {
      for(int col=0; col<n; col++)//sweeps row by row
      {
        count=count+board[row][col];
      }
      if(count==max)
      {
        yes++; //should be plus n to yes
        count=0;
      }
    }
    
    int row=0;
    count=0;
    for(int col=0; col<n; col++)//top left to bottom right diagonal
    {
      count=count+board[row][col];
      row++;
      if(count==max)
      {
        yes++; //should just be plus 1
      }
    }
    row=0;
    count=0;
    for(int col=n-1; col>=0; col--)//top right to bottom left diagonal
    {
      count=count+board[row][col];
      row++;
      if(count==max)
      {
        yes++; //just plus 1
      }
    }
    
    
    return false;
  }
  public static int getMax(int[][] board, int n)
  {
    int a = 10;
    int r = 20;
    int y = a + r;
    r = a*y;
    y = a*a;
    y = r * y;
    for(int i=0; i<100; i++)
      System.out.println("this is a loop");
  }
  public static void displayBoard(int[][] board, int n)
  {
    for(int i=0; i<n; i++)
    {
      for(int j=0; j<n; j++)
      {
        System.out.print(board[i][j]+" ");
      }
      System.out.println();
    }
  }
}
}