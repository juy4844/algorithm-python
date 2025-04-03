package 택배배송;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {

    static int n;
    static int m;
    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            int c = Integer.parseInt(input[2]);
            graph.get(a).add(new Node(b, c));
            graph.get(b).add(new Node(a, c));
        }

        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[1] = 0;

        PriorityQueue<Temp> pq = new PriorityQueue();
        pq.offer(new Temp(1, 0));

        while (!pq.isEmpty()) {
            Temp temp = pq.poll();

            if (temp.cost > dist[temp.start]) {
                continue;
            }

            for (Node node : graph.get(temp.start)) {
                if (dist[node.end] > temp.cost + node.cost) {
                    dist[node.end] = temp.cost + node.cost;
                    pq.offer(new Temp(node.end, dist[node.end]));
                }
            }
        }

        System.out.println(dist[n]);
    }

    static class Temp implements Comparable<Temp> {
        int cost;
        int start;
        public Temp(int start, int cost) {
            this.start = start;
            this.cost = cost;
        }

        public int compareTo(Temp t) {
            return cost - t.cost;
        }
    }

    static class Node {
        int end;
        int cost;
        public Node(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }
    }
}
