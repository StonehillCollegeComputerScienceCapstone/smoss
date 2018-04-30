import java.util.*;
/* https://www.daniweb.com/programming/software-development/threads/426381/blackjack-code-review-beginner */
public class BlackJack {
public static void main(String[] args) {

    Scanner kb = new Scanner(System.in);
    int playerDecision = 0;
    int playerTotal = 0;
    int dealersTotal = 0;
    String[] card = { "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"};
    ArrayList<String> playergame = new ArrayList<String>();
    ArrayList<String> dealersgame = new ArrayList<String>();
    for (int i = 0; i <= 0; i++) {

    }
        int randomGenNumber = (int) (Math.random()*13);
        dealersgame.add(card[randomGenNumber]);}
    System.out.println("The Dealer Was Dealt: " + dealersgame);
    for (int i = 0; i <= 1; i++) {
        int randomGenNumber = (int) (Math.random()*13);
        playergame.add(card[randomGenNumber]);}
    System.out.println("The User Was Dealt: " + playergame);
    if(playergame.contains("Ace")) {
        if(playergame.contains("King") || playergame.contains("Queen") || playergame.contains("Jack") || playergame.contains("10")){
            System.out.println("You've Got BlackJack! Congratulations, You Win!");
            System.exit(0);} else {System.out.println("You Did Not Get BlackJack!\n[1] Twist\n[2] Stick");}} else {
        System.out.println("You Did Not Get BlackJack! :( \n[1] Twist\n[2] Stick");}
    int x = 0;
    while(x==0) {
        playerDecision = kb.nextInt();
        switch (playerDecision) {
        case 1:
            System.out.println("You've Twisted - Your game: " + playergame);
            System.out.println("You've Twisted - Additional Card Dealt");
            x = 0;
            for (int i = 0; i <= 0; i++) {
                int randomGenNumber = (int) (Math.random()*13);
                playergame.add(card[randomGenNumber]);}
            System.out.println(playergame + "\n");
            playerTotal = 0;
            for(int i = 0; i < playergame.size(); i++) {
                if(playergame.get(i).equals("2")) {
                    playerTotal += 2;} else if(playergame.get(i).equals("3")) {
                    playerTotal += 3;} else if(playergame.get(i).equals("4")) {
                    playerTotal += 4;} else if(playergame.get(i).equals("5")) {
                    playerTotal += 5;} else if(playergame.get(i).equals("6")) {
                    playerTotal += 6;} else if(playergame.get(i).equals("7")) {
                    playerTotal += 7;} else if(playergame.get(i).equals("8")) {
                    playerTotal += 8;} else if(playergame.get(i).equals("9")) {
                    playerTotal += 9;} else if(playergame.get(i).equals("10")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("Jack")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("Queen")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("King")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("Ace")) {
                    playerTotal += 11;}}
               System.out.println("Users game Total: " + playerTotal + "");
            if(playerTotal != 21 && playerTotal <=21){
                System.out.println("You Did Not Get BlackJack!\n[1] Twist\n[2] Stick");} else if (playerTotal == 21) {
                System.out.println("You Got BlackJack! Congratulations!");} else if (playerTotal > 21) {
                System.out.println("You've Bust! You Lose!");
                System.exit(0);}
            break;
        case 2:
            System.out.println("You've Stuck - Your game: " + playergame +"\n");
            x = 1;
            playerTotal = 0;
            for(int i = 0; i <playergame.size(); i++) {
                if(playergame.get(i).equals("2")) {
                    playerTotal += 2;} else if(playergame.get(i).equals("3")) {
                    playerTotal += 3;} else if(playergame.get(i).equals("4")) {
                    playerTotal += 4;} else if(playergame.get(i).equals("5")) {
                    playerTotal += 5;} else if(playergame.get(i).equals("6")) {
                    playerTotal += 6;} else if(playergame.get(i).equals("7")) {
                    playerTotal += 7;} else if(playergame.get(i).equals("8")) {
                    playerTotal += 8;} else if(playergame.get(i).equals("9")) {
                    playerTotal += 9;} else if(playergame.get(i).equals("10")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("Jack")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("Queen")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("King")) {
                    playerTotal += 10;} else if(playergame.get(i).equals("Ace")) {
                    playerTotal += 11;}}
            System.out.println("Dealing Dealers Second Card!");
            for (int i = 0; i <= 0; i++) {
                int randomGenNumber = (int) (Math.random()*13);
                dealersgame.add(card[randomGenNumber]);}
            System.out.println(dealersgame + "\n");
            dealersTotal = 0;
            for(int i = 0; i < dealersgame.size(); i++) {
                if(dealersgame.get(i).equals("2")) {
                    dealersTotal += 2;} else if(dealersgame.get(i).equals("3")) {
                    dealersTotal += 3;} else if(dealersgame.get(i).equals("4")) {
                    dealersTotal += 4;} else if(dealersgame.get(i).equals("5")) {
                    dealersTotal += 5;} else if(dealersgame.get(i).equals("6")) {
                    dealersTotal += 6;} else if(dealersgame.get(i).equals("7")) {
                    dealersTotal += 7;} else if(dealersgame.get(i).equals("8")) {
                    dealersTotal += 8;} else if(dealersgame.get(i).equals("9")) {
                    dealersTotal += 9;} else if(dealersgame.get(i).equals("10")) {
                    dealersTotal += 10;} else if(dealersgame.get(i).equals("Jack")) {
                    dealersTotal += 10;} else if(dealersgame.get(i).equals("Queen")) {
                    dealersTotal += 10;} else if(dealersgame.get(i).equals("King")) {
                    dealersTotal += 10;} else if(dealersgame.get(i).equals("Ace")) {
                    dealersTotal += 11;}}
            int y = 0;
            while(y==0) {
                dealersTotal = 0;
                for(int i = 0; i < dealersgame.size(); i++) {
                    if(dealersgame.get(i).equals("2")) {
                        dealersTotal += 2;} else if(dealersgame.get(i).equals("3")) {
                        dealersTotal += 3;} else if(dealersgame.get(i).equals("4")) {
                        dealersTotal += 4;} else if(dealersgame.get(i).equals("5")) {
                        dealersTotal += 5;} else if(dealersgame.get(i).equals("6")) {
                        dealersTotal += 6;} else if(dealersgame.get(i).equals("7")) {
                        dealersTotal += 7;} else if(dealersgame.get(i).equals("8")) {
                        dealersTotal += 8;} else if(dealersgame.get(i).equals("9")) {
                        dealersTotal += 9;} else if(dealersgame.get(i).equals("10")) {
                        dealersTotal += 10;} else if(dealersgame.get(i).equals("Jack")) {
                        dealersTotal += 10;} else if(dealersgame.get(i).equals("Queen")) {
                        dealersTotal += 10;} else if(dealersgame.get(i).equals("King")) {
                        dealersTotal += 10;} else if(dealersgame.get(i).equals("Ace")) {
                        dealersTotal += 11;}}
                if(dealersTotal <= 16) {
                    int randomGenNumber = (int) (Math.random()*13);
                    dealersgame.add(card[randomGenNumber]);
                    System.out.println("Dealer Has Less Than 17 - Taking Another Card\n");
                    System.out.println("Dealers game: " + dealersgame);
                    dealersTotal = 0;
                    for(int i = 0; i < dealersgame.size(); i++) {
                        if(dealersgame.get(i).equals("2")) {
                            dealersTotal += 2;} else if(dealersgame.get(i).equals("3")) {
                            dealersTotal += 3;} else if(dealersgame.get(i).equals("4")) {
                            dealersTotal += 4;} else if(dealersgame.get(i).equals("5")) {
                            dealersTotal += 5;} else if(dealersgame.get(i).equals("6")) {
                            dealersTotal += 6;} else if(dealersgame.get(i).equals("7")) {
                            dealersTotal += 7; } else if(dealersgame.get(i).equals("8")) {
                            dealersTotal += 8;} else if(dealersgame.get(i).equals("9")) {
                            dealersTotal += 9;} else if(dealersgame.get(i).equals("10")) {
                            dealersTotal += 10;} else if(dealersgame.get(i).equals("Jack")) {
                            dealersTotal += 10;} else if(dealersgame.get(i).equals("Queen")) {
                            dealersTotal += 10;} else if(dealersgame.get(i).equals("King")) {
                            dealersTotal += 10;} else if(dealersgame.get(i).equals("Ace")) {
                            dealersTotal += 11;}}
                    System.out.println("Dealers game Total: " + dealersTotal + "\n");}
                if(dealersTotal == 17 ) {
                    System.out.println("Dealer Has 17 - Dealer Sticks\n");
                    y = 1;
                    if(playerTotal < 17) {
                        System.out.println("You Have: " + playerTotal + " You Lost");} else if(playerTotal == dealersTotal) {
                        System.out.println("You Have: " + playerTotal + " You Drew");} else {
                        System.out.println("You Have: " + playerTotal + " You Won!");}}
                if(dealersTotal > 17 && dealersTotal < 21) {
                    System.out.println("Dealer Has: " + dealersTotal + " Dealer Sticks\n" );
                    y = 1;
                    if(playerTotal < 18) {
                        System.out.println("You Have: " + playerTotal + " You Lost");} else if(playerTotal == dealersTotal) {
                        System.out.println("You Have: " + playerTotal + " You Drew");} else {
                        System.out.println("You Have: " + playerTotal + " You Won!");}}
                if(dealersTotal == 21) {
                    System.out.println("Dealer Has BlackJack\n");
                    y = 1;
                    if(playerTotal == dealersTotal) {
                        System.out.println("You Have: " + playerTotal + " You Drew");} }
                if(dealersTotal > 21) {
                    System.out.println("Dealer Has Busted - You Win!");
                    y = 1; }}
            break;
        default:
            System.out.println("Not A Valid Selection");}};}
