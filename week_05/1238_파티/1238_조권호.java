import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static final int INF = Integer.MAX_VALUE;
	static int N, M, X, ans;
	static List<Node>[] list;
	static List<Node>[] list2;
	static int[] dist, dist2;

	static class Node implements Comparable<Node> {
		int v, weight;

		public Node(int v, int weight) {
			super();
			this.v = v;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.weight, o.weight);
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());

		list = new ArrayList[N + 1];
		list2 = new ArrayList[N + 1];

		for (int i = 0; i <= N; i++) {
			list[i] = new ArrayList<>();
			list2[i] = new ArrayList<>();
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());
			list[start].add(new Node(end, time));
			list2[end].add(new Node(start, time));
		}
		ans = 0;
		for (int i = 1; i < N + 1; i++) {
			dist = new int[N + 1];
			dist2 = new int[N + 1];
			int a=0;
			int b=0;
			Arrays.fill(dist, INF);
			Arrays.fill(dist2, INF);
			a=dijkstra(i);
			b=dijkstra2(i);
			ans = Math.max(ans, a+b);
		}

		System.out.println(ans);
	}

	private static int dijkstra(int i) {
		PriorityQueue<Node> q = new PriorityQueue<>();
		boolean[] check = new boolean[N + 1];
		q.offer(new Node(i, 0));
		dist[i] = 0;
		int cnt=0;
		while (!q.isEmpty()) {
			Node curNode = q.poll();
			int cur = curNode.v;
			if(cur==X) {
				cnt = Math.max(ans, dist[X]);
				return cnt;
			}
			if (check[cur])
				continue;
			check[cur] = true;
			for (Node node : list[cur]) {
				if (dist[node.v] > dist[cur] + node.weight) {
					dist[node.v] = dist[cur] + node.weight;
					q.add(new Node(node.v, dist[node.v]));
				}
			}
		}
		return cnt;
	}
	private static int dijkstra2(int i) {
		PriorityQueue<Node> q = new PriorityQueue<>();
		boolean[] check = new boolean[N + 1];
		q.offer(new Node(X, 0));
		dist2[X] = 0;
		int cnt=0;
		while (!q.isEmpty()) {
			Node curNode = q.poll();
			int cur = curNode.v;
			if(cur==i) {
				cnt = Math.max(cnt, dist2[i]);
				return cnt;
			}
			if (check[cur])
				continue;
			check[cur] = true;
			for (Node node : list[cur]) {
				if (dist2[node.v] > dist2[cur] + node.weight) {
					dist2[node.v] = dist2[cur] + node.weight;
					q.add(new Node(node.v, dist2[node.v]));
				}
			}
		}
		return cnt;
	}
}