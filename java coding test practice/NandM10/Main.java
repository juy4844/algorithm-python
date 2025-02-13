package NandM10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedHashSet;

public class Main {
    static int n;
    static int m;
    static int[] arr;
    static int[] result;
    static boolean[] visited;
    static LinkedHashSet<String> ans = new LinkedHashSet<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        arr = new int[n];
        visited = new boolean[n];
        result = new int[m];

        input = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(arr);
        dfs(0,0);
        for (String s : ans) {
            System.out.println(s);
        }
    }

    static void dfs(int start, int index) {
        if (index == m) {
            StringBuilder sb = new StringBuilder();
            for (int p : result) {
                sb.append(p).append(" ");
            }
            ans.add(sb.toString());
            return;
        }
        for (int i = start; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result[index] = arr[i];
                dfs(i, index + 1);
                visited[i] = false;
            }
        }
    }
}
