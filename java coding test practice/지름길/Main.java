package 지름길;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int n;
    static int d;
    static int[][] arr;
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        d = Integer.parseInt(input[1]);
        ans = d;
        arr = new int[n][3];

        for (int i = 0; i < n; i++) {
            input = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(input[0]);
            arr[i][1] = Integer.parseInt(input[1]);
            arr[i][2] = Integer.parseInt(input[2]);
        }

        int[] dp = new int[d+1];
        dp[0] = 0;

        for (int i = 1; i < d+1; i++) {
            dp[i] = dp[i-1] +1;
            for (int j = 0; j < n; j++) {
                if (i == arr[j][1]) {
                    dp[i] = Math.min(dp[i], dp[arr[j][0]] + arr[j][2]);
                }
            }

        }

        System.out.println(dp[d]);
    }

}
