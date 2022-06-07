package Bronze;
import java.util.*;

public class Problem1 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        char[][] letters = new char[3][3];

        for (int a = 0; a < 3; a++) {
            String input = scanner.next();
            for (int b = 0; b < input.length(); b++) {
                letters[a][b] = input.charAt(b);
            }
        }

        char[][] cow = new char[3][3];

        for (int a = 0; a < 3; a++) {
            String input = scanner.next();
            for (int b = 0; b < input.length(); b++) {
                cow[a][b] = input.charAt(b);
            }
        }

        boolean[][] already = new boolean[3][3];
        int ans1 = 0;

        for (int a = 0; a < 3; a++) {
            for (int j = 0; j < 3; j++) {
                if (letters[a][j] == cow[a][j]) {
                    already[a][j] = true;
                    ans1++;
                }
            }
        }

        int ans2 = 0;

        for (int x = 0; x < 26; x++) {
            int num = 0;
            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    if (letters[a][b] == (x + 65) && !already[a][b]) {
                        num++;
                    }
                }
            }

            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    if (cow[a][b] == (x + 65) && num > 0 && !already[a][b]) {
                        ans2++;
                        num--;
                    }
                }
            }
        }

        System.out.println(ans1);
        System.out.println(ans2);
    }
}
