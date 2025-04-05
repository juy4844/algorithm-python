package 트리순회;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;


public class Main {

    static HashMap<String, Node> tree = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");

            if (s[1].equals(".") && s[2].equals(".")) {
                tree.put(s[0], new Node(null, null));
            } else if (s[1].equals(".")) {
                tree.put(s[0], new Node(null, s[2]));
            } else if (s[2].equals(".")) {
                tree.put(s[0], new Node(s[1], null));
            } else {
                tree.put(s[0], new Node(s[1], s[2]));
            }

        }
        preOrder("A");
        System.out.println();
        midOrder("A");
        System.out.println();
        postOrder("A");
        System.out.println();
    }

    static void preOrder(String cur) {
        if (cur == null) {
            return;
        }
        System.out.print(cur);
        preOrder(tree.get(cur).left);
        preOrder(tree.get(cur).right);
    }

    static void midOrder(String cur) {
        if (cur == null) {
            return;
        }

        midOrder(tree.get(cur).left);
        System.out.print(cur);
        midOrder(tree.get(cur).right);
    }

    static void postOrder(String cur) {
        if (cur == null) {
            return;
        }

        postOrder(tree.get(cur).left);
        postOrder(tree.get(cur).right);
        System.out.print(cur);
    }

    static class Node {
        String left;
        String right;
        public Node(String left, String right) {
            this.left = left;
            this.right = right;
        }
    }
}
