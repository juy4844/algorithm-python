package 내리막길;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int m,n;
    static int[][] arr;
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};

    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        m = Integer.parseInt(input[0]);
        n = Integer.parseInt(input[1]);
        arr = new int[m][n];
        dp = new int[m][n];

        for (int i = 0; i<m; i++) {
            for (int j = 0; j<n; j++) {
                dp[i][j] = -1;
            }
        }

        for (int i = 0; i < m; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        System.out.println(dfs(0,0));
    }

    public static int dfs(int cx, int cy) {
        if (cx == m - 1 && cy == n - 1) {
            return 1;
        }

        if (dp[cx][cy] != -1) {
            return dp[cx][cy];
        }

        int ways = 0;
        for (int i = 0; i<4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx >= 0 && nx < m && ny >= 0 && ny < n && arr[nx][ny] < arr[cx][cy]) {
                ways += dfs(nx, ny);
            }
        }
        dp[cx][cy] = ways;

        return dp[cx][cy];
    }
}
