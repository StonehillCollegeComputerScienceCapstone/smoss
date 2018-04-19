/*
Christian F Lewis 12.03.17
CS111a Intro to java
Extra Credit Program
*/

import java.util.Scanner;

/* https://fog.ccsf.edu/~cpersiko/cs111a/blackjack.java.html */
public class blackjack
{
     static Scanner scan = new Scanner(System.in);

     public static void main(String[] args)
     {
          int[] deck = new int[4];
          char players_choice;

          System.out.print("Do you want to play blackjack? (y/n): ");
          players_choice = scan.next().charAt(0);

          display(deck, players_choice);
     }
     //passes the card deck "array" and initial answer to play into method

     //and displays the body of the blackjack game in full...

     public static void display(int[] cards, char play)
     {
          char another_card;
          int players_wins = 0, dealers_wins = 0;

          while (move(play))
          {
               //first 2 cards of players hand...

               cards[0] = (int) (Math.random() * 10) + 1;
               cards[1] = (int) (Math.random() * 10) + 1;

               int dealers_card = 0, dealers_total = 0;

               //keeps running count of hands won, dealer vs player...

               System.out.println("\n>>> Player has won " + players_wins + " hands <<<");
               System.out.println(">>> Dealer has won " + dealers_wins + " hands <<<\n");
               System.out.println("First cards: " + cards[0] + ", " + cards[1]);
               cards[3] = cards[0] + cards[1];

               if ((cards[0] == 10 && cards[1] == 1) || (cards[0] == 1 && cards[1] == 10))
     		{
     			System.out.println("\n!!! Blackjack !!! You win!");
     			players_wins = players_wins + 2;
     		     play = answer();

                    if (move(play))
                         System.out.print("\nYou entered: YES\n");
                    else
                         System.out.print("\nYou entered: NO\n");
     		}

               if (!((cards[0] == 10 && cards[1] == 1) || (cards[0] == 1 && cards[1] == 10)))
     		{
     			while (true)
     			{
     				System.out.println("\nTotal: " + cards[3] + "\n");
                         another_card = flop();

                         if (move(another_card))
                              System.out.print("\nYou entered: YES\n");
                         else
                              System.out.print("\nYou entered: NO\n");

     				if (move(another_card))
     				{
     					cards[2] = (int) (Math.random() * 10) + 1;
                              System.out.println("\nCard: " + cards[2]);
     					cards[3] += cards[2];

     					if (cards[3] > 21)
     					{
                                   System.out.print("\nTotal: " + cards[3] + "\n");
                                   System.out.println("\n *** Bust ***");
     						play = answer();
     						dealers_wins = dealers_wins + 1;

                                   if (move(play))
                                        System.out.print("\nYou entered: YES\n");
                                   else
                                        System.out.print("\nYou entered: NO\n");
                                   break;
     					}
     					if (cards[3] == 21)
     					{
                                   System.out.println("\n!!! Blackjack !!! You win!");
     						play = answer();
     						players_wins = players_wins + 1;

                                   if (move(play))
                                        System.out.print("\nYou entered: YES\n");
                                   else
                                        System.out.print("\nYou entered: NO\n");
     						break;
     					}
     				}
     				if (!move(another_card))
     				{
     					if (dealers_total < cards[3])
     					{
     						do
     						{
     							dealers_card = (int) (Math.random() * 10) + 1;
     							dealers_total += dealers_card;

                                        if (dealers_total == 21 || dealers_total > cards[3])
     								break;
     						} while (dealers_total <= 21);

     						if (dealers_total > cards[3] && dealers_total <= 21)
     						{
                                        System.out.println("\nYour total is: " + cards[3]);
     							System.out.println("\nThe dealers total is: " +
     								dealers_total + "  You lose...");
     							dealers_wins = dealers_wins + 1;
     						}
     						else if (dealers_total > 21 || dealers_total < cards[3])
     						{
                                        System.out.println("\nYour total is: " + cards[3]);
     							System.out.println("\nThe dealers total is: " +
     								              dealers_total + "  You win!");
     							players_wins = players_wins + 1;
     						}
     						else if (dealers_total == cards[3])
     						{
                                        System.out.println("\nYour total is: " + cards[3]);
     							System.out.println("\nThe dealers total is: " +
                                                           dealers_total + "  Push...");
     						}
     					}
     					play = answer();
                              System.out.println();

                              if (move(play))
                                   System.out.print("You entered: YES\n");
                              else
                                   System.out.print("You entered: NO\n");
     					break;
     				}
     			}
     		}
               if (!move(play))
     		{
     			System.out.println("\n>>> Player hands won: " + players_wins + " <<<");
     			System.out.println(">>> Dealer hands won: " + dealers_wins + " <<<\n");

     			if (players_wins > dealers_wins)
     				System.out.println("Congratualations! You beat the house!");
     			else if (players_wins < dealers_wins)
     				System.out.println("Sorry, the house won...");
     			else
     				System.out.println("Even break. No winners no losers...");
     		}
          }
     }
     //used in place of asking the player if they want

     //to play another hand, returns a character...

     public static char answer()
     {
          System.out.print("\nDo you want to play again? (y/n): ");
          char next_move = scan.next().charAt(0);
          return next_move;
     }
     //used in place of asking the player if they want

     //another card throughout the program, returns character...

     public static char flop()
     {
          System.out.print("Would you like another card? (y/n): ");
          char a_card = scan.next().charAt(0);
          return a_card;
     }
     //uses a boolean to simplify the condition of the

     //various if statements throughout the program...

     public static boolean move(char x)
     {
          if (x == 'y')
               return true;
          else
               return false;
     }
}