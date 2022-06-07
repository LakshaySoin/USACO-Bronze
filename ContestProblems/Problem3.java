import java.util.*;

public class Problem3 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int t = scanner.nextInt();

		for (int ti = 0; ti < t; ti++) {

			int n = scanner.nextInt();
			int[] cow = new int[n];
			int mi = 1000000000;

			for (int i = 0; i < n; i++) {
				cow[i] = scanner.nextInt();
				mi = Math.min(mi, cow[i]);
			}

			long a = 0;
			int ma = -1000000000;

			while (mi >= 0) {

				for (int i = 1; i < n; i++) {

					if (cow[i] >= mi && cow[i - 1] >= mi) {

						int decrease = Math.min(cow[i] - mi, cow[i - 1] - mi);
						cow[i] -= decrease;
						cow[i - 1] -= decrease;
						a += decrease * 2;
					}
				}

                boolean works = true;
                mi = cow[n - 1];
				ma = cow[n - 1];

				for (int i = 0; i < n - 1; i++) {

					if (cow[i] != cow[i + 1]) {
						works = false;
					}

					ma = Math.max(ma, cow[i]);
					mi = Math.min(mi, cow[i]);
				}

				if (works) {
					break;
				} else {
                    mi -= (ma - mi);
                }

			}
			if (mi > -1) {
				System.out.println(a);
			} else {
				System.out.println(-1);
			}
		}
	}
}