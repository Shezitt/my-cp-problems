import os
import random

def generate_testcase(subtask, test_num, N, Ai_min, Ai_max, K, sorted_array=False):
    os.makedirs("input", exist_ok=True)
    filename = f"input/{subtask}-{test_num:02d}.in"
    with open(filename, "w") as f:
        f.write(f"{N}\n")
        f.write(f"{K}\n")
        A = [random.randint(Ai_min, Ai_max) for _ in range(N)]
        if sorted_array:
            A.sort()
        f.write(" ".join(map(str, A)) + "\n")
    print(f"Generated: {filename}")

def main():
    random.seed(42)

    # Subtask 1
    for t in range(1, 5):
        N = random.randint(1, 10**5)
        generate_testcase(1, t, N, 1, 10**3, N)

    # Subtask 2
    for t in range(1, 7):
        N = random.randint(1, 10**5)
        generate_testcase(2, t, N, 1, 10**8, N)

    # Subtask 3
    for t in range(1, 5):
        N = random.randint(1, 10**5)
        K = random.randint(1, N)
        generate_testcase(3, t, N, 1, 10**3, K, sorted_array=True)

    # Subtask 4
    for t in range(1, 7):
        N = random.randint(1, 10**5)
        K = random.randint(1, N)
        generate_testcase(4, t, N, 1, 10**8, K, sorted_array=True)

    # Subtask 5
    for t in range(1, 7):
        N = random.randint(1, 10**5)
        K = random.randint(1, N)
        generate_testcase(5, t, N, 1, 10**8, K)

if __name__ == "__main__":
    main()
