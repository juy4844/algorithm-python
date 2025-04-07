package 텀프로젝트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int ans = 0;
            int[] graph = new int[n+1];
            String[] str = br.readLine().split(" ");
            for (int i = 0; i < n; i++) {
                graph[i+1] = Integer.parseInt(str[i]);
            }

            for (int i = 1; i <= n; i++) {
                boolean[] visited = new boolean[n+1];
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);
                while (!queue.isEmpty()) {
                    int cur = queue.poll();
                    if (!visited[graph[cur]]) {
                        if (graph[cur] == i) {
                            ans += 1;
                        }
                        visited[graph[cur]] = true;
                        queue.offer(graph[cur]);
                    }
                }
            }

            System.out.println(n - ans);
        }
    }
}
