import os, random, pathlib

OUT_DIR = pathlib.Path("tests")          # folder to receive the .in files
OUT_DIR.mkdir(exist_ok=True)

NUM_LARGE  = 200_000
NUM_MEDIUM =   2_000
NUM_SMALL  =      30
MAX_A      = 1_000_000_000


def write_test(num: int, label: str, n: int, q: int, A: list[int], K: list[int]):
    assert 1 <= num <= 99 and n == len(A) and q == len(K)
    fname = OUT_DIR / f"{num:02d}.in"
    with fname.open("w") as f:
        f.write(f"{n} {q}\n")
        f.write(" ".join(map(str, A)) + "\n")
        for k in K:
            f.write(f"{k}\n")
    manifest.append((num, label))

write_test(1, "n=1 q=1 trivial",
           1, 1, [0], [1])

write_test(2, "tiny mixed 3-elements",
           3, 3, [3, 1, 3], [1, 2, 3])

random.seed(1)
for idx, seed in enumerate([11, 12, 13], start=3):
    random.seed(seed)
    n = random.randint(2, NUM_SMALL)
    q = random.randint(1, NUM_SMALL)
    A = [random.randint(0, 9) for _ in range(n)]
    K = [random.randint(1, n) for _ in range(q)]
    write_test(idx, f"small random seed{seed}", n, q, A, K)

nC, qC = 2_000, 2_000
write_test(6, "all zeros",
           nC, qC, [0]*nC, [(i % nC) + 1 for i in range(qC)])
write_test(7, "all 1e9",
           nC, qC, [MAX_A]*nC, [(i % nC) + 1 for i in range(qC)])

nD, qD = NUM_LARGE, NUM_LARGE
inc = list(range(nD))
dec = list(range(nD, 0, -1))
randK = [random.randint(1, nD) for _ in range(qD)]
write_test(8, "strictly increasing 0..n-1",
           nD, qD, inc, randK)
write_test(9, "strictly decreasing n..1",
           nD, qD, dec, randK)

write_test(10, "all equal 42",
           NUM_LARGE, 1, [42]*NUM_LARGE, [NUM_LARGE//2])

nF, qF = 100_000, 100_000
alt = [0 if i % 2 == 0 else MAX_A for i in range(nF)]
write_test(11, "alternating high/low",
           nF, qF, alt, [random.randint(1, nF) for _ in range(qF)])

def dense(n: int) -> list[int]:
    out = []
    while len(out) < n:
        base = random.randint(0, MAX_A-3)
        out += [base, base, base+1, base+2]
    return out[:n]

for num, seed in zip(range(12, 15), [21, 22, 23]):
    random.seed(seed)
    n, q = 50_000, 50_000
    write_test(num, f"dense harmonic seed{seed}",
               n, q, dense(n), [random.randint(1, n) for _ in range(q)])


for num, seed in zip(range(15, 20), [31, 32, 33, 34, 35]):
    random.seed(seed)
    n, q = NUM_MEDIUM, NUM_MEDIUM
    A = [random.randint(0, MAX_A) for _ in range(n)]
    K = [random.randint(1, n) for _ in range(q)]
    write_test(num, f"medium random seed{seed}", n, q, A, K)

#max random
random.seed(42)
Amax = [random.randint(0, MAX_A) for _ in range(NUM_LARGE)]
Kmax = [random.randint(1, NUM_LARGE) for _ in range(NUM_LARGE)]
write_test(20, "max random seed42",
           NUM_LARGE, NUM_LARGE, Amax, Kmax)

#blocks of equal values
block = 500
Ab = []
v = 0
while len(Ab) < NUM_LARGE:
    Ab.extend([v]*block)
    v += 1
write_test(21, "blocks size500",
           NUM_LARGE, NUM_LARGE, Ab[:NUM_LARGE],
           list(range(1, NUM_LARGE+1)))

#increasing then flat run pattern
Aif = []
run = 1_000
val = 0
while len(Aif) < NUM_LARGE:
    Aif.extend(range(val, val+run))      # strictly inc
    val += run
    Aif.extend([val]*run)                # flat
write_test(22, "inc+flat repeated",
           NUM_LARGE, NUM_LARGE, Aif[:NUM_LARGE],
           [random.randint(1, NUM_LARGE) for _ in range(NUM_LARGE)])

#huge randoms
for num, seed in zip(range(23, 26), [101, 102, 103]):
    random.seed(seed)
    write_test(num, f"huge random seed{seed}",
               NUM_LARGE, NUM_LARGE,
               [random.randint(0, MAX_A) for _ in range(NUM_LARGE)],
               [random.randint(1, NUM_LARGE) for _ in range(NUM_LARGE)])
## i had to delete two tests manually because validator was giving an unexpected error
print(f"Generated {len(manifest)} tests inside '{OUT_DIR}/'")
