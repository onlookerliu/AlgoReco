import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = {-1, -1};
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer num = nums[i];
            Integer idx = map.get(num);
            if (null == idx) {
                map.put(target - num, i);
            } else {
                if (idx < i) {
                    res[0] = idx;
                    res[1] = i;
                    return res;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] expect = { 0, 1 };
        for (int i : s.twoSum(nums, target))
            System.out.println(i);
        System.out.println();
        System.out.println(Arrays.equals(s.twoSum(nums, target), expect));
    }
}