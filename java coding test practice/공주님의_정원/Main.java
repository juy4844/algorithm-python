package 공주님의_정원;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        Flower[] flowers = new Flower[n];

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            int startMonth = Integer.parseInt(s[0]);
            int startDay = Integer.parseInt(s[1]);
            int endMonth = Integer.parseInt(s[2]);
            int endDay = Integer.parseInt(s[3]);

            int start = startMonth * 100 + startDay;
            int end = endMonth * 100 + endDay;
            flowers[i] = new Flower(start, end);
        }

        Arrays.sort(flowers);

        int endDay = 1201;
        int start = 301;
        int count = 0;
        int max = 0;
        int index = 0;

        while(start < endDay) {
            boolean isFinded = false;

            for(int i = index; i < n; i++) {
                if(flowers[i].start > start) {
                    break;
                }

                if(max < flowers[i].end) {
                    isFinded = true;
                    max = flowers[i].end;
                    index = i + 1;
                }
            }

            if(isFinded) {
                start = max;
                count++;
            }
            else {
                break;
            }
        }

        if(max < endDay) {
            System.out.println(0);
        }
        else {
            System.out.println(count);
        }

    }

    static class Flower implements Comparable<Flower> {
        int start;
        int end;

        public Flower(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Flower o) {
            if (this.start < o.start) {
                return -1;
            }
            else if (this.start == o.start) {
                if (this.end > o.end) {
                    return -1;
                }
                else if (this.end == o.end) {
                    return 0;
                }
                else {
                    return 1;
                }
            }
            else {
                return 1;
            }
        }
    }
}
