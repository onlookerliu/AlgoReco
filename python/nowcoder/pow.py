# 求解数值x的整数(n)次方


class Solution:
    def resolve(self, x: float, n: int) -> float:
        """
        Calculate the power of base, i.e. x ** n


        -----
        Note:
            n is a 32-bit signed integer, within the range [−231, 231 − 1]
            -100.0 < x < 100.0
        -----
        Example:
            >>> pow(2.00000, -2)
            >>> 0.25000
            >>> pow(2.10000, 3)
            >>> 9.26100
            >>> pow(2.00000, 10)
            >>> 1024.00000
        -----
        :param x: base
        :param n: power
        :return: x ^ n
        """
        return x ** n

    def resolve_v2(self, x: float, n: int) -> float:

        # if int(x) == 2:
        #     return float(1 << n)
        if n == 0:
            return 1
        if n == 1:
            return x
        res = self.resolve_v2(x, n // 2)
        if n % 2 == 0:
            return res * res
        else:
            return x * res * res

    def resolve_v3(self, x: float, n: int) -> float:
        return x * self.resolve_v3(x, n >> 1) * self.resolve_v3(x, n >> 1) if n % 2 else self.resolve_v3(x, n >> 1) * self.resolve_v3(x, n >> 1)

    def resolve_v4(self, x: float, n: int) -> float:
        def resolve_util(x, n, acc):
            assert n >= 0, "这里的n已经默认大于0"
            if n == 0:
                return acc
            return resolve_util(x, n - 1, x * acc)

        # resolve_util(2, 4, 1) == resolve_util(2, 3, 2*1)
        # == resolve_util(2, 2, 2*2*1) == resolve_util(2, 1, 2*2*2*1)
        # == resolve_util(2, 0, 2*2*2*2*1) == 16

        return resolve_util(x, n, 1) if n >= 0 else 1 / resolve_util(x, -n, 1)

    def resolve_v5(self, x: float, n: int) -> float:
        acc = x
        sign = 1 if n > 0 else -1
        n = n if n > 0 else -n
        while n > 1:
            acc = acc * x
            n = n - 1
        return acc if sign == 1 else 1 / acc


    def resolve_v6(self, x: float, n: int) -> float:
        acc = 1
        if n % 2:
            while n:
                acc = acc * x * x
                n = n // 2
            return acc * x
        else:
            while n:
                acc = acc * x * x
                n = n // 2
            return acc

    def resolve_v7(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        sign = 1 if n > 0 else -1
        n = n if n > 0 else -n
        res = [1.0] * (n + 1)
        # res[i] == x^i
        for i in range(1, n+1):
            res[i] = res[i-1] * x
        return res[n] if sign == 1 else 1 / res[n]


if __name__ == '__main__':
    s = Solution()
    print(s.resolve_v7(2.00000, 10))
    print(s.resolve_v7(2.00000, 10) == 1024.0000)
    del s