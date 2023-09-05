//

package BOJ.failed;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class Main {
    static class Edge implements Comparable<Edge> {
        int u, c;

        Edge(int u, int c) {
            this.u = u;
            this.c = c;
        }

        @Override
        public int compareTo(Edge t) {
            return Integer.compare(t.c, this.c);
        }
    }

    private static final int INF = Integer.MAX_VALUE / 2;

    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        int T = read();

        for (int tc = 1; tc <= T; tc++) {
            int N = read();
            int P = read();
            int M = read();
            List<Edge>[] Gph = new ArrayList[N + 1];

            for (int i = 1; i <= N; i++) {
                Gph[i] = new ArrayList<>();
            }

            int[] X = new int[P + 1];
            int[] V = new int[P + 1];

            for (int i = 1; i <= P; i++) {
                X[i] = read();
                V[i] = read();
            }

            for (int i = 0; i < M; i++) {
                int d = read();
                int l = read();
                int s = read();
                for (int j = 1; j < l; j++) {
                    int t = read();
                    Gph[s].add(new Edge(t, d));
                    Gph[t].add(new Edge(s, d));
                    s = t;
                }
            }
            // while (M-- > 0) {
            // int d = read();
            // int l = read();
            // int s = read();

            // while (--l > 0) {
            // int t = read();
            // Gph[s].add(new Edge(t, d));
            // Gph[t].add(new Edge(s, d));
            // s = t;
            // }
            // }

            // dijkstra

            int[] dist = new int[N + 1];
            boolean[] visited = new boolean[N + 1];
            PriorityQueue<Edge> PQ = new PriorityQueue<>();
            boolean[] cannot = new boolean[N + 1];
            int[] result = new int[N + 1];

            for (int w = 1; w <= P; w++) {
                int u = X[w];

                Arrays.fill(dist, INF);
                Arrays.fill(visited, false);
                PQ.clear();

                PQ.add(new Edge(u, 0));
                dist[u] = 0;

                while (!PQ.isEmpty()) {
                    Edge t = PQ.poll();
                    if (visited[t.u])
                        continue;
                    visited[t.u] = true;
                    // if (dist[t.u] < t.c)
                    // continue;
                    for (Edge e : Gph[t.u]) {
                        if (!visited[e.u] &&
                                dist[e.u] > t.c + e.c) {
                            dist[e.u] = t.c + e.c;
                            PQ.offer(new Edge(e.u, t.c + e.c));
                        }
                    }
                }

                for (int i = 1; i <= N; i++) {
                    if (!visited[i])
                        cannot[i] = true;
                    else
                        result[i] = Math.max(result[i], dist[i] * V[w]);
                }
            }

            int res = INF;
            boolean stored = false;

            for (int i = 1; i <= N; i++) {
                if (!cannot[i]) {
                    stored = true;
                    res = Math.min(res, result[i]);
                }
            }
            sb.append("Case #" + tc + ": " + (stored ? res : -1)).append("\n");
        }
        System.out.print(sb.toString());
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