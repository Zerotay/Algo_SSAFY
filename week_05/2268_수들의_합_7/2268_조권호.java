import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static long[] arr, tree;

	static long init(int node, int start, int end) {
		if (start == end) {
			return tree[node] = arr[start];
		}
		int nn = node << 1;
		int mid = (start + end) >> 1;
		return tree[node]= init(nn, start, mid) + init(nn + 1, mid + 1, end);
	}

	static long sum(int node, int start, int end, long a, long b) {
		if (a > end || b < start) {
			return 0;
		}

		if (start >= a && end <= b) {
			return tree[node];
		}

		int nn = node << 1;
		int mid = (start + end) >> 1;
		return sum(nn, start, mid, a, b) + sum(nn + 1, mid + 1, end, a, b);
	}

	static void modify(int node, int start, int end, long a, long tmp) {
		if (a < start || a > end) {
			return ;
		}
		tree[node] += tmp;
		if (start == end) {
			arr[(int)a] = tree[node];
			return;
		}
		int nn = node << 1;
		int mid = (start + end) >> 1;
		modify(nn, start, mid, a, tmp);
		modify(nn + 1, mid + 1, end, a, tmp);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new long[N + 1];
		tree = new long[N << 2];

//		init(1, 0, N);

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int command = Integer.parseInt(st.nextToken());
			long a = Long.parseLong(st.nextToken());
			long b = Long.parseLong(st.nextToken());
			if (command == 0) {
				if(a>b) {
					long tmp =a;
					b=a;
					a=tmp;
				}
				sb.append(sum(1, 0, N, a, b)+"\n");
			} else if (command == 1) {
				long tmp = b - arr[(int)b];
				modify(1, 0, N, a, tmp);
//				System.out.println(Arrays.toString(tree));
			}
		}
		System.out.println(sb);
	}
}