package 자두나무;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int T;
    static int W;
    static int[] arr;
    static int[][][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        T = Integer.parseInt(input[0]);
        W = Integer.parseInt(input[1]);
        arr = new int[T+1];
        dp = new int[T+1][3][W+1];
        for (int i = 0; i < T; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        if(arr[1] == 1){    //1초일 때, 첫번째 자두가 1번 나무에서 떨어질 경우(초기에 자두는 1번 나무 아래 있음)
            dp[1][0][1] = 1;    //1초일 때, 0번 움직여서, 현재 위치 그대로(1)   -> 자두 1개 먹음 (안움직이고 먹음)
            dp[1][1][2] = 0;    //1초일 때, 1번 움직여서, 현재 위치 바뀌고(2로) => 자두 0개 먹음 (움직이고 못먹음)
        }
        else{                   //1초일 때, 첫번째 자두가 2번 나무에서 떨어질 경우
            dp[1][0][1] = 0;    //1초일 때, 0번 움직이고, 현재 위치 그대로(1) -> 자두 0개 먹음 (안움직이고 못먹음)
            dp[1][1][2] = 1;    //1초일 때, 1번 움직이고, 현재 위치 바뀌고(2로) -> 자두 1개 먹음 (움직이고 먹음)

        }


        for(int t = 2; t<=T; t++){

            if(arr[t] == 1){    //1번 자두나무에서 자두가 떨어질 때
                //w = 0일 때 (안 움직였을 때) 현재 위치에 따른 초기 값 셋팅
                dp[t][0][1] = dp[t-1][0][1] + 1;    //현재 위치 1이면 = 0번 움직이고, 현재 위치 그대로 (안 움직이고 먹음)
                dp[t][0][2] = dp[t-1][0][2];        //현재 위치 2이면 = 0번 움직이고, 현재 위치 그대로 (안 움직이고 못 먹음)

                for(int w = 1; w<=W; w++){
                    //자두가 t초째에 1번 자두나무 아래에 있을 때 (자두 먹은 케이스)
                    dp[t][w][1] = Math.max(dp[t-1][w][1], dp[t-1][w-1][2])+ 1;
                    //자두가 t초째에 2번 자두나무 아래에 있을 때
                    dp[t][w][2] = Math.max(dp[t-1][w-1][1], dp[t-1][w][2]);
                }
            }

            else{                   //2번 자두나무에서 자두가 떨어질 때
                //w = 0일 때 (안 움직였을 때) 현재 위치에 따른 초기 값 셋팅
                dp[t][0][1] = dp[t-1][0][1];        //현재 위치 1이면 = 0번 움직이고, 현재 위치 그대로 (안 움직이고  못 먹음)
                dp[t][0][2] = dp[t-1][0][2] + 1;    //현재 위치 2이면 = 0번 움직이고, 현재 위치 그대로 (안 움직이고 먹음)



                for(int w = 1; w<=W; w++){
                    //자두가 t초째에 1번 자두나무 아래에 있을 때
                    dp[t][w][1] = Math.max(dp[t-1][w][1], dp[t-1][w-1][2]);
                    //자두가 t초째에 2번 자두나무 아래에 있을 때 (자두 먹은 케이스)
                    dp[t][w][2] = Math.max(dp[t-1][w-1][1], dp[t-1][w][2]) + 1;
                }
            }


        }

        int ans = 0;
        for(int w = 0; w<=W; w++){
            ans = Math.max(ans, Math.max(dp[T][w][1], dp[T][w][2]));
        }
        System.out.println(ans);

    }
}
