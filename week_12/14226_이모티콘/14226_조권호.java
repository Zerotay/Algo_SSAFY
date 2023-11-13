// 14226 이모티콘 (G4)
// https://www.acmicpc.net/problem/14226
// 실패

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static StringTokenizer st;
	static int S;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		S = Integer.parseInt(br.readLine());
		boolean[] visited = new boolean[S + 1000];

		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { 1, 1, 1 });
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			if (cur[0] <= 0 || cur[0] >= (S + 1000) || visited[cur[0]])
				continue;
			if (cur[0] == S) {
				sb.append(cur[1]);
				q.clear();
				break;
			}
			visited[cur[0]] = true;
			q.add(new int[] { cur[0] + cur[2], cur[1] + 1, cur[2] });
			q.add(new int[] { cur[0] - 1, cur[1] + 1, cur[2] });
			cur[2] = cur[0];
			q.add(new int[] { cur[0] + cur[2], cur[1] + 2, cur[2] });
		}
		System.out.println(sb.toString());
	}
}
