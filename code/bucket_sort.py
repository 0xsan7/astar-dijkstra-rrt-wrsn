from __future__ import annotations
import random
import sys
from typing import List, Tuple


class OpCounter:
    def __init__(self) -> None:
        self.placements = 0
        self.comparisons = 0
        self.shifts = 0
        self.merges = 0

    def total(self) -> int:
        return self.placements + self.comparisons + self.shifts + self.merges

    def __repr__(self) -> str:  # concise summary
        return (
            f"placements={self.placements}, comparisons={self.comparisons}, "
            f"shifts={self.shifts}, merges={self.merges}, total={self.total()}"
        )


def insertion_sort_counted(arr: List[int], counter: OpCounter) -> List[int]:
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # compare a[j] and key repeatedly
        while j >= 0:
            counter.comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                counter.shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        counter.shifts += 1  # insertion assignment
    return a


def bucket_sort_counted(arr: List[int], num_buckets: int, rng_min: int, rng_max: int) -> Tuple[List[int], List[List[int]], OpCounter]:
    counter = OpCounter()
    # initialize buckets
    buckets: List[List[int]] = [[] for _ in range(num_buckets)]

    span = rng_max - rng_min + 1
    for v in arr:
        # map value to bucket index in [0, num_buckets-1]
        idx = (v - rng_min) * num_buckets // span
        if idx >= num_buckets:
            idx = num_buckets - 1
        buckets[idx].append(v)
        counter.placements += 1

    # record buckets before sorting (for printing)
    buckets_before = [b.copy() for b in buckets]

    # sort each bucket with insertion sort and count ops
    for i in range(len(buckets)):
        if buckets[i]:
            buckets[i] = insertion_sort_counted(buckets[i], counter)

    # merge buckets
    output: List[int] = []
    for b in buckets:
        for v in b:
            output.append(v)
            counter.merges += 1

    return output, buckets_before, counter


def run_demo(seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)

    N = 100
    MIN_V = 1
    MAX_V = 1000

    data = [random.randint(MIN_V, MAX_V) for _ in range(N)]

    print("Original list:")
    print(data)
    print()

    for num_buckets in (100, 10):
        sorted_arr, buckets_before, counter = bucket_sort_counted(data, num_buckets, MIN_V, MAX_V)

        print(f"--- Bucket Sort with {num_buckets} buckets ---")
        print(f"Buckets (before sorting) -- {len(buckets_before)} buckets:")
        for i, b in enumerate(buckets_before):
            print(f"  Bucket {i}: {b}")
        print()

        print("Buckets (after insertion sort):")
        # to avoid extremely long output for 100 buckets, compress empty buckets
        for i, b in enumerate(buckets_before):
            pass
        # print actual sorted buckets (matching indices)
        _, buckets_before2, _ = bucket_sort_counted(data, num_buckets, MIN_V, MAX_V)
        # sort those buckets for display
        display_buckets = []
        for b in buckets_before2:
            display_buckets.append(sorted(b))

        for i, b in enumerate(display_buckets):
            print(f"  Bucket {i}: {b}")

        print()
        print(f"Sorted list (merged):")
        print(sorted_arr)
        print()
        print(f"Operation counts: {counter}")
        print()


if __name__ == "__main__":
    seed = None
    if len(sys.argv) > 1:
        try:
            seed = int(sys.argv[1])
        except ValueError:
            seed = None
    run_demo(seed)
