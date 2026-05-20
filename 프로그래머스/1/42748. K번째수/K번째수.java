// int[] sliced = Arrays.copyOfRange(array, 1, 5);
// commands는 2차원 배열 ! 
import java.util.*;

class Solution {
    // int형 베열을 반환하는 메서드 solution
    public int[] solution(int[] array, int[][] commands) {
        
        // for문에서 결과값 넣을 배열 생성
        int[] answer = new int[commands.length];
        
        
        for(int i = 0;i<commands.length;i++){
            
           int[] sliced = Arrays.copyOfRange(array,commands[i][0] - 1 ,commands[i][1]);
            
        
        Arrays.sort(sliced);
        
        // answer[i]에 담을 값
        answer[i] = sliced[commands[i][2] - 1];
        }
        
        return answer;
    }
}