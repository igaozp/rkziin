from functools import lru_cache
from typing import Dict
from typing import Generator


def fib(n: int) -> int:
    # base case
    if n < 2:
        return n
    # recursive
    return fib(n - 1) + fib(n - 2)


memo: Dict[int, int] = {0: 0, 1: 1}


def fib_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def sample_fib_memo(n: int) -> int:
    if n < 2:
        return n
    return sample_fib_memo(n - 2) + sample_fib_memo(n - 1)


def iter_fib(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    nex: int = 1
    for _ in range(1, n):
        last, nex = nex, last + nex
    return nex


def yield_fib(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1

    last: int = 0
    nex: int = 1
    for _ in range(1, n):
        last, nex = nex, last + nex
        yield nex


if __name__ == '__main__':
    print(fib(5))
    print(fib(10))

    print(fib_memo(5))
    print(fib_memo(50))

    print(sample_fib_memo(5))
    print(sample_fib_memo(50))

    print(iter_fib(5))
    print(iter_fib(50))

    for i in yield_fib(50):
        print(i)
