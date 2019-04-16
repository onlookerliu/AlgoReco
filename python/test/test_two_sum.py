import unittest

from python.leetcode.two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def test_resolve(self):
        s = Solution()
        self.assertEqual(s.resolve([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(s.resolve([2, 7, 11, 15], 13), [0, 2])
        self.assertEqual(s.resolve([2, 7, 7, 11, 15], 9), [0, 1])
        self.assertEqual(s.resolve([2, 7, 7, 11, 15], 14), [1, 2])


if __name__ == '__main__':
    unittest.main()
