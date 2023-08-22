package sol;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Tmp {
	static int N, M, arr[], tree[], tree2[], a, b;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int init(int node, int start, int end) {
		if (start == end) {
			return tree[node] = arr[start];
		} else {

			int nn = node << 1;
			int mid = (start + end) >> 1;
			return tree[node] = Math.min(init(nn, start, mid), init(nn + 1, mid + 1, end));
		}
	}
	static int init2(int node, int start, int end) {
		if (start == end) {
			return tree2[node] = arr[start];
		} else {

			int nn = node << 1;
			int mid = (start + end) >> 1;
			return tree2[node] = Math.max(init2(nn, start, mid), init2(nn + 1, mid + 1, end));
		}
	}

	static int minval(int node, int start, int end, int left, int right) {
		if (left > end || right < start) {
			return Integer.MAX_VALUE;
		}
		if (left <= start && end <= right) {
			return tree[node];
		}

		int nn = node << 1;
		int mid = (start + end) >> 1;
		return Math.min(minval(nn, start, mid, left, right), minval(nn + 1, mid + 1, end, left, right));
	}

	static int maxval(int node, int start, int end, int left, int right) {
		if (left > end || right < start) {
			return 0;
		}
		if (left <= start && end <= right) {
			return tree2[node];
		}

		int nn = node << 1;
		int mid = (start + end) >> 1;
		return Math.max(maxval(nn, start, mid, left, right), maxval(nn + 1, mid + 1, end, left, right));
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N];
		tree = new int[N << 2];
		tree2 = new int[N << 2];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		init(1, 0, N - 1);
		init2(1, 0, N - 1);
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken()) - 1;
			b = Integer.parseInt(st.nextToken()) - 1;
			sb.append(minval(1, 0, N - 1, a, b)+" "+maxval(1, 0, N - 1, a, b)+"\n");
			
		}
		System.out.println(sb);
	}

}
