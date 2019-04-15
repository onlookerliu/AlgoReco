from ..nowcoder.pow import Solution

import unittest
# from unittest import TestCase


class TestPow(unittest.TestCase):
    def test_resolve(self):
        s = Solution()

        self.assertEqual(s.resolve(2, 2), 4.0)

        self.assertTrue(s.resolve(2, 3) == 8)

        self.assertEqual(s.resolve(0, 0), 1)
        self.assertEqual(s.resolve(2.0, -1), 0.5)

        self.assertEqual(s.resolve(2, 2), 4)

        self.assertEqual(s.resolve(3, 2), 9)
        # self.assertEqual(s.resolve_v1(2.10000, 3), 9.26100)
        # self.assertEqual(s.resolve_v1(2.00000, 10), 1024.00000)

        del s

    # def test_resolve_v2(self):
    #     s = Solution()
    #
    #     self.assertEqual(s.resolve_v2(2, 2), 4.0)
    #
    #     self.assertTrue(s.resolve_v2(2, 3) == 8)
    #
    #     self.assertEqual(s.resolve_v2(0, 0), 1)
    #     self.assertEqual(s.resolve_v2(2.0, -1), 0.5)
    #
    #     self.assertEqual(s.resolve_v2(2, 2), 4)
    #
    #     self.assertEqual(s.resolve_v2(3, 2), 9)
    #     self.assertEqual(s.resolve_v2(2.10000, 3), 9.26100)
    #     self.assertEqual(s.resolve_v2(2.00000, 10), 1024.00000)

    # def test_resolve_v3(self):
    #     s = Solution()
    #
    #     self.assertEqual(s.resolve_v3(2, 2), 4.0)
    #
    #     self.assertTrue(s.resolve_v3(2, 3) == 8)
    #
    #     self.assertEqual(s.resolve_v3(0, 0), 1)
    #     self.assertEqual(s.resolve_v3(2.0, -1), 0.5)
    #
    #     self.assertEqual(s.resolve_v3(2, 2), 4)
    #
    #     self.assertEqual(s.resolve_v3(3, 2), 9)
    #     self.assertEqual(s.resolve_v3(2.10000, 3), 9.26100)
    #     self.assertEqual(s.resolve_v3(2.00000, 10), 1024.00000)

    # def test_resolve_v4(self):
    #     s = Solution()
    #
    #     self.assertEqual(s.resolve_v4(2, 2), 4.0)
    #
    #     self.assertTrue(s.resolve_v4(2, 3) == 8)
    #
    #     self.assertEqual(s.resolve_v4(0, 0), 1)
    #     self.assertEqual(s.resolve_v4(2.0, -1), 0.5)
    #
    #     self.assertEqual(s.resolve_v4(2, 2), 4)
    #
    #     self.assertEqual(s.resolve_v4(3, 2), 9)
    #     self.assertEqual(s.resolve_v4(2.10000, 3), 9.26100)
    #     self.assertEqual(s.resolve_v4(2.00000, 10), 1024.00000)

    def test_resolve_v5(self):
        s = Solution()

        self.assertEqual(s.resolve_v5(2, 2), 4.0)

        self.assertTrue(s.resolve_v5(2, 3) == 8)

        self.assertEqual(s.resolve_v5(0, 0), 1)
        self.assertEqual(s.resolve_v5(2.0, -1), 0.5)

        self.assertEqual(s.resolve_v5(2, 2), 4)

        self.assertEqual(s.resolve_v5(3, 2), 9)
        # self.assertEqual(s.resolve_v5(2.10000, 3), 9.26100)
        self.assertEqual(s.resolve_v5(2.00000, 10), 1024.00000)

        del s


if __name__ == '__main__':
    unittest.main()