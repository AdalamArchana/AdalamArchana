// Bubble short
import java.util.Scanner;
class BubbleSort
{
    public static void bubblesort(int arr[]) {
        int n = arr.length;
        for(int i=0; i<n-1; i++) {
            for(int j=0;j<n-1-i;j++) {
                if(arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    public static void printArray(int[] arr) {
        for(int val : arr)
            System.out.print(val+" ");
        System.out.println();
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
        printArray(arr);
        bubblesort(arr);
        printArray(arr);
        sc.close();
    }
}