import java.util.*;

class Solution {
    public int solution(int n) {
        
        int s = (int)Math.sqrt(n);
        
        // 약수를 담을 배열 생성
        ArrayList<Integer> list = new ArrayList<>();
        
        // 0은 필요없음 약수니까
        for (int i=1;i<=s;i++){
            if(n%i == 0){
                list.add(i);
                if(n/i != i){
                    // 제곱수가 아니라면 몫도 저장해준다.
                    list.add(n/i);
                }
            }
            
        }
        
        
        int answer = 0;
        for (int a:list){
            answer=answer+a;            
        }
        

        return answer;
    }
}