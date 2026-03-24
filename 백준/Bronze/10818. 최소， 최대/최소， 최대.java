//package 손채민;
import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 몇개 정수 받을 건지 n 
        int n = Integer.parseInt(br.readLine());
        String[] strArr = br.readLine().split(" ");

        int[] result = new int[strArr.length];

        // int형으로 변환 
        for (int i = 0; i < strArr.length; i++) {
            result[i] = Integer.parseInt(strArr[i]);
        }

        int max = result[0];
        int min = result[0];

        for (int num : result){
            max = Math.max(max, num);
            min = Math.min(min, num);
        }

    
    //줄바꿈 없음
    System.out.print(min);
    System.out.print(" ");
    System.out.print(max);


        
    }
}