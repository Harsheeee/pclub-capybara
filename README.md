# Capybara Patrol
Pclub secy recruitment task by Harshit Tripathi -- 240443

## Problem: Capybara's Cells
Capy, the adventurous capybara, digs a straight tunnel made of $n$ consecutive burrow-cells.

In every cell $i$ ($1 \le i \le n$), he drops a shiny pebble whose value is $A_i$ ($0 \le A_i \le 10^9$).
Capy loves harmonics. He calls a contiguous segment of the burrow harmonic when:

**max value in the segment - min value in the segment = (length of the segment) - 1**

Now Capy gives you $q$ questions.  
Each question is one cell $k$ ($1 \le k \le n$).

For that cell, print:

- the length of the shortest harmonic segment that contains cell $k$;

- or $-1$ if cell $k$ is not contained in any harmonic segment at all.

### Input
The first line of input contains two integers $n$ $(1\le n\le 2\times10^5)$ --- number of cells and $q$ $(1\le q\le 2\times10^5)$ --- number of questions.

The second line contains $n$ integers $A_1,A_2,…,A_n$ $(0\le A_i \le 10^5)$ --- value of pebble in cell $i$.

Next $q$ lines contains $k_i$ $(1\le k_i\le n)$ --- cell queried in the $i_{th}$ question.

### Output
Print $q$ lines.

For each question output a single integer --- the shortest length of a harmonic segment containing cell $k_i$, or $-1$ if no such segment exists.
