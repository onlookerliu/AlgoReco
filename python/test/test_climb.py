import unittest
from python.nowcoder.climb import Solution

class TestClimb(unittest.TestCase):
    def test_resolve_v1(self):
        s = Solution()
        self.assertEqual(s.resolve_v1(1), 1)
        self.assertEqual(s.resolve_v1(2), 2)
        self.assertEqual(s.resolve_v1(3), 3)
        self.assertEqual(s.resolve_v1(4), 5)

    def test_resolve_v2(self):
        s = Solution()
        self.assertEqual(s.resolve_v2(1), 1)
        self.assertEqual(s.resolve_v2(2), 2)
        self.assertEqual(s.resolve_v2(3), 3)
        self.assertEqual(s.resolve_v2(4), 5)

    def test_resolve_v3(self):
        s = Solution()
        self.assertEqual(s.resolve_v3(1), 1)
        self.assertEqual(s.resolve_v3(2), 2)
        self.assertEqual(s.resolve_v3(3), 3)
        self.assertEqual(s.resolve_v3(4), 5)

    def test_resolve_v4(self):

        s = Solution()
        self.assertEqual(s.resolve_v4(1), 1)
        self.assertEqual(s.resolve_v4(2), 2)
        self.assertEqual(s.resolve_v4(3), 3)
        self.assertEqual(s.resolve_v4(4), 5)


if __name__ == '__main__':
    unittest.main()
