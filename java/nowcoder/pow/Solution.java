class Solution {
    public double myPowV1(double x, int n) {
        double res = 1.0;
        for (int i = n; i != 0; i /= 2) {
            if (i % 2 != 0)
                res *= x;
            x *= x; // x^2
        }
        return n < 0 ? 1 / res : res;
    }

    public double myPowV2(double x, int n) {
        if (n == 0)
            return (double) 1;

        if (n == 1)
            return x;
        else if (n == -1)
            return 1 / x;
        
        if (n % 2 == 1) {
            double r = myPowV2(x, n / 2);
            return r * r * (n > 0 ? x : 1 / x);
        } else {
            double r = myPowV2(x, n / 2);
            return r * r;
        }

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        var start = System.currentTimeMillis();
        System.out.println(s.myPowV2(2.0, 4) == 16.0);
        System.out.println(s.myPowV2(3.0, 2) == 9.0);
        System.out.println(s.myPowV2(2.0, 5) == 32.0);
        System.out.println(s.myPowV2(0.0, 0) == 1.0);
        System.out.println(s.myPowV2(0.0, 123456) == 0.0);
        var end = System.currentTimeMillis();
        System.out.println("Time elapsed: " + (end - start) / 1000 + "seconds!");
    }
}