/**
 * Pascal's Triangle
 * @author Jeffrey Wang
 * @license - may be used for educational purposes ONLY, excluding editing of this code
*/
import java.math.*;
import java.io.*;
import java.util.*;

class PascalsTriangle {
  public static void main ( String[] args ) {
    Scanner s = new Scanner ( System.in );
    System.out.println ( "Pascal's Triangle" );
    System.out.println ( "n = " );
    int n = s.nextInt();
    PascalsTriangle pt = new PascalsTriangle( n );
    System.out.println ( pt );
  }

  int[][] grid;
  public PascalsTriangle ( int n ) {
    grid = new int[n][n];
    for ( int[] irow : grid ) {
      for ( int icol : irow ) {
        icol = 0;
      }
    }
    this.ptgen ( n );
  }
  public void ptgen ( int n ) {
    grid[0][0] = 1;
    this.ptrow ( 1, n );
  }
  public void ptrow ( int start, int end ) {
    if ( start == end ) {
      // nothing much, just let it die
    } else {
      grid[start][0] = 1;
      grid[start][start] = 1;
      //if ( start == 2 ) {
      //  grid[2][1] = 2;
      //} else {
        for ( int i = 1; i < start; i++ ) {
          grid[start][i] = grid[start-1][i-1] + grid[start-1][i];
        }
      //}
      this.ptrow ( start + 1 , end );
    }
  }
  public String toString () {
    String output = "";
    for ( int i = 0; i < grid.length; i++ ) {
      //for ( int k = 0; k < i / 2; k++ ) {
      //  output += " ";
      //}
      for ( int j = 0; j < grid[0].length; j++ ) {
        if ( grid[i][j] != 0 ) {
          output += "" + grid[i][j] + " ";
        }
      }
      output += "\n";
    }
    return output;
  }
  
          for (int r=0; r<tri.length; r++) {
                tri[r] = new int[r+1];
                tri[r][0] = 1;
                tri[r][r] = 1;
                for (int c=1; c<r; c++) {
                        tri[r][c] = tri[r-1][c]+tri[r-1][c-1];
                        }
                }

        for (int r=0; r<tri.length; r++) {
                for (int c=0; c<tri[r].length; c++) {
                        System.out.print(" "+tri[r][c]);
                }
                System.out.println("");
                }
        }
}