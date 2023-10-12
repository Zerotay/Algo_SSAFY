// 2313 보석 구매하기 (S1)
// https://www.acmicpc.net/problem/2313
// 실패

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int N = Integer.parseInt(br.readLine());
		int ans_max=0;
		for (int i = 0; i < N; i++) {
			int L = Integer.parseInt(br.readLine());
			int[] jewels = new int[L];

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < L; j++) {
				jewels[j] = Integer.parseInt(st.nextToken());
			}

			int left = 0;
			int right = 0;
			int ans_l = 0;
			int ans_r = 0;

			int max = jewels[0];
			for (int j = 1; j < L; j++) {
				if(jewels[j]==max) {
					ans_l = j;
					ans_r = j;
					break;
				}
				
				if(jewels[j]>0) {
					right=j;
					jewels[j] +=jewels[j-1];
				}
				else if(jewels[j]==0) continue;
				else {
					left=j;
					jewels[j] -=jewels[j-1];
				}
				
				
				
				if(jewels[j]>max) {
					ans_l = left;
					ans_r = right;
					max = jewels[j];
				}else if(jewels[j]==max && (ans_r-ans_l)>(right-left)) {
					ans_l = left;
					ans_r = right;
				}
			}
			ans_l++;	// 1부터 시작
			ans_r++;
			sb.append(ans_l + " " + ans_r + "\n");
			ans_max+=max;
		}
		
		StringBuilder ans = new StringBuilder();
		ans.append(ans_max+"\n");
		ans.append(sb);
		
		System.out.println(ans.toString());
	}
}