package 문자열_집합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static int n;
    static int m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            map.put(s, 0);
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            String s = br.readLine();
            if (map.containsKey(s)) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}
