package 트리순회2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

public class Main {

    static int ans = 0;

    static HashMap<Integer, Node> tree = new HashMap<>();
    static Stack<Integer> stack = new Stack<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            int a = Integer.parseInt(s[0]);
            int b = Integer.parseInt(s[1]);
            int c = Integer.parseInt(s[2]);

            tree.put(a, new Node(b, c));
        }
        inOrder(1);
        int end = stack.peek();
        midOrder(1, end);

    }

    static void inOrder(int cur) {
        if (cur == -1) {
            return;
        }
        inOrder(tree.get(cur).left);
        stack.push(cur);
        inOrder(tree.get(cur).right);
    }


    static void midOrder(int cur, int end) {


        ans += 1;
        if (tree.get(cur).left != -1) {
            midOrder(tree.get(cur).left, end);
            ans += 1;
        }
        if (tree.get(cur).right != -1) {
            midOrder(tree.get(cur).right, end);
            ans += 1;
        }

        if (cur == end) {
            System.out.println(ans-1);
        }

    }


    static class Node {
        int left;
        int right;
        public Node(int left, int right) {
            this.left = left;
            this.right = right;
        }
    }
}

