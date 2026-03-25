import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        // 1. 문자열로 바꾸기 
        String str = String.valueOf(A*B*C);

        // 2. 숫자 갯수 저장할 배열 
        int[] count = new int[10];

        // 3. 문자열 메서드 이용하여 각 자리 숫자 파악
        for (char c: str.toCharArray()){
            count[Character.getNumericValue(c)]++;
        }

        // 4. 결과 출력 0부터 9 각 갯수
        for(int i=0;i<10;i++){
            System.out.println(count[i]);
        }
    }
}