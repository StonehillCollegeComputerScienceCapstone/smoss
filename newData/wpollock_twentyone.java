/* from: http://www.cs.cornell.edu/courses/cs100m/2005sp/Projects/P6/TwentyOne.java */
public class TwentyOne {
  public static final int HIT = 1;
  public static final int STAY = 2;
  public static final int QUIT = 3;

  private static final int NUM_PLAYERS = 3;

  /* Prepare the Dealer's Deck, set Players' play status, clear the
   * all hands, deal two cards to each Person, and display the hands.
   */
  private static void dealNewRound(Dealer d, Player players[]) {

  }

 /* Perform actions after player chooses to hit
   * =Returns true if the player has busted,
   * otherwise returns false
   *
   * DO NOT CHANGE THIS CODE.
   */
  private static boolean doHit(Dealer d, Player p) {
    if(p.getHand().isFull()) {
      System.out.println("Cannot hit! Hand is full");
      return false;
    }

    d.deal(p.getHand());
    System.out.println(p.getName() +"'s hand: "+ p.getHand());

    if(p.getHand().getValue() > 21) {
      System.out.println(p.getName() + " busted.");
      return true;
    }
    else{
      return false;
    }
  }

  /* Perform actions after player chooses to stay
   *
   * DO NOT CHANGE THIS CODE.
   */
  private static void doStay(Dealer d, Player players[]) {
    d.finishHand();
    int dealerPoints = d.getHand().getValue();

    System.out.println("----------------------------------------------");
    System.out.println("Dealer's hand: "+ d.getHand());

    if(dealerPoints > 21) {
        System.out.println("Dealer Busted.");
    }

    for(int i=0; i<NUM_PLAYERS; i++){
      if(players[i] != null) {
        int playerPoints = players[i].getHand().getValue();

        System.out.println(players[i].getName() +"'s hand: "+ players[i].getHand());

        if(playerPoints > 21){ // Player busted
          System.out.println(players[i].getName()+" lost.");
          players[i].loseHand();
        }
        else if(dealerPoints > 21 || dealerPoints < playerPoints){
          System.out.println(players[i].getName() + " won.");
          players[i].winHand();
        }
        else if(dealerPoints > playerPoints)
        {
          System.out.println(players[i].getName()+" lost.");
          players[i].loseHand();
        }
        else{
          System.out.println(players[i].getName()+" got a draw.");
        }
      }
    }
    System.out.println("----------------------------------------------");
  }

  /* the main entrance to the program
   *
   * DO NOT CHANGE THIS CODE
   */
  public static void main(String[] args) {
    System.out.println("Welcome to TwentyOne.");
    int numPlaying = NUM_PLAYERS;
    Player players[] = new Player[NUM_PLAYERS];

    Dealer d = new Dealer();
    boolean playing = true;

    for(int i=0; i < NUM_PLAYERS; i++){
      System.out.println("What is player #"+(i+1)+"'s name? ");
      String name = Keyboard.readString();
      players[i] = new Player(name);
    }
    System.out.print("\n");
    dealNewRound(d, players);

    int command;
    String cmd;
    while(playing) {
      for(int i=0;i<NUM_PLAYERS;i++){
        while(players[i]!=null && players[i].isPlaying()){
          System.out.println("\n"+players[i].getName() + "'s hand: " + players[i].getHand());
          System.out.println("What would " + players[i].getName() + " like to do? ");
          System.out.println("(1:HIT  2.STAY  3.QUIT) ");
          command = Keyboard.readInt();

          if(command == HIT) {
            if(doHit(d,players[i]) == true){
              players[i].stopPlaying();
            }
          }
          else if(command == STAY){
            players[i].stopPlaying();
          }
          else if(command == QUIT) {
            numPlaying--;
            System.out.println(players[i].getName() + " quit.");
            System.out.println(players[i]);
            players[i]= null;  //Player i no longer in this multiplayer game
          }
          else {
            System.out.println("INVALID COMMAND");
          }
        }//end while
      }//end for

      if(numPlaying == 0) {
        System.out.println("Everyone has quit the game. GoodBye");
        playing = false;
      }
      else {
        doStay(d, players);
        System.out.println("Start another round? ");
        cmd = Keyboard.readString().toLowerCase();
        if(!cmd.equals("y") && !cmd.equals("yes")) {
          playing = false;
          for(int i=0; i < NUM_PLAYERS; i++){
            if(players[i] != null)
              System.out.println(players[i]);
          }
          System.out.println("Goodbye");
        }
        else {
          dealNewRound(d, players);
        }
      }//end if
    }//end while
  }
}