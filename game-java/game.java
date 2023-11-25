import java.util.Scanner;

public class game {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Welcome to the guessing game!");
    System.out.println("Guess a number between 1 and 100: ");
    int target = (int) (Math.random() * 100) + 1;
    int guess = 0;
    while (guess != target) {
      guess = scanner.nextInt();
      if (guess < target) {
        System.out.println("Too low, guess again: ");
      } else if (guess > target) {
        System.out.println("Too high, guess again: ");
      }
    }
    System.out.println("You win!");
    scanner.close();
  }
}
