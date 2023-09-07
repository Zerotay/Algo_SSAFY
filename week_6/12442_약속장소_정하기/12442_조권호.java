import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N,P,M;
	static int[][] friends;
	static ArrayList[] graph;
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc < T+1; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			P = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			friends = new int[P][2];
			for (int p = 0; p < P; p++) {
				st = new StringTokenizer(br.readLine());
				friends[p][0] = Integer.parseInt(st.nextToken());
				friends[p][1] = Integer.parseInt(st.nextToken());
			}
			for (int m = 0; m < M; m++) {
				st = new StringTokenizer(br.readLine());
				int D = Integer.parseInt(st.nextToken());
				int L = Integer.parseInt(st.nextToken());
				graph = new ArrayList[L+1];
				for (int i = 0; i < L+1; i++) {
					graph[i] = new ArrayList<>();
				}
				ArrayList<Integer> tmp = new ArrayList<>();
				for (int i = 0; i < L; i++) {
					tmp.add(Integer.parseInt(st.nextToken()));
				}
				for (int i = 1; i < tmp.size(); i++) {
					int a = tmp.get(i-1);
					int b = tmp.get(i);
					graph[a].add(new int[] {D, b});
					graph[b].add(new int[] {D,a});
				}
			}
			int[] cost = new int[N];
			for (int i = 0; i < P; i++) {
				dijkstra(friends[i][0]);
				// P번 다익스트라 돌면서 모든 도시의 최단거리를 구하는데 가장 오래 걸리는 친구의 시간을 기록해야 모두 도착하는 최단시간
				// 가장 최소인 cost값 출력
			}
			
			
			sb.append("Case #"+tc+": ");
		}
	}


	private static int dijkstra(int i) {
		return 0;
	}
}
