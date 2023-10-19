import java.io.BufferedReader;
// 18870 좌표압축 (S2)
// https://www.acmicpc.net/problem/18870
// 정답


import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		HashMap<Integer, Integer> hmap = new HashMap<>();
		int[] nums = new int[N];
		int[] puts = new int[N];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			puts[i] = nums[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(nums);

		for (int i = 0, idx = 0; i < N; i++) {
			if (hmap.containsKey(nums[i]))
				continue;
			hmap.put(nums[i], idx++);
		}

		for (int i = 0; i < N; i++) {
			sb.append(hmap.get(puts[i]) + " ");
		}
		System.out.println(sb.toString());

	}
}
