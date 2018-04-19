import java.util.Scanner;
import java.util.*;
/* https://stackoverflow.com/questions/21394716/beginners-blackjack-game-using-loops*/
public class BlackjackGame {

    public static void main(String[] args) {

        String anotherCard, playAgain = "y", ctn;
        int nextCard, card1, card2, dCard1, dCard2;
        int cardTotal = 0, dTotal = 0;

        Scanner keyboard = new Scanner(System.in);

        Random random = new Random();

        // Begin dealing the players first two cards

        while (playAgain == "y")
        {
            //dealers first two random cards
            dCard1 = random.nextInt(10) + 1;
            dCard2 = random.nextInt(10) +1;

            //players first two random cards and card total
            card1 = random.nextInt(10) + 1;
            card2 = random.nextInt(10) + 1;
            cardTotal = card1 + card2;

            //Dealers two card total and display only one dealer card
            dTotal = dCard1 + dCard2;
            System.out.println("Dealer shows: " + dCard1);

            //Display players first two cards & card total
            System.out.println("First Cards: " + card1 + ", " +card2);
            System.out.println("Total: "+ cardTotal);

            System.out.print("Another Card (y/n)?: ");
            anotherCard = keyboard.nextLine();

            while (anotherCard == "y")
            {
                nextCard = random.nextInt(10) + 1;
                cardTotal += nextCard;
                System.out.println("Card: " + nextCard);
                System.out.println("Total: " + cardTotal);

                if (cardTotal > 21)
                {
                System.out.println("You busted, Dealer Wins");
                System.out.println("Do you want to play again? (y/n): ");
                playAgain = keyboard.nextLine();
                }
                if (cardTotal < 21)

                System.out.print("Another Card (y/n)?: ");
                anotherCard = keyboard.nextLine();
                if (anotherCard == "n")
                System.out.print("Press c to continue dealers cards");
                ctn = keyboard.nextLine();


                while (ctn == "c" && dTotal < 17)
                {
                    nextCard = random.nextInt(10) + 1;
                    dTotal += nextCard;

                    if (dTotal > 21)
                    {
                    System.out.println("Dealer Busts, You Win!");
                    System.out.println("Play Again? (y/n): ");
                    playAgain = keyboard.nextLine();
                    if (playAgain.equalsIgnoreCase("y"))
                            playAgain = "y";
                        else
                            System.exit(0);
                    }

                }

            }

        }
    }
}