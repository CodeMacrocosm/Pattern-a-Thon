import java.util.Scanner;

public class Hourglass {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of rows: ");
        int rows = scanner.nextInt();

        // Print top half of the hourglass
        for (int i = 1; i <= rows; i++) {
            // Print spaces
            for (int j = 1; j < i; j++) {
                System.out.print(" ");
            }

            // Print stars
            for (int k = i; k <= rows; k++) {
                System.out.print("* ");
            }

            // Move to the next line
            System.out.println();
        }

        // Print bottom half of the hourglass
        for (int i = rows - 1; i >= 1; i--) {
            // Print spaces
            for (int j = 1; j < i; j++) {
                System.out.print(" ");
            }

            // Print stars
            for (int k = i; k <= rows; k++) {
                System.out.print("* ");
            }

            // Move to the next line
            System.out.println();
        }

        scanner.close();
    }
}

