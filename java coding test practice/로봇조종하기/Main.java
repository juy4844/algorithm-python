package 로봇조종하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int n;
    static int m;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        dp = new int[n][m];

        for (int i = 0; i < n; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                dp[i][j] = Integer.parseInt(input[j]);
            }
        }

        for (int i = 1; i < m; i++) {
            dp[0][i] += dp[0][i-1];
        }

        for (int i = 1; i < n; i++) {
            int[] leftToRight = Arrays.copyOf(dp[i], m);
            int[] rightToLeft = Arrays.copyOf(dp[i], m);

            for (int j = 0; j < m; j++) {
                if (j == 0) {
                    leftToRight[j] += dp[i-1][j];
                } else {
                    leftToRight[j] += Math.max(dp[i-1][j], leftToRight[j-1]);
                }
            }

            for (int j = m-1; j >= 0; j--) {
                if (j == m-1) {
                    rightToLeft[j] += dp[i-1][j];
                } else {
                    rightToLeft[j] += Math.max(dp[i-1][j], rightToLeft[j+1]);
                }
            }

            for (int j = 0; j < m; j++) {
                dp[i][j] = Math.max(leftToRight[j], rightToLeft[j]);
            }
        }

        System.out.println(dp[n-1][m-1]);
    }
}
