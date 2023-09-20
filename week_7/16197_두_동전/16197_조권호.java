// 16197 두 동전(G4)
// https://www.acmicpc.net/problem/16197
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N, M, ans = Integer.MAX_VALUE;
	static char[][] board;
	static StringTokenizer st;
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		ArrayList<int[]> coin = new ArrayList<>();
		board = new char[N][M];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				board[i][j] = str.charAt(j);
				if (board[i][j] == 'o')
					coin.add(new int[] { i, j });
			}
		}
		dfs(0, coin);
		
		if(ans==Integer.MAX_VALUE) System.out.println(-1);
		else System.out.println(ans);
	}

	private static void dfs(int dep, ArrayList<int[]> coin) {
		if (dep >= 10 || dep >= ans) {
			return;
		}
		for (int i = 0; i < 4; i++) {
			int x1 = coin.get(0)[0]+dx[i];
			int y1 = coin.get(0)[1]+dy[i];
			int x2 = coin.get(1)[0]+dx[i];
			int y2 = coin.get(1)[1]+dy[i];
			int cnt = 0;

			if (x1 < 0 || x1 >= N || y1 < 0 || y1 >= M) {
				cnt++;
			}
			if (x2 < 0 || x2 >= N || y2 < 0 || y2 >= M) {
				cnt++;
			}
			if (cnt == 2) {
				continue;
			}
			if (cnt == 1) {
				ans = Math.min(ans, dep + 1);
				return;
			}
			if (board[x1][y1] == '#') {
				x1 = coin.get(0)[0];
				y1 = coin.get(0)[1];
			}
			if (board[x2][y2] == '#') {
				x2 = coin.get(1)[0];
				y2 = coin.get(1)[1];
			}
			ArrayList<int[]> tmp = new ArrayList<>();
			tmp.add(new int[] {x1,y1});
			tmp.add(new int[] {x2,y2});
			dfs(dep+1, tmp);
		}
	}
}

// 최대 10회이기 때문에 사방을 모두 완탐한다 해도 4^10밖에 안 됨=> visit체크 안해줘도 되겠다 대신 백트래킹
