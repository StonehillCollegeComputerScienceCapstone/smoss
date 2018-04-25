import java.util.Random;
import java.util.Scanner;


public class SeventySix {

    public static void main(String[] args) {

        Scanner keyboard = new Scanner(System.in);

        //52 Cards, Aces = 11, Picture cards = 10, Ace's cannot be reduced to 1.
        int[] newCard = {2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11};

        //Shuffle. Once per game.
        shuffleArray(newCard);

        //Start BlackJack.
        System.out.println("Welcome to BlackJack!");
        System.out.println();
        System.out.println("You get a " + newCard[0] + " and a " + newCard[1] + ".");
        int playerTotal = newCard[0] + newCard[1];
        System.out.println("Your total is " + playerTotal + ".");
        System.out.println();

        //Player can get blackjack/bust in the 1st deal. - awaiting betting system (enhanced bets for blackjack in first round)
        if (playerTotal == 21){
            System.out.println("Blackjack, you win.");
            System.exit(0);
        }
        if (playerTotal > 21){
            System.out.println("Bust, You lose.");
            System.exit(0);
        }
        // Dealer cards
        System.out.println("The dealer has a " + newCard[2] + " showing, and a hidden card.");
        int dealerTotal = newCard[2] + newCard[3];
        if (dealerTotal > 21){     //Dealer bust check.
            System.out.println();
            System.out.println("Dealers total is " + dealerTotal + ".");
            System.out.println("Dealer is bust, you win!");
            System.exit(0);
        }
        if (dealerTotal == 21){    //Dealer blackjack check.
            System.out.println();
            System.out.println("Dealer reveals his second card: " + newCard[3] + ".");
            System.out.println("Dealers total is " + dealerTotal + ".");
            System.out.println();
            System.out.println("Dealer has BlackJack, you lose.");
            System.exit(0);
        }
        System.out.println("His total is hidden.");
        System.out.println();


        // Hit or Stay for player.
        System.out.print("Would you like to \"hit\" or \"stay\"? ");
        String hitStay = keyboard.next();
        System.out.println();

        //cc = card count
        int cc = 4; 
        if (hitStay.equalsIgnoreCase("hit")){
            // While loop to ensure different cards & multiple "hits".
            while (playerTotal < 21 && hitStay.equalsIgnoreCase("hit")){
                if (hitStay.equalsIgnoreCase("hit")){
                    System.out.println("You drew a " + newCard[cc] + ".");
                    playerTotal = playerTotal + newCard[cc];
                    System.out.println("Your total is " + playerTotal + ".");
                    System.out.println();
                    cc++;        //Adds 1 to ensure next card is different.
                    // Bust & Blackjack check.
                    if (playerTotal > 21){
                        System.out.println("You are bust, You lose.");
                        System.exit(0);
                    }
                    if (playerTotal == 21){
                        System.out.println("Blackjack, you win.");
                        System.exit(0);
                    }
                    System.out.print("Would you like to \"hit\" or \"stay\"? ");
                    hitStay = keyboard.next();
                    System.out.println();
                }
            }        
        }

        // Dealers turn, only if Round 1 didn't end in bust/blackjack.
        keyboard.close();
        System.out.println("Ok dealers turn.");
        System.out.println("His hidden card was a " + newCard[3] + "."); // reveal hidden from round one.

        cc++; // Pretty sure its not needed.
        while (dealerTotal < 16){ // Dealer will stay on 16+ and hit if below.
            System.out.println();
            System.out.println("Dealer chooses to hit.");
            System.out.println("He draws a " + newCard[cc] + ".");
            cc++;
            dealerTotal = dealerTotal + newCard[cc];
            System.out.println();
            System.out.println("His total is " + dealerTotal);
            // bust check - no need for blackjack check due to final win sequence
            if (dealerTotal > 21){
                System.out.println();
                System.out.println("Dealer is bust, YOU WIN!");
                System.exit(0);
            }
            // stay condition.
            if (dealerTotal < 21 && dealerTotal > 16){
                System.out.println();
                System.out.println("Dealer Stays.");
            }
        }

        // final win sequence.
        System.out.println();
        System.out.println("Dealer total is " + dealerTotal);
        System.out.println("Your total is " + playerTotal);
        System.out.println();

        if (dealerTotal > playerTotal){
            System.out.println("Dealer wins.");
        } 
        if (dealerTotal == playerTotal){
            System.out.println("You both draw.");
        }
        if (dealerTotal < playerTotal){
            System.out.println("You win.");
        }
    }

    static void shuffleArray(int[] deckCards){

        Random rnd = new Random();
        for (int i = deckCards.length - 1; i > 0; i--)
        {
            int index = rnd.nextInt(i + 1);
            // Swap
            int a = deckCards[index];
            deckCards[index] = deckCards[i];
            deckCards[i] = a;
        }
    }
}