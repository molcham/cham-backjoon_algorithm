import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
         
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // testcase 갯수 입력 받기
        int T = Integer.parseInt(br.readLine());

        for(int i=0;i<T;i++){

            String[] strArr = br.readLine().split(" ");

            int a = Integer.parseInt(strArr[0]);
            String str = strArr[1]; 

            char[] chars = str.toCharArray();

            StringBuilder sb = new StringBuilder();
            for(char c : chars){
                sb.append(String.valueOf(c).repeat(a));
            }
            System.out.println(sb); 

        }
    }
}