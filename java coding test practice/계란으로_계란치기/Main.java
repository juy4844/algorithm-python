package 계란으로_계란치기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    static Egg[] arr;
    static int max;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new Egg[n];
        for (int i = 0; i < n; i++) {
            String[] str = br.readLine().split(" ");
            int s = Integer.parseInt(str[0]);
            int w = Integer.parseInt(str[1]);
            arr[i] = new Egg(s, w);
        }
        dfs(0);
        System.out.println(max);
    }

    static void dfs(int index) {
        if (index == n) {
            int temp = 0;
            for (int i = 0; i < n; i++) {
                if (arr[i].s <= 0) {
                    temp++;
                }
            }
            max = Math.max(max, temp);
            return;
        }
        int broken = 0;

        if (arr[index].s <= 0) {
            dfs(index + 1);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (arr[i].s <= 0) {
                broken++;
            }
        }

        if (broken == n-1) {
            max = Math.max(max, broken);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (i == index) {
                continue;
            }
            if (arr[i].s <= 0) {
                continue;
            }
            arr[i].s -= arr[index].w;
            arr[index].s -= arr[i].w;

            dfs(index+1);

            arr[i].s += arr[index].w;
            arr[index].s += arr[i].w;
        }


    }

    static class Egg {
        int s;
        int w;
        public Egg(int s, int w) {
            this.s = s;
            this.w = w;
        }
    }
}
