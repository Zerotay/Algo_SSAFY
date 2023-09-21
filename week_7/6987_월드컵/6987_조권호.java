// 6987 월드컵 (G4)
// https://www.acmicpc.net/problem/6987
// 실패

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N, M, ans;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 4; i++) {
			int[][] match = new int[6][3];
			st = new StringTokenizer(br.readLine());

			for (int j = 0; j < 18; j++) {
				int a = j / 3;
				int b = j % 3;
				match[a][b] = Integer.parseInt(st.nextToken());
			}

			boolean flag = false;
			int win = 0, lose = 0;
			int[][] draw = new int[6][2];

			for (int j = 0; j < 6; j++) {
				int cnt = 0;
				draw[j][0] = j;

				for (int k = 0; k < 3; k++) {
					if (k == 0)
						win+=match[j][k];
					else if (k == 2)
						lose+=match[j][k];
					else if (k == 1 && match[j][k]!=0) {
						draw[j][1] += match[j][k];
					}
					cnt += match[j][k];
				}

				if (cnt != 5) {
					flag = true;
					break;
				}
			}

			if (flag || (win != lose)) {
				sb.append(0 + " ");
				continue;
			}

			Arrays.sort(draw, (o1, o2) -> {
				return o2[1] - o1[1];
			});
//			for (int j = 0; j < 6; j++) {
//				for (int j2 = 0; j2 < 2; j2++) {
//					System.out.print(draw[j][j2]+" ");
//				}System.out.println();
//			}

			for (int j = 0; j < 5; j++) {
				if (draw[j][1] != 0) {
					for (int k = j + 1; k < 6; k++) {
						if (draw[j][1] > 0 && draw[k][1] > 0) {
							draw[j][1] -= 1;
							draw[k][1] -= 1;
						}
					}
					if (draw[j][1] != 0) {
						flag = true;
						break;
					}
				}
			}

			if (flag || draw[5][1] != 0) {
				sb.append(0 + " ");
				continue;
			}
			sb.append(1 + " ");
		}
		System.out.println(sb);
	}
}

/*
5승 한 팀이 있으면 다른 팀들은 다 1패 씩을 해야됨 etc..
5 0 0 5 0 0 5 0 0 0 0 5 0 0 5 0 0 5
5 0 0 4 0 1 4 0 1 1 0 4 1 0 4 0 0 5
0 5 0 5 0 0 0 0 5 0 5 0 0 5 0 0 5 0
0 5 0 0 5 0 3 0 2 2 0 3 4 0 1 1 0 4
out: 1 1 0 0 
ans: 0 0 0 0 
*/