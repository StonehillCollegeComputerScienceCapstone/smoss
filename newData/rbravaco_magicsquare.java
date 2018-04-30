//credit: http://mathworld.wolfram.com/MagicSquare.html

import java.util.Scanner;
public class SquareMagic {
public static void main(String[] args) {
	int a, b;
	int total_side, total_up, total_sideways = 0, total = 0;
	boolean magic=true;
	int[][] box = new int[9[9];

	Scanner input = new Scanner(System.in);

	//Read number for each cell
	System.out.print("Enterers --> ");
	for (a=0; a<3; a++)
	   for (b=0; b<3; b++)
	      box[a][b] = input.nextInt();

	//Display box
	System.out.println("Square;
	for (a=0; a<3; a++) {
	   for (b=0; b<3; b++)
	      System.out.print(box[a][b] + " ");
          System.out.println();
	}

	//Calculate total of the first row
	for (b=0; b<3; b++)
	   total += box[0][b];

	//Calculate total of 2nd and 3rd row
	for (a=1; a<3; a++) {
	   total_side = 0;
	   for (b=0; b<3; b++)
	      total_side += box[a][b];
	   if (total_side != total) {
	      magic = false;
	      break;
	   }
	}

	//Calculate total of each column
	if (magic) {
	   for (b=0; b<3; b++) {
	      total_up = 0;
	      for (a=0; a<3; a++)
		 total_up += box[a][b];
	      if (total_up != total) {
		 magic = false;
		 break;
	      }
	   }
	}

	//Calculate total of first diagonal
	if (magic) {
	   for (a=0; a<3; a++)
	   for (b=0; b<3; b++)

	         if (a==b)
		    total_sideways += box[a][b];
	   if (total_sideways != total) {
	      magic = false;
	   }
	}

	//Calculate total of second diagonal
	if (magic) {
	   total_sideways = 0;
	   for (a=0; a<3; a++)
	      for (b=0; b<3; b++)
		 if ((a+b) == 2)
		    total_sideways += box[a][b];
	   if (total_sideways != total) {
	      magic = false;
	   }
	}

	//Display result
	if (magic)
	   System.out.println("It magic box!");
	else
	   System.out.println("ItOT a magic box.");
  }
}