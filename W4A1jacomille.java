package jacomille;
import java.util.*;
public class W4A1jacomille {


    // Main method
    public static void main(String[] args) {
        Scanner JACOMILLE = new Scanner(System.in);

        int JAC;

        // Display the arithmetic menu
        System.out.println("===== ARITHMETIC MENU =====");
        System.out.println("1. Add Numbers");
        System.out.println("2. Subtract Numbers");
        System.out.println("3. Multiply Numbers");
        System.out.println("4. Divide Numbers");
        System.out.println("5. Exit");

        // Ask the user to choose an operation
        System.out.print("Enter your choice: ");
        JAC = JACOMILLE.nextInt();

        // Call the selected void method
        switch (JAC) {
        
            case 1:
                add(JACOMILLE);
                break;

                
            case 2:
                subtract(JACOMILLE);
                break;

                
            case 3:
                multiply(JACOMILLE);
                break;

                
            case 4:
                divide(JACOMILLE);
                break;

                
            case 5:
                exit();
                break;

                
            default:
                System.out.println("Invalid choice!");
        }

        JACOMILLE.close();
    }

    // Method 1: Addition
    public static void add(Scanner JACOMILLE) {
        System.out.print("Enter first number: ");
        double JAC = JACOMILLE.nextDouble();

        System.out.print("Enter second number: ");
        double number2 = JACOMILLE.nextDouble();

        System.out.println("Sum: " + (JAC + number2));
    }

    // Method 2: Subtraction
    public static void subtract(Scanner JACOMILLE) {
        System.out.print("Enter first number: ");
        double JAC = JACOMILLE.nextDouble();

        System.out.print("Enter second number: ");
        double number2 = JACOMILLE.nextDouble();

        System.out.println("Difference: " + (JAC - number2));
    }

    // Method 3: Multiplication
    public static void multiply(Scanner JACOMILLE) {
        System.out.print("Enter first number: ");
        double JAC = JACOMILLE.nextDouble();

        System.out.print("Enter second number: ");
        double number2 = JACOMILLE.nextDouble();

        System.out.println("Product: " + (JAC * number2));
    }

    // Method 4: Division
    public static void divide(Scanner JACOMILLE) {
        System.out.print("Enter first number: ");
        double JAC = JACOMILLE.nextDouble();

        System.out.print("Enter second number: ");
        double number2 = JACOMILLE.nextDouble();

        // Check if the divisor is zero
        if (number2 != 0) {
            System.out.println("Quotient: " + (JAC / number2));
        } else {
            System.out.println("Cannot divide by zero!");
        }
    }

    // Method 5: Exit
    public static void exit() {
        System.out.println("Thank you !");
    }
}

	



