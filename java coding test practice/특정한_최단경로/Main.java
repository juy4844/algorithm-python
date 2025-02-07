package 특정한_최단경로;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

public class Main {
    static int n;
    static int e;
    static int INF = 200000000;
    static HashMap<Integer, ArrayList<Node>> graph = new HashMap<>();
    static int[][] dist;
    static int start;
    static int end;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        e = Integer.parseInt(input[1]);
        dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int i = 0; i < e; i++) {
            int a, b, c;
            input = br.readLine().split(" ");
            a = Integer.parseInt(input[0]);
            b = Integer.parseInt(input[1]);
            c = Integer.parseInt(input[2]);
            graph.get(a-1).add(new Node(b-1, c));
            graph.get(b-1).add(new Node(a-1, c));
        }

        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], INF);
        }


        input = br.readLine().split(" ");
        start = Integer.parseInt(input[0]);
        end = Integer.parseInt(input[1]);

        for (int i = 0; i < n; i++) {
            dist[i][i] = 0;
        }
        distra(0);
        distra(start-1);
        distra(end-1);
        int ans = Math.min(dist[0][start-1] + dist[start-1][end-1] + dist[end-1][n-1], dist[0][end-1] + dist[end-1][start-1] + dist[start-1][n-1]);
        if (ans >= INF) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }
    }

    public static void distra(int s) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (dist[s][cur.v] < cur.w) {
                continue;
            }

            for (Node next : graph.get(cur.v)) {
                if (dist[s][next.v] > next.w + dist[s][cur.v]) {
                    dist[s][next.v] = next.w + dist[s][cur.v];
                    pq.add(new Node(next.v, dist[s][next.v]));
                }
            }
        }
    }

    static class Node implements Comparable<Node> {
        int v;
        int w;
        Node(int v, int w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Node n) {
            return this.w - n.w;
        }
    }
}
