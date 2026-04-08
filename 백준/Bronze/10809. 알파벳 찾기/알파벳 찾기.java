import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 문자열 입력 받기
        String s = br.readLine();
        
        // 문자열 => charAt으로 변환

        /* 
        if :a ~ z 까지 체크 하면서 문자열의 몇번째 인덱스에 있는지 반환(문자열 메서드)
        else : 없으면 -1 출력
        */
        for (char ch = 'a'; ch <= 'z'; ch++){
            int idx = s.indexOf(ch);
            System.out.print(idx);
            System.out.print(" ");
        }
        
        
    }
}