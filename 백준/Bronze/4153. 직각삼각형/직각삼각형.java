import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0 && b == 0 && c == 0) {
                break;
            }

            int max = Math.max(a, Math.max(b, c));
            int check;

            if (max == a) {
                check = b * b + c * c;
            } else if (max == b) {
                check = a * a + c * c;
            } else {
                check = a * a + b * b;
            }

            if (check == max * max) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}
