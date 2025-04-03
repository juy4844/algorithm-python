package 젤다;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    static int[] dx = {1, -1, 0,0};
    static int[] dy = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = 0;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            t++;
            if (n == 0) {
                break;
            }
            int[][] arr = new int[n][n];

            for (int i = 0; i < n; i++) {
                String[] s = br.readLine().split(" ");
                for (int j = 0; j < n; j++) {
                    arr[i][j] = Integer.parseInt(s[j]);
                }
            }

            int[][] dist = new int[n][n];
            for (int i = 0; i < n; i++) {
                Arrays.fill(dist[i], Integer.MAX_VALUE);
            }
            dist[0][0] = arr[0][0];
            PriorityQueue<Node> pq = new PriorityQueue();
            pq.offer(new Node(0,0,arr[0][0]));

            while (!pq.isEmpty()) {
                Node cur = pq.poll();

                if (cur.cost > dist[cur.x][cur.y]) {
                    continue;
                }

                for (int i = 0; i < 4; i++) {
                    int nx = cur.x + dx[i];
                    int ny = cur.y + dy[i];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                        if (dist[nx][ny] > cur.cost + arr[nx][ny]) {
                            dist[nx][ny] = cur.cost + arr[nx][ny];
                            pq.offer(new Node(nx, ny, dist[nx][ny]));
                        }
                    }
                }
            }

            System.out.println("Problem " + t + ": " + dist[n-1][n-1]);
        }


    }

    static class Node implements Comparable<Node> {
        int x;
        int y;
        int cost;
        public Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }

        public int compareTo(Node o) {
            return cost - o.cost;
        }
    }
}
