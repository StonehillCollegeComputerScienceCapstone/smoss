public class BlackJack {

    static PairOfDice cards = new PairOfDice();
    static Scanner scan = new Scanner(System. in );
    static int playerScore, dealerScore, player, dealer, tempScore;
    static boolean newGame;
    static String play, hit;


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

        System.out.println("You total is " + playerScore);

        while (playerScore < 21 || playerScore < dealerScore) {

            System.out.println("Would you like to take a hit? y or n?");
            hit = scan.nextLine();
            if (hit.equals("y")) {
                tempScore = cards.rollDice();
                System.out.println("The dice roll was: " + tempScore);
                playerScore += tempScore;
                System.out.println("Your score is now: " + playerScore);

            }
            else if (hit.equals("n")); {
                checkWinner();
            }
        }
    }

    public static void checkWinner() {
        if (playerScore == 21) System.out.println("You win!");
        else if (dealerScore == 21) System.out.println("Sorry, Dealer has won!");
        else if (dealerScore > playerScore) System.out.println("Sorry, Dealer has won!");
        else if (playerScore > dealer) System.out.println("You win!");
        else if (playerScore > 21) System.out.println("Sorry you busted, Dealer has won!");

        else if (dealerScore > 21) System.out.println("Dealer has busted, You win!");
    }
}​