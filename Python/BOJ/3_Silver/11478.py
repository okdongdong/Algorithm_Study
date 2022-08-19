S = input()
N = len(S)
subset = set()

for length in range(1, N+1):
    for start_idx in range(N-length+1):
        end_idx = start_idx+length
        subset.add(S[start_idx:end_idx])

print(len(subset))
