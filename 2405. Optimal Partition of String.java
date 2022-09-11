class Solution {
    public boolean isStrictlyPalindromic(int n) {
        for (int i = 2; i < n; i++) {
            String test = (Integer.toString(Integer.parseInt(
                Integer.toString(n), 10), i));

            String rev = "";
            for (int j = test.length() - 1; j >= 0; j--) {
                rev = rev + test.charAt(j);
            }
            if (!test.equals(rev)) {
                return(false);
            }

        }
        return(true);
    }
}
