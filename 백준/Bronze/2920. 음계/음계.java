import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        // 앞 - 뒤 했을때 모든 숫자의 차가 1이면 des
        // 앞 - 뒤 했을때 모든 숫자의 차가 -1이면 asc

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 저장할 Stirng형 배열 선언 
        String[] strArr = br.readLine().split(" ");
        int[] num = new int[strArr.length];
        int result=0;

        for(int i = 0; i < strArr.length; i++){
            num[i] = Integer.parseInt(strArr[i]);
        }
        

        for (int i=0;i<num.length-1;i++){

            if(num[i]-num[i+1]==1){
                result++;
            }
            else if(num[i]-num[i+1]==(-1)){
                result--;
            }
            else{
                result += 0;
            }
            //System.out.println(result);
        }
        if(result == 7){
            System.out.println("descending");
        }
        else if(result == (-7)){
            System.out.println("ascending");
        }
        else{
            System.out.println("mixed");
        }
   
    }
}