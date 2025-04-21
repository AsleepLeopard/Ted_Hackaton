import itertools
from functools import reduce

def alternating_sum(seq: list[int]):
    return sum(seq[::2]) - sum(seq[1::2])

def non_empty_subsequence(seq: list[int], k: int, limit: int):
    max_product = -1
    for r in range(1, len(seq)+1):
        combs = itertools.combinations(seq, r)
        for comb in combs:
            if alternating_sum(list(comb)) == k:
                product = reduce(lambda x, y: x * y, comb)
                if limit >= product > max_product:
                    max_product = product
    return max_product

if __name__ == "__main__":
    seq = [2, 2, 3, 3]
    print(non_empty_subsequence(seq, k=0, limit=9))
