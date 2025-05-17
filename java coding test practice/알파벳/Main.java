package 알파벳;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int r, c;
    static char[][] arr;
    static boolean[] alpabet = new boolean[26];
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        r = Integer.parseInt(input[0]);
        c = Integer.parseInt(input[1]);

        arr = new char[r][c];

        for (int i = 0; i < r; i++) {
            String str = br.readLine();
            for (int j = 0; j < c; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        alpabet[arr[0][0] - 'A'] = true;

        dfs(0,0, 1);
        System.out.println(ans);
    }

    public static void dfs(int cx, int cy, int cnt) {

        if (ans < cnt) {
            ans = cnt;
        }

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                if (!alpabet[arr[nx][ny] - 'A']) {
                    alpabet[arr[nx][ny] - 'A'] = true;
                    dfs(nx, ny, cnt + 1);
                    alpabet[arr[nx][ny] - 'A'] = false;
                }
            }
        }
    }
}
