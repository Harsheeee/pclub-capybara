# Problem: Capybara's Cells
You're given an array A of length n. A subarray [L..R] is harmonic if:

**$$max(A[L..R]) - min(A[L..R]) == (R - L)$$**

Each query gives you a position $k$, and your task is to find the length of the shortest harmonic subarray that contains position $k$, or $-1$ if no such subarray exists.

## Observation
A harmonic segment is such that the difference between the maximum and minimum values equals the length minus 1. This condition essentially ensures that the elements are consecutive integers in some order.

    Example: [2, 1, 3] → max=3, min=1, length=3 → 3-1 == 2, so it's harmonic.

We are not checking if the numbers are actually all distinct or continuous in value explicitly, because if ```max - min == length - 1``` and all values are distinct, the segment must be a permutation of consecutive integers.

For each index $i$, we need to find the shortest such harmonic segment that contains it.

## Brute Force
Try every subarray [L..R] and check:
- ```max-min= R-L```

### Time Complexity
O(n<sup>2</sup>) because of the two nested loops. This would give TLE for large values of $n$.

## Optimized Solution -- Sliding Window + Deques
To check all harmonic subarrays efficiently, we can use a sliding window technique with two monotonic deques:
- One deque (```maxQ```) to track the maximum in the current window.
- One deque (```minQ```) to track the minimum.

Steps:
1. Initialize two deques: ```maxQ```, ```minQ```, and two pointers ```L``` and ```R``` for the window.
2. Expand the window by increasing ```R```:
   - Update ```maxQ``` and ```minQ``` to maintain max/min in the window.

3. If ```max - min > R - L```, shrink the window from the left (```L++```) to restore the harmonic condition.
4. If at any point, ```max - min == R - L```, this window is harmonic. Record the length for all indices within this window if it’s smaller than previously found lengths.
5. Repeat for the whole array.
6. Query Handling:
   
   After precomputing the best (shortest) harmonic segment length for every index, we can answer each query in O(1) by looking up the value.
### Time Complexity
O(n+q)
- O(n) for sliding window
- O(q) for queries
## Why this works
- We process all valid harmonic segments exactly once and update the shortest one for each index it covers.
- The use of deques ensures we always get the current window's min and max in O(1), keeping the whole algorithm efficient.
