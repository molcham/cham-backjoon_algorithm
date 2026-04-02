import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strArr = new String[10];
        // 입력 10개 한줄씩
        for(int i=0;i<10;i++){
            strArr[i] = br.readLine();

        }
        int[] num = new int[strArr.length];
        int[] resultNum = new int[strArr.length];

        for(int i = 0; i < strArr.length; i++){
            num[i] = Integer.parseInt(strArr[i]);
        }
        for(int i=0;i<num.length;i++){
            resultNum[i]=num[i]%42;
            //System.out.println("resultNum["+i+"]: " + resultNum[i]);  // 추가
        }

        // 이 부분부터 몰라서 찾아봄
        Arrays.sort(resultNum);
        int count = 1;  // 첫 번째 값은 무조건 카운트!! (중요)

        for(int i = 1; i < resultNum.length; i++){
            // i는 1부터!! 0부터 하면 [i-1]에서 오류남
            if(resultNum[i] != resultNum[i-1]){  
                count++;
            }
        }

        System.out.println(count);
    }
}