import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 단어 받기 
        String str = br.readLine().trim();
        int n = 0;


        if(!str.isEmpty()){
            n = str.split(" ").length;
        }

    
        //문자열이 공백으로 시작하거나 끝날 때


        System.out.print(n);
    }
}