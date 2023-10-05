// 2294 동전 2 (G5)
// https://www.acmicpc.net/problem/2294
// 정답

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N,K;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		ArrayList<Integer> coins = new ArrayList<>();
		int[] dp = new int[K+1];

		Arrays.fill(dp, 10001);
		for (int i = 0; i < N; i++) {
			coins.add(Integer.parseInt(br.readLine()));
		}

		dp[0]=0;
		for(int coin: coins) {
			for (int i = coin; i < K+1; i++) {
				dp[i] = Math.min(dp[i], dp[i-coin]+1);
			}
		}

		if(dp[K]==10001)
            System.out.println(-1);
		else 
            System.out.println(dp[K]);
	}

}