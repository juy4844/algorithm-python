package 빗물;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        int h = Integer.parseInt(input[0]);
        int w = Integer.parseInt(input[1]);

        int[] arr = new int[w];
        input = br.readLine().split(" ");
        for (int i = 0; i < w; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        int ans = 0;

        Queue<Integer> queue = new LinkedList<>();
        int left = arr[0];
        int leftIndex = 0;

        for (int i = 1; i < w; i++) {
            if (left > arr[i]) {
                queue.add(arr[i]);
            } else {

                while (!queue.isEmpty()) {
                    int temp = queue.poll();
                    ans += (left - temp);
                }
                left = arr[i];
                leftIndex = i;
            }
        }

        Queue<Integer> queue1 = new LinkedList<>();
        int right = arr[w-1];
        for (int i = w-2; i >= leftIndex; i--) {
            if (right > arr[i]) {
                queue1.add(arr[i]);
            } else {

                while (!queue1.isEmpty()) {
                    int temp = queue1.poll();
                    ans += (right - temp);
                }
                right = arr[i];
            }
        }

        System.out.println(ans);
    }
}
