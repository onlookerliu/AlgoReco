from typing import List


class Solution:
    def resolve(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        :param nums:
        :param target:
        :return:

        Example:
        --------
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        """
        hash = {}
        for i, num in enumerate(nums):
            # hash[target - num] = i
            if hash.get(num) is None:
                hash[target - num] = i
            else:
                index = hash[num]
                if index < i:
                    return [index, i]

        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.resolve(nums, target)
    print(res)
