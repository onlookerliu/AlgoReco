# 一只青蛙可以跳上1级台阶，也可以跳上2级台阶，问它跳上n级台阶总共有多少种方法


class Solution:
    def resolve_v1(self, n):
        """
        Ways of climb n stairs
        
        ------
        n : Int
            count of stairs
        ------
        """
        # 动态规划状态转移方程
        # resolve_v1(n-1), resolve_v1(n-2) -> resolve_v1(n)
        if n <= 0 or not isinstance(n, int):
            raise AssertionError("n should be a non-negative integer!")
        if n <= 2:
            return n
        return self.resolve_v1(n - 1) + self.resolve_v1(n - 2)

    def resolve_v2(self, n):
        x0, x1 = 1, 1
        for i in range(n):
            x0, x1 = x1, x0 + x1  # 1, 2 -> 2, 3 -> 3, 5
        return x0

    def resolve_v3(self, n):
        # 尾递归版本
        # util(5, 1, 2) -> util(4, 2, 3) -> util(3, 3, 5) -> util(2, 5, 8) -> 8
        # fib(5) = fib(4) + fib(3) = fib(3) + fib(2) + fib(2) + fib(1) = 1 + 2 + 2 + 3
        def util(n, first, second):
            if n == 1:
                return first
            elif n == 2:
                return second
            else:
                return util(n-1, second, first + second)

        return util(n, 1, 2)

    def resolve_v4(self, n):
        # 记忆化（缓存）
        def memoized(fun):
            lookup = {}
            def wrapped(n):
                if lookup.get(n) is not None:
                    return lookup[n]
                else:
                    # 尽量节省fun函数运算的次数
                    # 例如fib(5) = fib(3) + fib(4) = fib(3) + fib(3) + fib(2)
                    res = fun(n)
                    lookup[n] = res
                    return res
            return wrapped

        # 装饰器写法
        @memoized
        def fib(n):
            if n == 1 or n == 2:
                return n
            return fib(n - 1) + fib(n - 2)

        return fib(n)
        # return memoized(fib)(n)

