import java.util.*;
/* https://www.daniweb.com/programming/software-development/threads/426381/blackjack-code-review-beginner */
public class BlackJack {
public static void main(String[] args) {

    Scanner jd = new Scanner(System.in);
    int personChoice = 0;
    int personAmount = 0;
    int personTotal = 0;
    String[] paper = { "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"};
    ArrayList<String> personsPaper = new ArrayList<String>();
    ArrayList<String> Comp_paper = new ArrayList<String>();
    for (int i = 0; i <= 0; i++) {
        int randomGenNumber = (int) (Math.random()*13);
        Comp_paper.add(paper[randomGenNumber]);}
    System.out.println("The Dealer Was Dealt: " + Comp_paper);
    for (int i = 0; i <= 1; i++) {
        int randomGenNumber = (int) (Math.random()*13);
        personsPaper.add(paper[randomGenNumber]);}
    System.out.println("The User Was Dealt: " + personsPaper);
    if(personsPaper.contains("Ace")) {
        if(personsPaper.contains("King") || personsPaper.contains("Queen") || personsPaper.contains("Jack") || personsPaper.contains("10")){
            System.out.println("You've Got BlackJack! Congratulations, You Win!");
            System.exit(0);} else {System.out.println("You Did Not Get BlackJack!\n[1] Twist\n[2] Stick");}} else {
        System.out.println("You Did Not Get BlackJack! :( \n[1] Twist\n[2] Stick");}
    int x = 0;
    while(x==0) {
        personChoice = jd.nextInt();
        switch (personChoice) {
        case 1:
            System.out.println("You've Twisted - Your Cards: " + personsPaper);
            System.out.println("You've Twisted - Additional Card Dealt");
            x = 0;
            for (int i = 0; i <= 0; i++) {
                int randomGenNumber = (int) (Math.random()*13);
                personsPaper.add(paper[randomGenNumber]);}
            System.out.println(personsPaper + "\n");
            personAmount = 0;
            for(int i = 0; i < personsPaper.size(); i++) {
                if(personsPaper.get(i).equals("2")) {
                    personAmount += 2;} else if(personsPaper.get(i).equals("3")) {
                    personAmount += 3;} else if(personsPaper.get(i).equals("4")) {

                    }
                    personAmount += 4;} else if(personsPaper.get(i).equals("5")) {
                    personAmount += 5;} else if(personsPaper.get(i).equals("6")) {

                    }
                    personAmount += 6;} else if(personsPaper.get(i).equals("7")) {
                    personAmount += 7;} else if(personsPaper.get(i).equals("8")) {
                    personAmount += 8;} else if(personsPaper.get(i).equals("9")) {

                    }
                    personAmount += 9;} else if(personsPaper.get(i).equals("10")) {
                    personAmount += 10;} else if(personsPaper.get(i).equals("Jack")) {

                    }
                    personAmount += 10;} else if(personsPaper.get(i).equals("Queen")) {
                    personAmount += 10;} else if(personsPaper.get(i).equals("King")) {

                    }
                    personAmount += 10;} else if(personsPaper.get(i).equals("Ace")) {
                    personAmount += 11;}}
               System.out.println("Users Cards Value: " + personAmount + "");
            if(personAmount != 21 && personAmount <=21){
                System.out.println("You Did Not Get BlackJack!\n[1] Twist\n[2] Stick");} else if (personAmount == 21) {
                System.out.println("You Got BlackJack! Congratulations!");} else if (personAmount > 21) {
                System.out.println("You've Bust! You Lose!");
                System.exit(0);}
            break;
        case 2:
            System.out.println("You've Stuck - Your Cards: " + personsPaper +"\n");
            x = 1;
            personAmount = 0;
            for(int i = 0; i <personsPaper.size(); i++) {
                if(personsPaper.get(i).equals("2")) {
                    personAmount += 2;} else if(personsPaper.get(i).equals("3")) {
                    personAmount += 3;} else if(personsPaper.get(i).equals("4")) {
                    personAmount += 4;} else if(personsPaper.get(i).equals("5")) {

                    }
                    personAmount += 5;} else if(personsPaper.get(i).equals("6")) {

                    }
                    personAmount += 6;} else if(personsPaper.get(i).equals("7")) {
                    personAmount += 7;} else if(personsPaper.get(i).equals("8")) {
                    personAmount += 8;} else if(personsPaper.get(i).equals("9")) {
                    personAmount += 9;} else if(personsPaper.get(i).equals("10")) {
                    personAmount += 10;} else if(personsPaper.get(i).equals("Jack")) {
                    personAmount += 10;} else if(personsPaper.get(i).equals("Queen")) {

                    }
                    personAmount += 10;} else if(personsPaper.get(i).equals("King")) {
                    personAmount += 10;} else if(personsPaper.get(i).equals("Ace")) {
                    personAmount += 11;}}

            while(y==0) {
                personTotal = 0;
                for(int i = 0; i < Comp_paper.size(); i++) {
                    if(Comp_paper.get(i).equals("2")) {
                        personTotal += 2;} else if(Comp_paper.get(i).equals("3")) {
                        personTotal += 3;} else if(Comp_paper.get(i).equals("4")) {
                        personTotal += 4;} else if(Comp_paper.get(i).equals("5")) {
                        personTotal += 5;} else if(Comp_paper.get(i).equals("6")) {
                        personTotal += 6;} else if(Comp_paper.get(i).equals("7")) {
                        personTotal += 7;} else if(Comp_paper.get(i).equals("8")) {
                        personTotal += 8;} else if(Comp_paper.get(i).equals("9")) {
                        personTotal += 9;} else if(Comp_paper.get(i).equals("10")) {
                        personTotal += 10;} else if(Comp_paper.get(i).equals("Jack")) {
                        personTotal += 10;} else if(Comp_paper.get(i).equals("Queen")) {
                        personTotal += 10;} else if(Comp_paper.get(i).equals("King")) {
                        personTotal += 10;} else if(Comp_paper.get(i).equals("Ace")) {
                        personTotal += 11;}}
                if(personTotal <= 16) {
                    int randomGenNumber = (int) (Math.random()*13);
                    Comp_paper.add(paper[randomGenNumber]);
                    System.out.println("Dealer Has Less Than 17 - Taking Another Card\n");
                    System.out.println("Dealers Cards: " + Comp_paper);
                    personTotal = 0;
                    for(int i = 0; i < Comp_paper.size(); i++) {
                        if(Comp_paper.get(i).equals("2")) {
                            personTotal += 2;} else if(Comp_paper.get(i).equals("3")) {
                            personTotal += 3;} else if(Comp_paper.get(i).equals("4")) {
                            personTotal += 4;} else if(Comp_paper.get(i).equals("5")) {
                            personTotal += 5;} else if(Comp_paper.get(i).equals("6")) {
                            personTotal += 6;} else if(Comp_paper.get(i).equals("7"))
                            {
                            personTotal += 7; } else if(Comp_paper.get(i).equals("8")) {
                            personTotal += 8;} else if(Comp_paper.get(i).equals("9")) {
                            personTotal += 9;} else if(Comp_paper.get(i).equals("10")) {
                            personTotal += 10;} else if(Comp_paper.get(i).equals("Jack")) {
                            personTotal += 10;} else if(Comp_paper.get(i).equals("Queen")) {
                            personTotal += 10;} else if(Comp_paper.get(i).equals("King")) {
                            personTotal += 10;} else if(Comp_paper.get(i).equals("Ace")) {
                            personTotal += 11;}}
                    System.out.println("Dealers Cards Value: " + personTotal + "\n");}
                if(personTotal == 17 ) {
                    System.out.println("Dealer Has 17 - Dealer Sticks\n");
                    y = 1;
                    if(personAmount < 17) {
                        System.out.println("You Have: " + personAmount + " You Lost");}
                         else if(personAmount == personTotal) {
                        System.out.println("You Have: " + personAmount + " You Drew");
                        } else {
                        System.out.println("You Have: " + personAmount + " You Won!");}}
                if(personTotal > 17 && personTotal < 21) {
                    System.out.println("Dealer Has: " + personTotal + " Dealer Sticks\n" );
                    y = 1;
                    if(personAmount < 18) {
                        System.out.println("You Have: " + personAmount + " You Lost");
                        } else if(personAmount == personTotal) {
                        System.out.println("You Have: " + personAmount + " You Drew");} else {

                        }
                        System.out.println("You Have: " + personAmount + " You Won!");}}
                if(personTotal == 21) {
                    System.out.println("Dealer Has BlackJack\n");
                    y = 1;
                    if(personAmount == personTotal) {
                        System.out.println("You Have: " + personAmount + " You Drew");} }
                if(personTotal > 21) {
                    System.out.println("Dealer Has Busted - You Win!");
                    y = 1; }}
            break;
        default:
            System.out.println("Not A Valid Selection");}};}
