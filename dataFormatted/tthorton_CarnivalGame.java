import java.util.*;
public class CarnivalGame {

	public static int dieRoll(int x){
		
		int y = 1+(int)(Math.random()*x-1);
		return y;
	}
	public static void main(String[] args) {
		Scanner k = new Scanner(System.in);
		int x = 1;
		int loop = 0;
		System.out.println("Welcome to the fantastically amazingly astounding carnival game!");
		while(x==1)
		{
			if(loop==0){
			System.out.println("Would you like to roll your chances against lady luck? (Type '1' to play).");
			x = k.nextInt();}
			if(x==1)
			{
				System.out.println("Here we go! Your rolls are...");
				//6,20,8,4,12
				int six = dieRoll(6);
				int twenty = dieRoll(20);
				int eight = dieRoll(8);
				int four = dieRoll(4);
				int twelve = dieRoll(12);
				System.out.println(six+" on a 6-sided dice...");
				System.out.println(twenty+" on a 20-sided dice...");
				System.out.println(eight+" on a 8-sided dice...");
				System.out.println(four+" on a 4-sided dice...");
				System.out.println(twelve+" on a 12-sided dice...");
				
				if(six+twenty+eight+four+twelve>35||six+twenty+eight+four+twelve<20)
				{
					System.out.println("You win! Want to play again? (Type '1' to play again).");
					x = k.nextInt();
					loop++;
				}
					else
					{
						System.out.println("You lost! Want to try again? (Type '1' to try again).");
						x = k.nextInt();
						loop++;
					}
			}
		}
		k.close();
	}

}
