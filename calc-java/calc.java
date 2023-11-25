import java.util.Scanner;

public class calc {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter the first number: ");
    double num1 = scanner.nextDouble();
    System.out.println("Enter the second number: ");
    double num2 = scanner.nextDouble();
    System.out.println("Enter the operation (+, -, *, /): ");
    String operation = scanner.next();
    double result = 0;
    switch (operation) {
      case "+":
        result = num1 + num2;
        break;
      case "-":
        result = num1 - num2;
        break;
      case "*":
        result = num1 * num2;
        break;
      case "/":
        result = num1 / num2;
        break;
      default:
        System.out.println("Invalid operator");
        break;
    }
    System.out.println("Result: " + result);
    scanner.close();
  }
}
