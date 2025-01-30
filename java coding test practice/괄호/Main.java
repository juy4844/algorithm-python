package 괄호;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int t;
    static int[] arr;
    static long[] dp = new long[5001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        arr = new int[t];

        for (int i = 0; i < t; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        dp[0] = 1;
        dp[2] = 1;

        for (int i = 4; i < 5001; i+=2) {
            for (int j = 2; j <= i; j+=2) {
                dp[i] += (dp[j-2] * dp[i-j]);
                dp[i] %= 1000000007;
            }

        }

        for (int i = 0; i < t; i++) {
            System.out.println(dp[arr[i]]);
        }
    }
}
