import 'dart:io';

void main() {
  stdout.write('Enter first number: ');
  int num1 = int.parse(stdin.readLineSync()!);

  stdout.write('Enter second number: ');
  int num2 = int.parse(stdin.readLineSync()!);

  stdout.write('Enter operator (+, -, *, /): ');
  String operator = stdin.readLineSync()!;

  int result;
  switch (operator) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      result = num1 ~/ num2;
      break;
    default:
      stdout.write('Invalid operator');
      return;
  }

  stdout.write('Result: $result');
}
