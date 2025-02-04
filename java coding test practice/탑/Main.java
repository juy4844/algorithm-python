package 탑;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Stack<Node> stack = new Stack<>();
        int[] arr = new int[n];
        int[] ans = new int[n];
        String[] str = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
        for (int i = 0; i < n; i++) {
            if (stack.empty()) {
                stack.push(new Node(arr[i], i));
            }
            else {
                while (!stack.empty()) {
                    if (stack.peek().data < arr[i]) {
                        stack.pop();
                    }
                    else {
                        break;
                    }
                }
                if (stack.empty()) {
                    stack.push(new Node(arr[i], i));
                }
                else {
                    ans[i] = stack.peek().index + 1;
                    stack.push(new Node(arr[i], i));
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.print(ans[i] + " ");
        }
    }

    static class Node{
        int data;
        int index;
        public Node(int data, int index) {
            this.data = data;
            this.index = index;
        }
    }
}
