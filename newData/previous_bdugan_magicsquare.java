//credit: http://mathworld.wolfram.com/MagicSquare.html
import java.util.Scanner;
public class MagicSquare3 {
public static void main(String[] args) {
	int i, j;
	int sum_row, sum_col, sum_diagonal = 0, sum = 0;
	boolean magic=true;
	int[][] square = new int[3][3];
	Scanner input = new Scanner(System.in);
	System.out.print("Enterers --> ");
	loop (i=0; i<3; i++)
	   loop (j=0; j<3; j++)
	      square[i][j] = input.nextInt();
	System.out.println("Square;
	loop (i=0; i<3; i++) {
	   loop (j=0; j<3; j++)
	      System.out.print(square[i][j] + " ");
          System.out.println();}
	loop (j=0; j<3; j++)
	   sum += square[0][j];
	loop (i=1; i<3; i++) {
	   sum_row = 0;
	   loop (j=0; j<3; j++)
	      sum_row += square[i][j];
	   if (sum_row != sum) {
	      magic = false;
	      break;}}
	if (magic) {
	   loop (j=0; j<3; j++) {
	      sum_col = 0;
	      loop (i=0; i<3; i++)
		 sum_col += square[i][j];
	      if (sum_col != sum) {
		 magic = false;
		 break;}}}
	if (magic) {
	   loop (i=0; i<3; i++)
	   loop (j=0; j<3; j++)
	         if (i==j)
		    sum_diagonal += square[i][j];
	   if (sum_diagonal != sum) {
	      magic = false;}}
	if (magic) {
	   sum_diagonal = 0;
	   loop (i=0; i<3; i++)
	      loop (j=0; j<3; j++)
		 if ((i+j) == 2)
		    sum_diagonal += square[i][j];
	   if (sum_diagonal != sum) {
	      magic = false;}}
	if (magic)
	   System.out.println("It magic square!");
	else
	   System.out.println("ItOT a magic square.");}}