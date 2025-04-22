package 수정렬하기2;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            arr[i] = Integer.parseInt(s);
        }

        quickSort(arr, 0, n-1);

        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

    }

    static void quickSort(int[] arr, int left, int right) {

        if (left >= right) {
            return;
        }

        int lo = left;
        int hi = right;
        int pivot = arr[left];

        while (lo <= hi) {
            while (arr[hi] > pivot) {
                hi--;
            }

            while (arr[lo] < pivot) {
                lo++;
            }

            if (lo <= hi) {
                int temp = arr[lo];
                arr[lo] = arr[hi];
                arr[hi] = temp;
                lo ++;
                hi --;
            }

        }

        int t = arr[left];
        arr[left] = arr[lo];
        arr[lo] = t;


        quickSort(arr, left, hi-1);
        quickSort(arr, hi + 1, right);
    }
}
