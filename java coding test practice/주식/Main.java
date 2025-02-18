package 주식;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int t;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            long[] arr = new long[n];
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[j] = Integer.parseInt(input[j]);
            }
            long max = arr[n-1];
            long ans = 0;
            for (int j = n-2; j >= 0; j--) {
                if (arr[j] <= max) {
                    ans += max - arr[j];
                }
                else {
                    max = arr[j];
                }
            }
            System.out.println(ans);
        }
    }
}
