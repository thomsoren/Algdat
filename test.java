class Solution {
    public int solution(int[] A) {
        // Implement your solution here
        int n = 1;
        for (int i = 1; i < 100000; i++) {
            if (!contains(A, i)) {
                n = i;
                break;
            }
        }
        return n;


    }

    public boolean contains(int[] A, int val) {
        for (int i = 0; i < A.length; i++) {
            if (A[i] == val) {
                return true;
            }
        }
        return false;
    }
}

