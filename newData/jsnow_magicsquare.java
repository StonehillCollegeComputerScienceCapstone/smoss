import java.util.Scanner;  

//importing Array tools
import java.util.Arrays;

public class TestProject3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        //a strings type variable used to store text
        String textvar = "";
        //flag which determines whether sqr array is filled with numbers
        boolean existingsqr = false;
        //array for storing magic square
        int [] [] sqr = new int [3][3];
        //used in for cycles
        int sqrsize = sqr.length;
        //creating new scanner object which takes InputStream as parameter
        Scanner in = new Scanner(System.in);
        
        do
        { 
            System.out.println("Input \"new\" to start filling new 3x3 square");
            if(existingsqr)System.out.println("Input \"show\" to display existing square");      
            if(existingsqr)System.out.println("Input \"info\" to display info about existing square");      
            System.out.println("Input \"quit\" for exiting the application");
                 
            textvar = in.nextLine();
            if("new".equals(textvar))
            {
                System.out.println("Input 9 numbers ");
                
                for (int i = 0; i < sqrsize; i++)
                {
                    for (int j = 0; j < sqrsize; j++)
                    {
                        System.out.println("Input value for row " + (i+1) + " column " + (j+1));
                        sqr[i][j] = in.nextInt();
                    }
                }
                existingsqr = true;
                System.out.println("Thanks!");
                System.out.println();  
            }  
            else if("show".equals(textvar) && existingsqr)
            {
                System.out.println("Current square:");
                System.out.println(sqr[0][0]+" " +sqr[0][1]+" " +sqr[0][2]);
                System.out.println(sqr[1][0]+" " +sqr[1][1]+" " +sqr[1][2]);
                System.out.println(sqr[2][0]+" " +sqr[2][1]+" " +sqr[2][2]);               
            }
            else if("info".equals(textvar) && existingsqr)
            {                
                int[] sums_rows = new int[sqrsize];
                Arrays.fill(sums_rows, 0);
                                
                int[] sums_columns = new int[sqrsize];
                Arrays.fill(sums_columns, 0);
                
                int[] sums_diagonals = new int[2];
                Arrays.fill(sums_diagonals, 0);

                for (int i = 0; i < sqrsize; i++) {
                    for (int j = 0; j < sqrsize; j ++) {
                        sums_rows[i] += sqr[i][j];
                    }
                    System.out.println("the sum of elements of row " + (i+1) + " :\n" + sums_rows[i]);
                }
                for (int j = 0; j < sqrsize; j++) {
                    for (int i = 0; i < sqrsize; i ++) {
                        sums_columns[j] += sqr[i][j];
                    }
                    System.out.println("the sum of elements of column " + (j+1) + " :\n" + sums_columns[j]);
                }
                
                for (int i = 0; i < sqrsize; i++) {
                    sums_diagonals[0] += sqr[i][i];
                }
                System.out.println("the sum of diagonal 1 " + "\n" + sums_diagonals[0]);
                
                for (int i = 0; i < sqrsize; i++) {
                    sums_diagonals[1] += sqr[i][(sqrsize-1)-i];
                }
                System.out.println("the sum of diagonal 2 " + "\n" + sums_diagonals[1]);
                
                boolean isMagicSquare = true;
                
                int comparedSum = sums_rows[0];
                for (int i = 1; i < sqrsize; i++) {
                  isMagicSquare = isMagicSquare && (comparedSum == sums_rows[i]);
                }
                for (int i = 0; i < sqrsize; i++) {
                  isMagicSquare = isMagicSquare && (comparedSum == sums_columns[i]);
                }
                for (int i = 0; i < 2; i++) {
                  isMagicSquare = isMagicSquare && (comparedSum == sums_diagonals[i]);
                }

                if(isMagicSquare)
                    System.out.println("All sums are equal, this is a magic square");
                else
                    System.out.println("The sums are not equal, so this isn't a magic square");    
                
                System.out.println();  
            }
            else if(!"quit".equals(textvar))
            {
                //cleans screen by pushing text off screen
                for(int clear = 0; clear < 1000; clear++)
                {
                    System.out.println("\b") ;
                }
            }
        }        
        while (!"quit".equals(textvar)); 
        //loop will repeat until textvar reaches the necessary value
    }
    
}