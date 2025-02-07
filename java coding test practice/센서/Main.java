package 센서;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        String[] input = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }
        Arrays.sort(arr);

        Integer[] diffArr = new Integer[n-1];
        for (int i = 0; i < n-1; i++) {
            diffArr[i] = arr[i+1] - arr[i];
        }

        Arrays.sort(diffArr, Collections.reverseOrder());

        int sum = 0;

        for(int i = k-1; i < n-1; i++) {
            sum += diffArr[i];
        }
        System.out.println(sum);
    }
}
