// 1446 지름길 (S1)
// https://www.acmicpc.net/problem/1446
// N이 최대 12이므로 2^12이면(지름길 방문 or 방문 x) 충분 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N, D;
	static List<Node> data;
	static int result = Integer.MAX_VALUE;

	static class Node {
		int start;
		int end;
		int dist;

		public Node(int start, int end, int dist) {
			this.start = start;
			this.end = end;
			this.dist = dist;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());

		data = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			if (b <= D) {
				data.add(new Node(a, b, c));
			}
		}

		Collections.sort(data, new Comparator<Node>() {
			@Override
			public int compare(Node o1, Node o2) {
				return Integer.compare(o1.start, o2.start);
			}
		});

		solve(0, 0, 0);

		System.out.println(result);
	}

	static void solve(int idx, int x, int count) {
		if (x == D) {
			result = Math.min(result, count);
			return;
		}
		if (idx == data.size() && x < D) {
			result = Math.min(result, count + (D - x));
			return;
		}
		if (x > data.get(idx).start) { // 이미 지난 거리면
			solve(idx + 1, x, count);
		} else {
			if (x == data.get(idx).start) {// 지름길 O
				solve(idx + 1, data.get(idx).end, count + data.get(idx).dist);
			} else { // 현재 바로 지름길을 탈 수 없는 경우
				solve(idx + 1, data.get(idx).end, count + data.get(idx).dist + (data.get(idx).start - x));
			}
			solve(idx + 1, x, count); // 지름길 선택 x
		}
	}

}
