package 최소비용구하기2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int start;
    static int end;
    static HashMap<Integer, ArrayList<Node>> map;
    static int d[], preCity[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        d = new int[n+1];
        Arrays.fill(d, Integer.MAX_VALUE);
        preCity = new int[n+1];
        map = new HashMap<>();

        for (int i = 1; i < n+1; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            int c = Integer.parseInt(input[2]);
            map.get(a).add(new Node(b, c));
        }
        String[] input = br.readLine().split(" ");
        start = Integer.parseInt(input[0]);
        end = Integer.parseInt(input[1]);

        distra(start);
        System.out.println(d[end]);

        int cnt = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(end);
        int temp = end;
        while (preCity[temp] != start) {
            cnt +=1;
            stack.push(preCity[temp]);
            temp = preCity[temp];
        }
        stack.push(start);
        System.out.println(cnt + 2);
        while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }
    }

    static void distra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));
        d[start] = 0;

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            int cur = curNode.to;
            if (d[cur] < curNode.weight) {
                continue;
            }
            for (Node node : map.get(cur)) {
                if (d[node.to] > node.weight + d[cur]) {
                    d[node.to] = node.weight + d[cur];
                    preCity[node.to] = cur;
                    pq.offer(new Node(node.to, d[node.to]));
                }
            }
        }
    }

    static class Node implements Comparable<Node> {
        int to;
        int weight;
        Node(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }
}
