import java.util.*;
public class PascalTriangle 
{

    public static void main(String[] nt) 
    {
          Scanner in=new Scanner(System.in);
          System.out.print("Enter Number of Rows: ");
          int n=in.nextInt();
          int [][] a=new int[n+1][];
          for(int i=0;i<=n;i++)
          {
              a[i]=new int[i+1];                  //jagged array 
          }
          for(int i=0;i<=n;i++)
          {    a[i][0]=1;
               a[i][i]=1;
          }
          for(int i=2;i<=n;i++)
          {
              for(int j=1;j<i;j++)
              {
                  a[i][j]=a[i-1][j-1]+a[i-1][j];
              }
          }
          for(int i=0;i<=n;i++)
          {
              for(int spc=2*n-i;spc>0;spc--)
              {
                  System.out.print(" ");
              }
              for(int j=0;j<=i;j++)
              {  
                  System.out.print(a[i][j]+" "); 
              }
              System.out.println();
          }
    }

}