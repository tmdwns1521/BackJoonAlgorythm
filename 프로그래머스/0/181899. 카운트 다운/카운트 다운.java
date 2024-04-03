class Solution {
    public int[] solution(int start, int end_num) {
        int[] answer = new int[start - end_num + 1];
        int j = start;
        for (int i = 0; i <= start - end_num; i++ ) {
            answer[i] = j;
            j--;
        }
        return answer;
    }
}