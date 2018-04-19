 // credit: https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/

 import java.util.Scanner;


 class MagicSquare{

static int[] grid = new int[9];

public static void main(String[] args){

    Scanner keyboard = new Scanner(System.in);
    System.out.println("Enter The 9 Numbers of The Square in Order: "); //Takes 9 numbers with a space in between each

    String nums = keyboard.nextLine();

    for(int i = 0; i < 9; i++){
    grid[i] = Integer.parseInt(nums.substring(i * 2, i * 2 + 1));
    }

    System.out.println(checkSquare(grid) ? "true" : "false");

}

public static boolean checkSquare(int[] grid){ //takes an array of integers assuming a 3 x 3 square
                                        //and checks if it is magic
    for(int i = 0; i < 9; i++){
        if( (i % 3 == 0 && grid[i] + grid[i + 1] + grid[i + 2] != 15)
        ||  (i < 3 && grid[i] + grid[i + 3] + grid[i + 6] != 15)
        ||  grid[0] + grid[4] + grid[8] != 15
        ||  grid[2] + grid[4] + grid[6] != 15) return false;
    }
    return true;
}
}