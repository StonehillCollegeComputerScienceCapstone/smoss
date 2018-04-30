import java.util.*;
/* https://www.daniweb.com/programming/software-development/threads/426381/blackjack-code-review-beginner */
public class BlackJack {
public static void main(String[] args) {

    Scanner kb = new Scanner(System.in);
    int usersDecision = 0;
    int usersValue = 0;
    int dealersValue = 0;
    String[] card = { "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"};
    ArrayList<String> usersCards = new ArrayList<String>();
    ArrayList<String> dealersCards = new ArrayList<String>();
    for (int i = 0; i <= 0; i++) {
        int randomGenNumber = (int) (Math.random()*13);
        dealersCards.add(card[randomGenNumber]);}
    System.out.println("The Dealer Was Dealt: " + dealersCards);
    for (int i = 0; i <= 1; i++) {
        int randomGenNumber = (int) (Math.random()*13);
        usersCards.add(card[randomGenNumber]);}
    System.out.println("The User Was Dealt: " + usersCards);
    if(usersCards.contains("Ace")) {
        if(usersCards.contains("King") || usersCards.contains("Queen") || usersCards.contains("Jack") || usersCards.contains("10")){
            System.out.println("You've Got BlackJack! Congratulations, You Win!");
            System.exit(0);} else {System.out.println("You Did Not Get BlackJack!\n[1] Twist\n[2] Stick");}} else {
        System.out.println("You Did Not Get BlackJack! :( \n[1] Twist\n[2] Stick");}
    int x = 0;
    while(x==0) {
        usersDecision = kb.nextInt();
        switch (usersDecision) {
        case 1:
            System.out.println("You've Twisted - Your Cards: " + usersCards);
            System.out.println("You've Twisted - Additional Card Dealt");
            x = 0;
            for (int i = 0; i <= 0; i++) {
                int randomGenNumber = (int) (Math.random()*13);
                usersCards.add(card[randomGenNumber]);}
            System.out.println(usersCards + "\n");
            usersValue = 0;
            for(int i = 0; i < usersCards.size(); i++) {
                if(usersCards.get(i).equals("2")) {
                    usersValue += 2;} else if(usersCards.get(i).equals("3")) {
                    usersValue += 3;} else if(usersCards.get(i).equals("4")) {
                    usersValue += 4;} else if(usersCards.get(i).equals("5")) {
                    usersValue += 5;} else if(usersCards.get(i).equals("6")) {
                    usersValue += 6;} else if(usersCards.get(i).equals("7")) {
                    usersValue += 7;} else if(usersCards.get(i).equals("8")) {
                    usersValue += 8;} else if(usersCards.get(i).equals("9")) {
                    usersValue += 9;} else if(usersCards.get(i).equals("10")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("Jack")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("Queen")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("King")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("Ace")) {
                    usersValue += 11;}}
               System.out.println("Users Cards Value: " + usersValue + "");
            if(usersValue != 21 && usersValue <=21){
                System.out.println("You Did Not Get BlackJack!\n[1] Twist\n[2] Stick");} else if (usersValue == 21) {
                System.out.println("You Got BlackJack! Congratulations!");} else if (usersValue > 21) {
                System.out.println("You've Bust! You Lose!");
                System.exit(0);}
            break;
        case 2:
            System.out.println("You've Stuck - Your Cards: " + usersCards +"\n");
            x = 1;
            usersValue = 0;
            for(int i = 0; i <usersCards.size(); i++) {
                if(usersCards.get(i).equals("2")) {
                    usersValue += 2;} else if(usersCards.get(i).equals("3")) {
                    usersValue += 3;} else if(usersCards.get(i).equals("4")) {
                    usersValue += 4;} else if(usersCards.get(i).equals("5")) {
                    usersValue += 5;} else if(usersCards.get(i).equals("6")) {
                    usersValue += 6;} else if(usersCards.get(i).equals("7")) {
                    usersValue += 7;} else if(usersCards.get(i).equals("8")) {
                    usersValue += 8;} else if(usersCards.get(i).equals("9")) {
                    usersValue += 9;} else if(usersCards.get(i).equals("10")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("Jack")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("Queen")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("King")) {
                    usersValue += 10;} else if(usersCards.get(i).equals("Ace")) {
                    usersValue += 11;}}
            System.out.println("Dealing Dealers Second Card!");
            for (int i = 0; i <= 0; i++) {
                int randomGenNumber = (int) (Math.random()*13);
                dealersCards.add(card[randomGenNumber]);}
            System.out.println(dealersCards + "\n");
            dealersValue = 0;
            for(int i = 0; i < dealersCards.size(); i++) {
                if(dealersCards.get(i).equals("2")) {
                    dealersValue += 2;} else if(dealersCards.get(i).equals("3")) {
                    dealersValue += 3;} else if(dealersCards.get(i).equals("4")) {
                    dealersValue += 4;} else if(dealersCards.get(i).equals("5")) {
                    dealersValue += 5;} else if(dealersCards.get(i).equals("6")) {
                    dealersValue += 6;} else if(dealersCards.get(i).equals("7")) {
                    dealersValue += 7;} else if(dealersCards.get(i).equals("8")) {
                    dealersValue += 8;} else if(dealersCards.get(i).equals("9")) {
                    dealersValue += 9;} else if(dealersCards.get(i).equals("10")) {
                    dealersValue += 10;} else if(dealersCards.get(i).equals("Jack")) {
                    dealersValue += 10;} else if(dealersCards.get(i).equals("Queen")) {
                    dealersValue += 10;} else if(dealersCards.get(i).equals("King")) {
                    dealersValue += 10;} else if(dealersCards.get(i).equals("Ace")) {
                    dealersValue += 11;}}
            int y = 0;
            while(y==0) {
                dealersValue = 0;
                for(int i = 0; i < dealersCards.size(); i++) {
                    if(dealersCards.get(i).equals("2")) {
                        dealersValue += 2;} else if(dealersCards.get(i).equals("3")) {
                        dealersValue += 3;} else if(dealersCards.get(i).equals("4")) {
                        dealersValue += 4;} else if(dealersCards.get(i).equals("5")) {
                        dealersValue += 5;} else if(dealersCards.get(i).equals("6")) {
                        dealersValue += 6;} else if(dealersCards.get(i).equals("7")) {
                        dealersValue += 7;} else if(dealersCards.get(i).equals("8")) {
                        dealersValue += 8;} else if(dealersCards.get(i).equals("9")) {
                        dealersValue += 9;} else if(dealersCards.get(i).equals("10")) {
                        dealersValue += 10;} else if(dealersCards.get(i).equals("Jack")) {
                        dealersValue += 10;} else if(dealersCards.get(i).equals("Queen")) {
                        dealersValue += 10;} else if(dealersCards.get(i).equals("King")) {
                        dealersValue += 10;} else if(dealersCards.get(i).equals("Ace")) {
                        dealersValue += 11;}}
                if(dealersValue <= 16) {
                    int randomGenNumber = (int) (Math.random()*13);
                    dealersCards.add(card[randomGenNumber]);
                    System.out.println("Dealer Has Less Than 17 - Taking Another Card\n");
                    System.out.println("Dealers Cards: " + dealersCards);
                    dealersValue = 0;
                    for(int i = 0; i < dealersCards.size(); i++) {
                        if(dealersCards.get(i).equals("2")) {
                            dealersValue += 2;} else if(dealersCards.get(i).equals("3")) {
                            dealersValue += 3;} else if(dealersCards.get(i).equals("4")) {
                            dealersValue += 4;} else if(dealersCards.get(i).equals("5")) {
                            dealersValue += 5;} else if(dealersCards.get(i).equals("6")) {
                            dealersValue += 6;} else if(dealersCards.get(i).equals("7")) {
                            dealersValue += 7; } else if(dealersCards.get(i).equals("8")) {
                            dealersValue += 8;} else if(dealersCards.get(i).equals("9")) {
                            dealersValue += 9;} else if(dealersCards.get(i).equals("10")) {
                            dealersValue += 10;} else if(dealersCards.get(i).equals("Jack")) {
                            dealersValue += 10;} else if(dealersCards.get(i).equals("Queen")) {
                            dealersValue += 10;} else if(dealersCards.get(i).equals("King")) {
                            dealersValue += 10;} else if(dealersCards.get(i).equals("Ace")) {
                            dealersValue += 11;}}
                    System.out.println("Dealers Cards Value: " + dealersValue + "\n");}
                if(dealersValue == 17 ) {
                    System.out.println("Dealer Has 17 - Dealer Sticks\n");
                    y = 1;
                    if(usersValue < 17) {
                        System.out.println("You Have: " + usersValue + " You Lost");} else if(usersValue == dealersValue) {
                        System.out.println("You Have: " + usersValue + " You Drew");} else {
                        System.out.println("You Have: " + usersValue + " You Won!");}}
                if(dealersValue > 17 && dealersValue < 21) {
                    System.out.println("Dealer Has: " + dealersValue + " Dealer Sticks\n" );
                    y = 1;
                    if(usersValue < 18) {
                        System.out.println("You Have: " + usersValue + " You Lost");} else if(usersValue == dealersValue) {
                        System.out.println("You Have: " + usersValue + " You Drew");} else {
                        System.out.println("You Have: " + usersValue + " You Won!");}}
                if(dealersValue == 21) {
                    System.out.println("Dealer Has BlackJack\n");
                    y = 1;
                    if(usersValue == dealersValue) {
                        System.out.println("You Have: " + usersValue + " You Drew");} }
                if(dealersValue > 21) {
                    System.out.println("Dealer Has Busted - You Win!");
                    y = 1; }}
            break;
        default:
            System.out.println("Not A Valid Selection");}};}
