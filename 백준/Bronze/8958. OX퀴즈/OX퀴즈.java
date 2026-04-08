import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 테스트 케이스 받기
        int t = Integer.parseInt(br.readLine());

        for (int i=0;i<t;i++){
            String s = br.readLine();
            int score=0;
            int sum=0;
            for (int j=0;j<s.length();j++){
            
                char ch = s.charAt(j);
                if(ch=='O'){
                    score++;
                    sum=sum+score;
                }
                else{
                    score=0;
                    sum=sum+score;
                }
            }
        
        System.out.println(sum);
            
        }
    }

}