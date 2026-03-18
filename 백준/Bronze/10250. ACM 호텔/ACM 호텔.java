import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Testcase수 입력받기
        int T = Integer.parseInt(br.readLine());

        // 마지막 결과 저장할 배열 
        int[] result = new int[T];


        for (int i=0;i<T;i++){

            StringTokenizer st = new StringTokenizer(br.readLine());

            
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            int room = (N/H) + 1;
            int floor = (N%H);

            // 딱 맞아떨어질 떄 , 최고층일 떄 
            if (floor==0){
                floor=H;
                room=N/H;

            }
            
            result[i]=(floor*100)+room;

        }

        for(int i=0;i<T;i++){
            System.out.println(result[i]);
        }
    }
}