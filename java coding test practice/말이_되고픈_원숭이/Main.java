package 말이_되고픈_원숭이;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int k;
    static int w;
    static int h;
    static int[][] arr;
    static int[] hdx = {-2, -2, -1, -1, 1, 1, 2, 2};
    static int[] hdy = {-1, 1, -2, 2, -2, 2, -1, 1};
    static int[] dx = {0, 1, 0 ,-1};
    static int[] dy = {1, 0, -1, 0};
    static boolean[][][] visited;
    static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        k = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        w = Integer.parseInt(input[0]);
        h = Integer.parseInt(input[1]);

        arr = new int[h][w];
        for (int i = 0; i < h; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < w; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        visited = new boolean[h][w][k+1];
        min = bfs(0, 0);

        if(min == Integer.MAX_VALUE) System.out.println("-1");
        else System.out.println(min);
    }

    public static int bfs(int x, int y) {
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(x, y, 0, k));
        visited[x][y][k] = true;

        while (!q.isEmpty()) {
            Node cur = q.poll();

            if (cur.x == h-1 && cur.y == w-1) {
                return cur.count;
            }

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (nx >= 0 && nx < h && ny >= 0 && ny < w) {
                    if (!visited[nx][ny][cur.k] && arr[nx][ny] == 0) {
                        visited[nx][ny][cur.k] = true;
                        q.offer(new Node(nx, ny, cur.count + 1, cur.k));
                    }
                }
            }

            if (cur.k > 0) {
                for (int i = 0; i < 8; i++) {
                    int nx = cur.x + hdx[i];
                    int ny = cur.y + hdy[i];
                    if (nx >= 0 && nx < h && ny >= 0 && ny < w) {
                        if (!visited[nx][ny][cur.k-1] && arr[nx][ny] == 0) {
                            visited[nx][ny][cur.k-1] = true;
                            q.offer(new Node(nx, ny, cur.count + 1, cur.k - 1));
                        }
                    }
                }
            }
        }
        return min;
    }

    public static class Node {
        int x;
        int y;
        int count;
        int k;

        public Node(int x, int y, int count, int k) {
            this.x = x;
            this.y = y;
            this.count = count;
            this.k = k;
        }
    }
}
