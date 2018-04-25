import java.util.*;
public class twentyone
{
public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);
    String player;
    int matchstick;
    int total = 0;

    System.out.println("Rules of the game: \nThe player and computer take turns picking 1, 2, 3 , or 4 matchsticks."
                        + " \nThe player to pick the last stick out of 21 loses.");
    System.out.print("\nHello player. Please enter your name: ");
    player = keyboard.next();

     while (total < 21) {

        System.out.print("\nHow many matchsticks do you pick, " + player + "? ");
        matchstick = keyboard.nextInt();

        while (matchstick > 4) {
            System.out.print("You have exceeded the limit of 4 matchsticks. Please try again. \n\nHow many matchsticks do you pick? ");
            matchstick = keyboard.nextInt();
        }

        total += matchstick;

        System.out.println(player + " has picked " + matchstick + " matchstick(s) and brings the total to " + total + " matchsticks.");

        if (total == 21) {
            System.out.println("You picked the last matchstick... YOU LOSE!!!");
        }

        System.out.println("\nNow it's the computer's turn.");

        if (matchstick == 1) {
            total += 4;
            System.out.println("The computer chooses 4 matchsticks, bringing the total to " + total + " matchsticks.");
        }
        if (matchstick == 2) {
            total += 3;
            System.out.println("The computer chooses 3 matchsticks, bringing the total to " + total + " matchsticks.");
        }
        if (matchstick == 3) {
            total += 2;
            System.out.println("The computer chooses 2 matchsticks, bringing the total to " + total + " matchsticks.");
        }
        if (matchstick == 4) {
            total += 1;
            System.out.println("The computer chooses 1 matchstick, bringing the total to " + total + " matchsticks.");
        }

    }
}
}