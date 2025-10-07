package 캐슬디펜스;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int n,m,d;
    static int[][] arr;

    static int[] location = new int[3];

    static int[] dx = {-1, 0, 0};
    static int[] dy = {0, -1, 1};
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        d = Integer.parseInt(input[2]);

        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        dfs(0,0);
        System.out.println(ans);
    }

    static void dfs(int index, int start) {
        if (index == 3) {
            int[][] temp = new int[n][m];
            for (int i = 0; i < n; i++) {
                temp[i] = arr[i].clone();
            }

            int anstemp = 0;
            for (int k = 0; k < n; k++) {
                int[][] remove = new int[3][2];
                for (int j = 0; j < 3; j++) {
                    Arrays.fill(remove[j], -1);
                }
                for (int i = 0; i < 3; i++) {
                    boolean[][] visited = new boolean[n][m];
                    Queue<Node> queue = new LinkedList<>();
                    queue.offer(new Node(n, location[i], 0));
                    boolean flag = false;

                    while (!queue.isEmpty()) {
                        Node node = queue.poll();

                        for (int j = 0; j < 3; j++) {
                            int nx = node.x + dx[j];
                            int ny = node.y + dy[j];

                            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                                if (!visited[nx][ny] && node.cnt < d) {
                                    if (temp[nx][ny] == 1) {
                                        anstemp += 1;
                                        remove[i][0] = nx;
                                        remove[i][1] = ny;
                                        flag = true;
                                        break;
                                    } else {
                                        visited[nx][ny] = true;
                                        queue.offer(new Node(nx, ny, node.cnt + 1));
                                    }
                                }
                            }
                        }
                        if (flag) {
                            break;
                        }
                    }
                }

                for (int i = 0; i < 3; i++) {
                    temp[remove[i][0]][remove[i][1]] = 0;
                }

                if (remove[0][0] == remove[1][0] && remove[0][1] == remove[1][1] && remove[0][0] == remove[2][0] && remove[0][1] == remove[2][1]) {
                    anstemp -= 2;
                } else if (remove[0][0] == remove[1][0] && remove[0][1] == remove[1][1]) {
                    anstemp -= 1;
                } else if (remove[0][0] == remove[2][0] && remove[0][1] == remove[2][1]) {
                    anstemp -= 1;
                } else if (remove[1][0] == remove[2][0] && remove[1][1] == remove[2][1]) {
                    anstemp -= 1;
                }

                for (int i = n-1; i >= 1; i--) {
                    temp[i] = temp[i-1].clone();
                }
            }

            if (ans < anstemp) {
                ans = anstemp;
            }

            return;
        }

        for (int i = start; i < m; i++) {
            location[index] = i;
            dfs(index + 1, i+1);
        }
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
