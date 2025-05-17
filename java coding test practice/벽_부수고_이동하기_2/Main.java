package 벽_부수고_이동하기_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int n, m, k;
    static int[][] arr;
    static int[][][] visited;

    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};

    static int ans = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        k = Integer.parseInt(input[2]);

        arr = new int[n][m];
        visited = new int[n][m][k+1];

        for (int i = 0; i < n; i++) {
            input = br.readLine().split("");
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(0,0,0));
        visited[0][0][0] = 1;

        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            if (cur.x == n-1 && cur.y == m-1) {
                ans = visited[cur.x][cur.y][cur.cnt];
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    if (arr[nx][ny] == 0 && visited[nx][ny][cur.cnt] == 0) {
                        visited[nx][ny][cur.cnt] = visited[cur.x][cur.y][cur.cnt] + 1;
                        queue.offer(new Node(nx,ny,cur.cnt));
                    }
                    else if (arr[nx][ny] == 1 && cur.cnt < k) {
                        if (visited[nx][ny][cur.cnt+1] == 0) {
                            visited[nx][ny][cur.cnt + 1] = visited[cur.x][cur.y][cur.cnt] + 1;
                            queue.offer(new Node(nx,ny,cur.cnt+1));
                        }
                    }
                }
            }
        }

        System.out.println(ans);
    }

    static class Node {
        int x, y, cnt;
        Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
