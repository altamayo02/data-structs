TEST = range(10, 15)
for m in TEST:
    for n in range(1, m):
        if m < n: continue
        if (m % 2 + n % 2) % 2 == 0: print("->", end=" ")
        print(f"{m}, {n}: {m ** 2 - n ** 2}, {2 * m * n}, {m ** 2 + n ** 2}")
