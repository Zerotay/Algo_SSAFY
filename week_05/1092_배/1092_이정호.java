// 1092 배 (G5)
// https://www.acmicpc.net/problem/1092
// 성공

package BOJ;

import java.io.IOException;
import java.util.Arrays;

public class Main_1092_G5_배 {

    static int N, M, total, result;
    static int[] limit, weight, boxes;

    public static void main(String[] args) throws IOException {
        N = read();
        limit = new int[N];
        for (int i = 0; i < N; i++)
            limit[i] = read();

        M = read();
        weight = new int[M];
        for (int i = 0; i < M; i++)
            weight[i] = read();

        Arrays.sort(weight);
        Arrays.sort(limit);

        boxes = new int[N];
        int j = 0;
        for (int i = 0; i < N; i++) {
            int count = 0;
            while (j < M) {
                if (limit[i] < weight[j])
                    break;
                j++;
                count++;
            }
            boxes[i] = count;
            total += count;
            if (j == M)
                break;
        }

        if (total != M)
            System.out.println(-1);
        else {
            result = 0;
            int queue = 0;

            while (total > 0) {
                for (int i = N - 1; i >= 0; i--) {
                    int crane = boxes[i];
                    queue++;
                    if (crane == 0)
                        continue;

                    if (crane >= queue) {
                        total -= queue;

                        boxes[i] -= queue;
                        queue = 0;
                    } else {
                        total -= crane;

                        queue -= crane;
                        boxes[i] = 0;
                    }
                }
                result++;
                queue = 0;
            }
            System.out.println(result);
        }
    }

    static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13)
            System.in.read();

        return n;
    }
}