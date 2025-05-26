import random
import os

# Create input directory if it doesn't exist
os.makedirs("input", exist_ok=True)

# Number of test cases per subtask
cases_per_subtask = 5

# Subtask 1: Strictly increasing array
for t in range(1, cases_per_subtask + 1):
    N = random.randint(1, 10**5)
    A = []
    current = 1
    for _ in range(N):
        increment = 1
        current += increment
        A.append(current)
    with open(f"input/1-{t:02d}.in", "w") as f:
        f.write(f"{N}\n")
        f.write(" ".join(map(str, A)) + "\n")

# Subtask 2: 1 <= N <= 1000
for t in range(1, cases_per_subtask + 1):
    N = random.randint(500, 1000)
    A = [random.randint(1, 10**9) for _ in range(N)]
    with open(f"input/2-{t:02d}.in", "w") as f:
        f.write(f"{N}\n")
        f.write(" ".join(map(str, A)) + "\n")

# Subtask 3: No restrictions
for t in range(1, cases_per_subtask + 1):
    N = random.randint(1, 10**5)
    A = [random.randint(1, 10**9) for _ in range(N)]
    with open(f"input/3-{t:02d}.in", "w") as f:
        f.write(f"{N}\n")
        f.write(" ".join(map(str, A)) + "\n")

