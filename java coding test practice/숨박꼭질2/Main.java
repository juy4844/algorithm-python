package 숨박꼭질2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int n, k;
    static int[] dist = new int[200001];
    static int answer = 0;
    static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        n = Integer.parseInt(input[0]);
        k = Integer.parseInt(input[1]);

        Queue<Integer> queue = new LinkedList<>();

        queue.offer(n);

        boolean flag = true;

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (dist[now] > min) {
                break;
            }

            if (now == k) {
                if (flag) {
                    min = dist[now];
                    flag = false;
                }
                answer += 1;
            }

            if (now - 1 >= 0 && (dist[now - 1] == dist[now] + 1 || dist[now - 1] == 0)) {
                dist[now - 1] = dist[now] + 1;
                queue.offer(now-1);
            }
            if (now + 1 <= 200000 && (dist[now + 1] == dist[now] + 1 || dist[now + 1] == 0)) {
                dist[now + 1] = dist[now] + 1;
                queue.offer(now+1);
            }
            if (now * 2 <= 200000 && (dist[now * 2] == dist[now] + 1 || dist[now * 2] == 0)) {
                dist[now * 2] = dist[now] + 1;
                queue.offer(now*2);
            }
        }

        System.out.println(min);
        System.out.println(answer);
    }
}
