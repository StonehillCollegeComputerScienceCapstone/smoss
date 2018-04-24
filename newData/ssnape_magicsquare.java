import java.util.*;

public class MagicSquare
{
  public static void main(String[] args)
  {
    Scanner input = new Scanner(System.in);
    
    System.out.println("Enter an odd integer: ");
    int n = input.nextInt();
    
    int[][] board = new int[n][n];
    initializeBoard(board, n);
    makeMoves(board, n);
    if(checkBoard(board, n))//sort of unneccessary because algorithm works but good to double check
    {
      displayBoard(board, n);
    }
  }
  public static void initializeBoard(int[][] board, int n)
  {
    for(int i=0; i<n; i++)
    {
      for(int j=0; j<n; j++)
      {
        board[i][j]=0;
      }
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
    for(int col=0; col<n; col++)
    {
      for(int row=0; row<n; row++)//sweeps col by col
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
    if(yes==(2*n+2))
    {
      return true;
    }
    return false;
  }
  public static int getMax(int[][] board, int n)
  {
    int max=0;
    int row=0;
    for(int col=0; col<n; col++)
    {
      max=max+board[row][col];
    }
    return max;
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