# Problem: Capybara's Cells
You're given an array A of length n. A subarray [L..R] is harmonic if:

**$$max(A[L..R]) - min(A[L..R]) == (R - L)$$**

Each query gives you a position $k$, and your task is to find the length of the shortest harmonic subarray that contains position $k$, or $-1$ if no such subarray exists.

## Brute Force (TLE)
Try every subarray [L..R] and check:
