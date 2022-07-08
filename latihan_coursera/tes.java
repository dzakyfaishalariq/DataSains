
// impoert scenner
import java.util.Scanner;

public class tes {

    public static void main(String[] args) {
        // cetak array
        int[] array = { 7, 20, 13, 9, 3, 19, 12, 80 };
        Scanner input = new Scanner(System.in);
        System.out.println("Masukkan nilai a: ");
        int a = input.nextInt();
        // lakukan sorting
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] > array[j]) {
                    int temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }
        // cetak array
        System.out.println("Array setelah sorting: ");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        // index a berada di
        int indexA = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == a) {
                indexA = i;
            }
        }
        System.out.println("\nIndex a berada di " + indexA);
    }
}