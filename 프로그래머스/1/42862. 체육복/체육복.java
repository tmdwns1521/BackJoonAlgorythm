import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] clothes = new int[n];
        Arrays.fill(clothes, 1);
        for (int l : lost) {
            clothes[l - 1]--;
        }
        for (int r : reserve) {
            clothes[r - 1]++;
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (clothes[i] == 0) {
                if (0 < i && clothes[i - 1] == 2) {
                    clothes[i]++;
                    clothes[i - 1]--;
                } else if (i < n - 1 && clothes[i + 1] == 2) {
                    clothes[i]++;
                    clothes[i + 1]--;
                }
            }
            if (clothes[i] > 0) {
                answer++;
            }
        }
        return answer;
    }
}