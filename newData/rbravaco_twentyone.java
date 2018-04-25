import java.util.*;
/**
 * Blackjack
 * @authors Khanh Tran & Victor Lourng
 */
 /* from https://github.com/pixelyunicorn/CIS-1068/blob/master/11%20Lab%20Cards/BlackJack.java */
import java.util.Scanner;

public class BlackJack {
    public static void main(String[] args) {
        int moneytotal;
        int bet;
        boolean playerwins;

        Scanner kbd = new Scanner(System.in);

        System.out.println("Welcome to game of BlackJack");
        System.out.println();

        moneytotal = 100;

        while(true){
             System.out.println("You have " + moneytotal + " dollars.");
           do{
               System.out.println("How much money do you want to bet?");
               bet = kbd.nextInt();
                 if (bet < 0 || bet > moneytotal)
                     System.out.println("Your answer must be between 0 and " + moneytotal + '.');
              } while (bet < 0 || bet > moneytotal);
               //  break;

             playerwins = playBlackJack();

              if (playerwins)
                 moneytotal = moneytotal + bet;
              else
                 moneytotal = moneytotal - bet;
                System.out.println();
              if (moneytotal == 0) {
                 System.out.println("Looks like you've are out of money!");
                 break;
              }
          }

          System.out.println();
         System.out.println("You leave with $" + moneytotal + '.');
       } // end main

   public static boolean playBlackJack(){
       Scanner kbd = new Scanner(System.in);
       Deck deck = new Deck();
       Hand dealerHand = new Hand();   // The dealer's hand.
       Hand userHand = new Hand();     // The user's hand.


          //  Shuffle the deck, then deal two cards to each player. */

          deck.shuffle();
          dealerHand.addCard(deck.dealCard() );
          dealerHand.addCard(deck.dealCard() );
          userHand.addCard(deck.dealCard() );
          userHand.addCard( deck.dealCard() );

          System.out.println();
          System.out.println();

          // Calculate had values

          // Please fix this
          // dealerHand.getValue() == 21
          // userHand.getValue() == 21


          if (dealerHand.getValue() == 21) {
               System.out.println("Dealer has the " + dealerHand.getCard(0).toString()
                                       + " and the " + dealerHand.getCard(1).toString() + ".");
               System.out.println("User has the " + userHand.getCard(0).toString() + " and the " + userHand.getCard(1).toString() + ".");
               System.out.println();
               System.out.println("Dealer has Blackjack.  Dealer wins.");
               return false;
          }
          if (userHand.getValue() == 21) {
               System.out.println("Dealer has the " + dealerHand.getCard(0).toString()
                                       + " and the " + dealerHand.getCard(1).toString() + ".");
               System.out.println("User has the " + userHand.getCard(0).toString()
                                         + " and the " + userHand.getCard(1).toString() + ".");
               System.out.println();
               System.out.println("You have Blackjack.  You win.");
               return true;
          }

          while (true) {
          System.out.println();
          System.out.println();

          System.out.println("Your cards are:");
               for ( int i = 0; i < userHand.getCardCount(); i++ ) {
                  System.out.println("    " + userHand.getCard(i));
               }
               System.out.println("Your total is " + userHand.getValue());
               System.out.println();
               System.out.println("Dealer is showing the " + dealerHand.getCard(0));
               System.out.println();
               System.out.println("Hit (H) or Stand (S)? ");
               char userAction;  // User's response, 'H' or 'S'.
               do {
                  userAction = kbd.next().charAt(0);
                  Character.toUpperCase( userAction );
                  if (userAction != 'H' && userAction != 'S')
                     System.out.println("Please respond H or S:  ");
               } while (userAction != 'H' && userAction != 'S');

               if ( userAction == 'S' ) {
                       // Loop ends; user is done taking cards.
                   break;
               }
               else {  // userAction is 'H'.  Give the user a card.
                       // If the user goes over 21, the user loses.
                   Card newCard = deck.dealCard();
                   userHand.addCard(newCard);
                   System.out.println();
                   System.out.println("User hits.");
                   System.out.println("Your card is the " + newCard);
                   System.out.println("Your total is now " + userHand.getValue());
                   if (userHand.getValue() > 21) {
                       System.out.println();
                       System.out.println("You busted by going over 21.  You lose.");
                       System.out.println("Dealer's other card was the "+ dealerHand.getCard(1));
                       return false;
                   }
               }
          }
          System.out.println();
          System.out.println("User stands.");
          System.out.println("Dealer's cards are");
          System.out.println(" " + dealerHand.getCard(0));
          System.out.println(" " + dealerHand.getCard(1));
          Card dealersHandCard0 = dealerHand.getCard(0);
          Card dealersHandCard1 = dealerHand.getCard(1);
          int dealersHandValue = dealersHandCard0.getValue() + dealersHandCard1.getValue();
          while (dealersHandValue <= 16 && dealerHand.getCardCount() > 0) {
             Card newCard = deck.dealCard();
             System.out.println("Dealer hits and gets the " + newCard);
             dealerHand.addCard(newCard);
             if (dealersHandValue > 21) {
                System.out.println();
                System.out.println("Dealer busted by going over 21.  You win.");
                return true;
             }
          }
          System.out.println("Dealer's total is " + dealersHandValue);

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