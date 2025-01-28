package 벽_부수고_이동하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int n;
    static int m;
    static int[][] arr;
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            String[] str = br.readLine().split("");
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(str[j]);
            }
        }

        int[][][] visited = new int[n][m][2];
        visited[0][0][0] = 1; // 시작 지점, 벽을 부수지 않은 상태

        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0, 1, false));

        while (!q.isEmpty()) {
            Node node = q.poll();

            // 도착 지점에 도달한 경우 최단 거리 출력
            if (node.x == n - 1 && node.y == m - 1) {
                System.out.println(node.count);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];

                // 맵 범위를 벗어나는 경우
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

                // 이동 가능한 경우
                if (arr[nx][ny] == 0) {
                    if (node.flag == false && visited[nx][ny][0] == 0) {
                        visited[nx][ny][0] = node.count + 1;
                        q.offer(new Node(nx, ny, node.count + 1, false));
                    } else if (node.flag == true && visited[nx][ny][1] == 0) {
                        visited[nx][ny][1] = node.count + 1;
                        q.offer(new Node(nx, ny, node.count + 1, true));
                    }
                }

                // 벽을 만난 경우
                if (arr[nx][ny] == 1 && node.flag == false && visited[nx][ny][1] == 0) {
                    visited[nx][ny][1] = node.count + 1;
                    q.offer(new Node(nx, ny, node.count + 1, true));
                }
            }
        }

        // 도달할 수 없는 경우
        System.out.println(-1);

    }

    static class Node {
        int x;
        int y;
        int count;
        boolean flag;
        Node(int x, int y, int count, boolean flag) {
            this.x = x;
            this.y = y;
            this.count = count;
            this.flag = flag;
        }
    }
}
