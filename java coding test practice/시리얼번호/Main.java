package 시리얼번호;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    static int n;
    static String[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine();
        }

        CustomComparator customComparator = new CustomComparator();
        Arrays.sort(arr,customComparator);

        for (String s : arr) {
            System.out.println(s);
        }
    }
    static class CustomComparator implements Comparator<String> {

        @Override
        public int compare(String o1, String o2) {
            if (o1.length() < o2.length()) {
                return -1;
            }
            else if (o1.length() > o2.length()) {
                return 1;
            }
            else {
                int num1 = 0;
                int num2 = 0;
                for (int i = 0; i < o1.length(); i++) {
                    if (o1.charAt(i) >= '1' && o1.charAt(i) <= '9') {
                        num1 += o1.charAt(i) - '0';
                    }
                }
                for (int i = 0; i < o2.length(); i++) {
                    if (o2.charAt(i) >= '1' && o2.charAt(i) <= '9') {
                        num2 += o2.charAt(i) - '0';
                    }
                }
                if (num1 < num2) {
                    return -1;
                }
                else if (num1 > num2) {
                    return 1;
                }
                else {
                    return o1.compareTo(o2);
                }
            }
        }
    }
}
