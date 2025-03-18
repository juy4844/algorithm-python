package 계단오르기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int n;
    static int[] arr;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(reader.readLine());


        arr = new int[n];
        dp = new int[n][2];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(reader.readLine());
        }

        if (n == 1) {
            System.out.println(arr[0]);
            return;
        }

        dp[0][0] = arr[0];
        dp[0][1] = arr[0];
        dp[1][0] = arr[1];
        dp[1][1] = arr[1]+arr[0];

        for (int i = 2; i < n; i++) {
            dp[i][0] = Math.max(dp[i-2][0], dp[i-2][1]);
            dp[i][0] += arr[i];
            dp[i][1] = dp[i-1][0] + arr[i];
        }

        System.out.println(Math.max(dp[n-1][0], dp[n-1][1]));
    }
}
