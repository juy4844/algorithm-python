package 스카이라인_쉬운거;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    static int n;
    static int[][] arr;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(s[0]);
            arr[i][1] = Integer.parseInt(s[1]);
        }

        Stack<Integer> stack = new Stack<>();


        for (int i = 0; i < n; i++) {
             if (stack.isEmpty()) {
                 if (arr[i][1] != 0) {
                     stack.push(arr[i][1]);
                 }
                 continue;
             }

             if (stack.peek() < arr[i][1]) {
                 stack.push(arr[i][1]);
             } else {
                 if (arr[i][1] == 0) {
                     if (!stack.isEmpty()) {
                         ans += stack.size();
                         stack.clear();
                     }
                 } else {
                     while (!stack.isEmpty()) {
                         if (stack.peek() > arr[i][1]) {
                             stack.pop();
                             ans ++;
                         } else {
                             break;
                         }
                     }

                     if (stack.isEmpty()) {
                         stack.push(arr[i][1]);
                     } else {
                         if (stack.peek() < arr[i][1]) {
                             stack.push(arr[i][1]);
                         }
                     }
                 }
             }
        }
        if (!stack.isEmpty()) {
            ans += stack.size();
        }
        System.out.println(ans);
    }
}
