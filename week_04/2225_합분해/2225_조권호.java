package alg;

import java.util.Scanner;

public class G2225 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[][] nums = new int[K+1][N+1];
		for (int k = 1; k < K+1; k++) {
			for (int n = 0; n < N+1; n++) {
				if(n==0) nums[k][n]=1;
				else {
					nums[k][n] = (nums[k-1][n]+nums[k][n-1])%1_000_000_000;
				}
			}
		}
		System.out.println(nums[K][N]);
	}
}


/*
	0	1	2	3	4	5	6
1	1	1	1	1	1	1	1
2	1	2	3	4	5	6	7
3	1	3	6	10	15	21	28
4	1	4	10	20	35	56	84

[K,N] = [K-1,N]+[K,N-1]
0~N까지 K-1개를 써서 N을 만드는 순열=> 맨끝 숫자가 0인 순열 + 맨끝 숫자가 0이 아닌 순열
끝 숫자가 0이 아닌 순열 중 0~N-1까지 K개 써서 N-1 만드는 순열 전부 =>반복
*/
