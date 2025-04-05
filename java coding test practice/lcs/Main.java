package lcs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String a = br.readLine();
        String b = br.readLine();

        int ans;

        int[][] lcs = new int[a.length()][b.length()];
        if (a.charAt(0) == b.charAt(0)) {
            lcs[0][0] = 1;
            ans = 1;
        } else {
            lcs[0][0] = 0;
            ans = 0;
        }

        for (int i = 1; i < b.length(); i++) {
            if (a.charAt(0) == b.charAt(i)) {
                lcs[0][i] = 1;
            } else {
                lcs[0][i] = lcs[0][i-1];
            }
            ans = Math.max(ans, lcs[0][i]);
        }

        for (int i = 1; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(0)) {
                lcs[i][0] = 1;
            } else {
                lcs[i][0] = lcs[i-1][0];
            }
            ans = Math.max(ans, lcs[i][0]);
        }



        for (int i = 1; i < a.length(); i++) {
            for (int j = 1; j < b.length(); j++) {
                if (a.charAt(i) == b.charAt(j)) {
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                } else {
                    lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
                }
                ans = Math.max(ans, lcs[i][j]);
            }
        }

        System.out.println(ans);
    }
}
