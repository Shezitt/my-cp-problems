import random
import os

def write_testcase(filename, N):
    """Write a single test case to a file."""
    with open(f"input/{filename}", "w") as f:
        f.write(f"{N}\n")

def generate_testcases():
    # Create 'input' directory if it doesn't exist
    os.makedirs("input", exist_ok=True)

    subtask_counts = {
        1: 5,  # Subtask 1: N is even
        2: 5,  # Subtask 2: N is odd
        3: 5,  # Subtask 3: 1 <= N <= 10^5
        4: 5,   # Subtask 4: 1 <= N <= 10^9
        5: 5    # Subtask 5: 1 <= N <= 10^18
    }

    for subtask, count in subtask_counts.items():
        for testnum in range(1, count + 1):
            if subtask == 1:
                N = random.randrange(2, 10**9, 2)
            elif subtask == 2:
                N = random.randrange(1, 10**9, 2)
            elif subtask == 3:
                N = random.randint(1, 10**5)
            elif subtask == 4:
                N = random.randint(1, 10**9)
            if subtask == 5:
                N = random.randint(1, 10**18)

            filename = f"{subtask}-{testnum:02}.in"
            write_testcase(filename, N)

if __name__ == "__main__":
    generate_testcases()
