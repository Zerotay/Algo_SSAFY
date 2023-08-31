// 1238 게임 (G3)
// https://www.acmicpc.net/problem/1238
// 성공
package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main_1238_G3_파티 {
	static class Node implements Comparable<Node> {
		int v, weight;

		public Node(int v, int weight) {
			this.v = v;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.weight, o.weight);
		}
	}

	private static final int INF = Integer.MAX_VALUE;
	static int V, E, A;
	static List<Node>[] list, revList;

	public static void main(String[] args) throws Exception {
		V = read(); // 정점 수
		E = read(); // Edge 수
		// S = Integer.parseInt(st.nextToken()); //시작 정점
		A = read(); // 도착 정점

		list = new ArrayList[V + 1];
		revList = new ArrayList[V + 1];
		
		for (int i = 0; i <= V; i++) {
			list[i] = new ArrayList<>();
			revList[i] = new ArrayList<>();
		}

		//
		

		// 출발 도착 가중치
		for (int i = 0; i < E; i++) {
			int u = read();
			int v = read();
			int weight = read();
			list[u].add(new Node(v, weight));
			revList[v].add(new Node(u, weight));
		}
		int[] dist1 = dijkstra(list); 
        int[] dist2 = dijkstra(revList); 
		// 다익스트라 알고리즘
		int ans = 0;
		for (int i = 1; i <= V; i++) {
			ans = Math.max(ans, dist1[i] + dist2[i]);
		}
		System.out.println(ans);
	}


	static int[] dijkstra(List<Node>[] list) {
		PriorityQueue<Node> queue = new PriorityQueue<>();
		int[] dist = new int[V + 1];
		Arrays.fill(dist, INF);
		// 선택배열
		boolean[] check = new boolean[V + 1];
		// 도착 노드를 pq에 삽입
		queue.add(new Node(A, 0));
		// 도착 노드까지의 거리는 0
		dist[A] = 0;

		while (!queue.isEmpty()) {
			// 하나 꺼내서
			Node curNode = queue.poll();
			// 정점
			int cur = curNode.v;
			// 이 이미 선택됐다면
			if (check[cur])
				continue;
			// 선택한걸로 치고
			check[cur] = true;
			// 여기서 출발해서 도착할 수 있는 모든 정점들에 대해서
			for (Node node : list[cur]) {
				// 이미 알고 있는 거리보다 더 가깝게 도달할 수 있다면
				if (dist[node.v] > dist[cur] + node.weight) {
					// 거리 갱신하고
					dist[node.v] = dist[cur] + node.weight;
					queue.add(new Node(node.v, dist[node.v]));
				}
			}
		}
		return dist;
	}
	private static int read() throws Exception {

        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13)
            System.in.read();
        return n;

    }
}
