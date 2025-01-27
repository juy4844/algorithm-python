package 스도쿠;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

    static int[][] sdo = new int[9][9];
    static ArrayList<Point> block = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < 9; j++) {
                sdo[i][j] = Integer.parseInt(input[j]);
                if (sdo[i][j] ==  0) {
                    block.add(new Point(i, j));
                }
            }
        }

        dfs(0);

    }

    static int dfs(int index) {
        if (index == block.size()) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.print(sdo[i][j] + " ");
                }
                System.out.println();
            }
            return -1;
        }

        for (int i = 1; i <= 9; i++) {
            int temp = i;
            boolean flag = true;
            for (int j = 0; j < 9; j++) {
                if (sdo[block.get(index).x][j] == temp || sdo[j][block.get(index).y] == temp) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                int startx = block.get(index).x / 3 * 3;
                int starty = block.get(index).y / 3 * 3;
                for (int j = 0; j < 3; j++) {
                    for (int k = 0; k < 3; k++) {
                        if (sdo[startx + k][starty + j] == temp) {
                            flag = false;
                            break;
                        }
                        if (flag == false) {
                            break;
                        }
                    }
                }
            }

            if (flag) {
                sdo[block.get(index).x][block.get(index).y] = temp;
                if (dfs(index + 1) == -1) {
                    return -1;
                }
                sdo[block.get(index).x][block.get(index).y] = 0;
            }
        }

        return 1;
    }

    static class Point {
        int x;
        int y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
