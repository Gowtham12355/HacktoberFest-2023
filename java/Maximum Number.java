import java.util.Scanner;

public class MaxNumberInArray {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        
        int[] numbers = new int[n];

        System.out.println("Enter " + n + " numbers:");
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }

        int maxNumber = findMax(numbers);
        System.out.println("The maximum number in the array is: " + maxNumber);

        scanner.close();
    }

    public static int findMax(int[] array) {
        int max = array[0];  // Assume the first element is the maximum
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];  // Update max if current element is greater
            }
        }
        return max;
    }
}
