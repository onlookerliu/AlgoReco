import timeit

from python.nowcoder.climb import Solution


if __name__ == '__main__':
    s = Solution()

    start_v1 = timeit.default_timer()
    res_v1 = s.resolve_v1(35)
    end_v1 = timeit.default_timer()
    print("Got result {}, time elapsed {} seconds!".format(res_v1, end_v1 - start_v1))

    start_v3 = timeit.default_timer()
    res_v3 = s.resolve_v3(35)
    end_v3 = timeit.default_timer()
    print("Got result {}, time elapsed {} seconds!".format(res_v3, end_v3 - start_v3))