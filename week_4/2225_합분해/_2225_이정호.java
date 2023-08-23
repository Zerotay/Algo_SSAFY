import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final long[][] d = new long[201][201];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        d[0][0] = 1;

        for (int i = 1; i <= K; i++) {
            for (int j = 0; j <= N; j++) {
                for (int l = 0; l <= j; l++) {
                    d[i][j] += d[i - 1][j - l];
                    d[i][j] %= 1000000000;
                }
            }
        }

        System.out.println(d[K][N]);
    }
}