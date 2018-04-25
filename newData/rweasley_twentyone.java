import static java.lang.System.out;
import static java.lang.System.in;
import java.util.Random;
import java.util.Scanner;
 
class PlayTwentyOne {
 
    public static void main(String args[]) {
        Random myRandom = new Random();
        Scanner myScanner = new Scanner(in);
        Scanner myScanner2 = new Scanner(in);
 
        int CompCard, CompTotal = 0;
        int PlayerCard=0, totalPlayer = 0;
        int points;                             // value of a card
        int aces;                           // how many aces do you have
        char replyCard, replyPlayAgain = 'y';
        int bet=0 , moneyPlayer = 200;
        wkw whoWins;                        // wkw is a class: public enum wkw {computer, you, nowbody}
         
        String nameCard = " ";
         
        out.println("you have " + moneyPlayer + " euro");
         
        while (replyPlayAgain == 'y' && moneyPlayer >= 0){       // Draw 2 cards for player.
            aces = 0;
            totalPlayer = 0;
            CompTotal = 0;
            bet = 0;
            replyCard = 'y';
            whoWins = wkw.nowbody;
             
                while (bet == 0){ 
                     
                    out.println("How much do you want to bet?");
                    bet = myScanner.nextInt();
                    }
                         
                for (int count = 0; count < 2; count++){
                     
                    PlayerCard = myRandom.nextInt(13) + 1;
                 
                    switch (PlayerCard) {
                    case 1:
                        nameCard = "ace";
                        aces = +1;
                        points = 11;
                        break;
                    case 2:
                        nameCard = "two";
                        points = 2;
                        break;
                    case 3:
                        nameCard = "tree";
                        points = 3;
                        break;
                    case 4:
                        nameCard = "for";
                        points = 4;
                        break;
                    case 5:
                        nameCard = "five";
                        points = 5;
                        break;
                    case 6:
                        nameCard = "six";
                        points = 6;
                        break;
                    case 7:
                        nameCard = "seven";
                        points = 7;
                        break;
                    case 8:
                        nameCard = "eight";
                        points = 8;
                        break;
                    case 9:
                        nameCard = "nine";
                        points = 9;
                        break;
                    case 10:
                        nameCard = "ten";
                        points = 10;
                        break;
                    case 11:
                        points = 10;
                        nameCard = "Jack";
                        break;
                    case 12:
                        points = 10;
                        nameCard = "queen";
                        break;
                    case 13:
                        points = 10;    
                        nameCard = "king";
                        break;
                    default:
                        points = 1000;
                        break;
                    }
                 
                    totalPlayer += points;
                    while (totalPlayer> 21 && aces >=1){
                        totalPlayer = totalPlayer -10;
                        aces = aces -1;
                    }
                   System.out.println("Kaart getrokken: " + nameCard + ". Total points: " + totalPlayer);
               }
                if (totalPlayer == 21){
                    System.out.println(":) You have 21");
                    replyCard = 'n';
                    whoWins = wkw.you;
                }
                
                while (replyCard == 'y' & whoWins == wkw.nowbody){      //Draw cards for player
                 
                    System.out.println("Do you want a card? y/n");
                    replyCard = myScanner2.findWithinHorizon(".",0).charAt(0);
                     
                    if (replyCard == 'y'){
                     
                        PlayerCard = myRandom.nextInt(13) + 1;
                         
                        switch (PlayerCard) {
                        case 1:
                            nameCard = "ace";
                            aces = +1;
                            points = 11;
                            break;
                        case 2:
                            nameCard = "two";
                            points = 2;
                            break;
                        case 3:
                            nameCard = "tree";
                            points = 3;
                            break;
                        case 4:
                            nameCard = "for";
                            points = 4;
                            break;
                        case 5:
                            nameCard = "five";
                            points = 5;
                            break;
                        case 6:
                            nameCard = "six";
                            points = 6;
                            break;
                        case 7:
                            nameCard = "seven";
                            points = 7;
                            break;
                        case 8:
                            nameCard = "eight";
                            points = 8;
                            break;
                        case 9:
                            nameCard = "nine";
                            points = 9;
                            break;
                        case 10:
                            nameCard = "ten";
                            points = 10;
                            break;
                        case 11:
                            points = 10;
                            nameCard = "Jack";
                            break;
                        case 12:
                            points = 10;
                            nameCard = "queen";
                            break;
                        case 13:
                            points = 10;    
                            nameCard = "king";
                            break;
                        default:
                            points = 1000;
                            break;
                        }
                         
                        totalPlayer += points;
                        while (totalPlayer> 21 && aces >=1){
                            totalPlayer = totalPlayer -10;
                            aces = aces -1;
                        }
                        System.out.println("Draw card " + nameCard + ". Total points: " + totalPlayer);
                        
                        if (totalPlayer == 21){
                            System.out.println(":) Je hebt 21");
                            replyCard = 'n';
                            whoWins = wkw.you;
                             
                        } else if (totalPlayer > 21){
                            replyCard = 'n';
                            whoWins = wkw.computer;
                             
                        } else { 
                            replyCard = 'y';
                            whoWins = wkw.nowbody;
                        }   
                    }
                }
                System.out.println("total Player 1: "+ totalPlayer + " ppoints");
                
                //Computers turn:
                aces = 0;
                 
                if (whoWins == wkw.nowbody){
                    out.println();
                    out.println("Computer:");
                }
                 
                while ((whoWins == wkw.nowbody) && (CompTotal <= totalPlayer)) { //Draw cards for computer till he wins or >21
                    CompCard = myRandom.nextInt(13) + 1;
                     
                    switch (CompCard) {
                    case 1:
                        nameCard = "ace";
                        aces = +1;
                        points = 11;
                        break;
                    case 2:
                        nameCard = "two";
                        points = 2;
                        break;
                    case 3:
                        nameCard = "tree";
                        points = 3;
                        break;
                    case 4:
                        nameCard = "for";
                        points = 4;
                        break;
                    case 5:
                        nameCard = "five";
                        points = 5;
                        break;
                    case 6:
                        nameCard = "six";
                        points = 6;
                        break;
                    case 7:
                        nameCard = "seven";
                        points = 7;
                        break;
                    case 8:
                        nameCard = "eight";
                        points = 8;
                        break;
                    case 9:
                        nameCard = "nine";
                        points = 9;
                        break;
                    case 10:
                        nameCard = "ten";
                        points = 10;
                        break;
                    case 11:
                        points = 10;
                        nameCard = "Jack";
                        break;
                    case 12:
                        points = 10;
                        nameCard = "queen";
                        break;
                    case 13:
                        points = 10;    
                        nameCard = "king";
                        break;
                    default:
                        points = 1000;
                        break;
                    }
                    while (CompTotal> 21 && aces >=1){
                        CompTotal = CompTotal -10;
                        aces = aces -1;
                    }
                    CompTotal += points;
                    System.out.println("Draw Card: " + nameCard + ". Total points: " + CompTotal);
                }
                 
                if (whoWins == wkw.nowbody){                
                System.out.print("total Computer:" );
                System.out.print(CompTotal);
                out.println();
                }
                 
                if (CompTotal >= totalPlayer){
                    whoWins = wkw.computer;
                }
                if (CompTotal >= 22){
                    whoWins = wkw.you;
                }
                if (whoWins == wkw.you){
                    out.println();
                    System.out.println("Yee, you win!");
                    moneyPlayer = moneyPlayer + bet;
                } else if (whoWins == wkw.computer){
                    out.println();
                    System.out.println("Computer wins");
                    moneyPlayer = moneyPlayer - bet;
                } else {
                    out.println();
                    System.out.println("there is something wrong with my code.");
                }
             
            out.println();
            out.println("You have " + moneyPlayer + " euro");
            out.println ("Do you want to play again? y/n");
            replyPlayAgain = myScanner2.findWithinHorizon(".",0).charAt(0);
                         
        }
     } 
}