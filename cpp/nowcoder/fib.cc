#include <iostream>
#include <time.h>

using namespace std;

unsigned long long climb_normal_rec(unsigned long n) {
    if (n <= 2)
        return n;
    else
        return climb_normal_rec(n - 1) + climb_normal_rec(n - 2);
}

unsigned long long climb_tail_rec(unsigned long n, unsigned long long first, unsigned long long second) {
    if (n == 1)
        return first;
    if (n == 2)
        return second;
    return climb_tail_rec(n - 1, second, first + second);
}

unsigned long long climb_no_rec(unsigned long n) {
    if (n <= 2)
        return n;
    unsigned long long x = 1, y = 1, tmp = 0;
    // n = 3
    // i = 0, 1, 2
    // x, y
    // 1, 1
    // 1, 2
    // 2, 3
    for (unsigned int i = 0; i < n-1; i++) {
        tmp = y;
        y = x + y;
        x = tmp;
    }
    return y;
}

double calc_runtime(clock_t start, clock_t end) {
    return (double)(end - start) / CLOCKS_PER_SEC;
}

int main() {
    unsigned long order = 50;
    unsigned long long fib = 0;

    clock_t start0, end0, start1, end1, start2, end2;

    start0 = clock();
    fib = climb_normal_rec(order);
    end0 = clock();
    cout << order << "-th fibonacci number is " << fib << endl;
    cout << "normal recursion time elapsed: " << calc_runtime(start0, end0) << " seconds!" << endl;

    start1 = clock();
    fib = climb_tail_rec(order, 1, 2);
    end1 = clock();
    cout << order << "-th fibonacci number is " << fib << endl;
    cout << "tail recursion time elapsed: " << calc_runtime(start1, end1)  << " seconds!" << endl;

    start2 = clock();
    fib = climb_no_rec(order);
    end2 = clock();
    cout << order << "-th fibonacci number is " << fib << endl;
    cout << "no recursion time elapsed: " << calc_runtime(start2, end2)  << " seconds!" << endl;
}