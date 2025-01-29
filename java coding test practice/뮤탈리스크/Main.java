package 뮤탈리스크;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Queue;

public class Main {
    static int n;
    static int[] arr = new int[3];
    static int[][] attack = {{1,3,9},{1,9,3},{3,1,9},{3,9,1},{9,3,1},{9,1,3}};
    static int[][][] dp = new int[61][61][61];
    static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        dfs(arr, 0);
        System.out.println(min);
    }

    static void dfs(int[] scv, int cnt) {
        int s1 = scv[0];
        int s2 = scv[1];
        int s3 = scv[2];

        if (dp[s1][s2][s3] != 0 && dp[s1][s2][s3] <= cnt) {
            return;
        }

        dp[s1][s2][s3] = cnt;

        if (s1 == 0 && s2 == 0 && s3 == 0) {
            min = Math.min(min, cnt);
            return;
        }

        for (int i=0; i<6; i++) {
            dfs(new int[] {Math.max(s1 - attack[i][0], 0),Math.max(s2 - attack[i][1], 0),Math.max(s3 - attack[i][2], 0)}, cnt+1);
        }
    }
}
