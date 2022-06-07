package Bronze;
import java.util.*;

public class Problem2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();

        for (int ti = 0; ti < t; ti++) {

            int[] a = new int[4];
            int[] b = new int[4];

            for (int i = 0; i < 4; i++) {
                int k = scanner.nextInt();
                a[i] = k;
            }

            for (int i = 0; i < 4; i++) {
                int k = scanner.nextInt();
                b[i] = k;
            }

            int[] c = new int[4];
            boolean works = false;
            for (int z = 1; z <= 10; z++) {

                for (int y = 1; y <= 10; y++) {

                    for (int x = 1; x <= 10; x++) {

                        for (int w = 1; w <= 10; w++) {

                            c[0] = z; c[1] = y; c[2] = x; c[3] = w;

                            if ((winner(b, c) && winner(c, a) && winner(a, b)) || (winner(b, a) && winner(a, c) && winner(c, b))) {
                                works = true;
                            }

                        }
                    }
                }
            }

            if (works == true) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }

        }
    }
    public static boolean winner(int[] thing1, int[] thing2) {
        int a1 = 0;
        int a2 = 0;

        for (int a = 0; a < 4; a++) {

            for (int b = 0; b < 4; b++) {

                if (thing1[a] > thing2[b]) {
                    a1++;
                } else if (thing1[a] < thing2[b]) {
                    a2++;
                }

            }
        }

        if (a1 > a2) {
            return true;
        } else {
            return false;
        }
        
    }
}
