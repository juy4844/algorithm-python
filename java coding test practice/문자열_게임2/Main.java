package 문자열_게임2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String w = br.readLine();
            int k = Integer.parseInt(br.readLine());
            int numMax = -1;
            int numMin = 10001;
            HashMap<Character, Queue<Integer>> map = new HashMap<>();
            for (int j = 0; j < w.length(); j++) {
                if (!map.containsKey(w.charAt(j))) {
                    map.put(w.charAt(j), new LinkedList<>());
                }
                if (map.get(w.charAt(j)).size() < k-1) {
                    map.get(w.charAt(j)).add(j);
                } else if (map.get(w.charAt(j)).size() == k-1) {
                    map.get(w.charAt(j)).add(j);
                    numMin = Math.min(numMin, j - map.get(w.charAt(j)).peek() + 1);
                    numMax = Math.max(numMax, j - map.get(w.charAt(j)).peek() + 1);
                } else {
                    map.get(w.charAt(j)).poll();
                    map.get(w.charAt(j)).add(j);
                    numMin = Math.min(numMin, j - map.get(w.charAt(j)).peek() + 1);
                    numMax = Math.max(numMax, j - map.get(w.charAt(j)).peek() + 1);
                }
            }

            if (numMax == -1) {
                System.out.println(-1);
            } else {
                System.out.print(numMin + " ");
                System.out.println(numMax);
            }
        }
    }
}
