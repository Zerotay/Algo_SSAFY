import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _14719_이정호 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int ans = 0;
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        boolean[][] grid = new boolean[H][W];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < W; i++) {
            int range = Integer.parseInt(st.nextToken());
            for (int j = 0; j < range; j++) {
                grid[j][i] = true;
            }
        }

        int tmp = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (grid[i][j]) {
                    while (j + 1 < W && !grid[i][j + 1]) {
                        ++j;
                        ++tmp;
                    }
                }
                if (j + 1 < W && grid[i][j + 1]) {
                    ans += tmp;
                }
                tmp = 0;
            }
        }
        System.out.println(ans);
    }
}