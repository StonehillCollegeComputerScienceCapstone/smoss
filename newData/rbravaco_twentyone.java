public class BlackJack {

    static PairOfDice cards = new PairOfDice();
    static Scanner scan = new Scanner(System. in );
    static int playerScore, dealerScore, player, dealer, tempScore;
    static boolean newGame;
    static String play, hit;


			try {

				if (bw != null)
					bw.close();

				if (fw != null)
					fw.close();

			} catch (IOException ex)

				ex.printStackTrace();


    public static void main(String[] args) {
        newGame();
        dealerRoll();
        playerRoll();

        // checkWinner();
    }

    public static void newGame() {

        System.out.println("Would you like to play blackjack? y or n?");
        play = scan.nextLine();

        if (play == "y"); {
            newGame = true;
        }
        if (play != "y") newGame = false;
    }

    public static void dealerRoll() {
        while (newGame) {
            cards.rollDice();
        }

        dealerScore = (cards.rollDice());
        System.out.println("Dealer score is: " + dealerScore);

        if (dealerScore <= 15 && playerScore > dealerScore) tempScore = cards.rollDice();
        System.out.println("The dice roll was: " + tempScore);
        dealerScore += tempScore;
        System.out.println("Dealer score is: " + dealerScore);

    }

    public static void playerRoll() {
        while (newGame) {
            cards.rollDice();
        }

        playerScore = (cards.rollDice());
} finally {

			try {

				if (bw != null)
					bw.close();

				if (fw != null)
					fw.close();

			} catch (IOException ex) {

				ex.printStackTrace();

        System.out.println("You total is " + playerScore);

        while (playerScore < 21 || playerScore < dealerScore) {

private static boolean magicSquare(int[][] square){

   //calculate the sum of the first row and assign it to n
       int n = sumOfRow(square[0]);

       for (int[] row : square)
       {
          int sum = sumOfRow(row);
          if (sum != n)
          return false;
       }

            }
            else if (hit.equals("n")); {
                checkWinner();
            }
        }
    }

    public static void checkWinner() {
        if (playerScore == 21) System.out.println("You win!");


        else if (dealerScore > 21) System.out.println("Dealer has busted, You win!");
    }
}
          System.out.println();
          if (dealersHandValue == userHand.getValue()) {
             System.out.println("Dealer wins on a tie.  You lose.");
             return false;
          }
          else if (dealersHandValue > userHand.getValue()) {
             System.out.println("Dealer wins, " + dealersHandValue
                              + " points to " + userHand.getValue() + ".");
             return false;
          }
          else {
             System.out.println("You win, " + userHand.getValue() + " points to " + dealersHandValue + ".");
             return true;
          }
       }
    }
    }