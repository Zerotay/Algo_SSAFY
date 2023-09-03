package BOJ.dp;

import java.util.ArrayList;
import java.util.List;

public class Main_1446_S1_지름길_dp {
	static class Point {
		int start, end, d;

		public Point(int start, int end, int d) {
			this.start = start;
			this.end = end;
			this.d = d;
		}
	}

	public static void main(String[] args) throws Exception {
		int N = read();
		int D = read();

		int[] dp = new int[D + 1];
		List<Point> graph = new ArrayList<Point>();

		int s, e, d; // start, end, distance
		for (int i = 0; i < N; i++) {
			s = read();
			e = read();
			d = read();
			if (e - s <= d)
				continue;
			if (e > D)
				continue;
			graph.add(new Point(s, e, d));
		}

		int size = graph.size();
		Point p;

		for (int i = 1; i <= D; i++) {
			dp[i] = dp[i - 1] + 1;
			for (int j = 0; j < size; j++) {
				p = graph.get(j);
				if (p.end == i) {
					dp[i] = Math.min(dp[p.start] + p.d, dp[i]);
				}
			}
		}
		System.out.println(dp[D]);
	}

	private static int read() throws Exception {
		int c, n = System.in.read() & 15;
		while ((c = System.in.read()) > 32)
			n = (n << 3) + (n << 1) + (c & 15);
		return n;
	}
}