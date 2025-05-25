import os
import random

def generate_subtask_1(test_count):
    for t in range(1, test_count + 1):
        N = random.randint(1, 1000)
        A = [random.randint(1, 10**6) for _ in range(N)]
        for i in range(1, N):
            while A[i] == A[i-1]:
                A[i] = random.randint(1, 10**6)
        write_input_file(1, t, N, A)

def generate_subtask_2(test_count):
    for t in range(1, test_count + 1):
        N = random.randint(2, 1000)
        A = []
        i = 0
        while i < N:
            value = random.randint(1, 10**6)
            A.append(value)
            if i+1 < N:
                if random.choice([True, False]):
                    A.append(value)
                    i += 1
            i += 1
        if len(A) > N:
            A = A[:N]
        write_input_file(2, t, len(A), A)

def generate_subtask_3(test_count):
    for t in range(1, test_count + 1):
        N = random.randint(1, 1000)
        A = [random.randint(1, 10**6) for _ in range(N)]
        write_input_file(3, t, N, A)

def generate_subtask_3_strong(test_count, start_num):
    for t in range(start_num, start_num + test_count):
        N = random.randint(500, 1000)
        A = []
        i = 0
        while i < N:
            value = random.randint(1, 10**6)
            repeat_count = random.randint(1, min(5, N-i))  # up to 5 consecutive duplicates
            A.extend([value] * repeat_count)
            i += repeat_count
        if len(A) > N:
            A = A[:N]
        write_input_file(3, t, len(A), A)

def generate_subtask_4(test_count):
    for t in range(1, test_count + 1):
        N = random.randint(1, 10**5)
        A = [random.randint(1, 10**6) for _ in range(N)]
        write_input_file(4, t, N, A)

def generate_subtask_4_strong(test_count, start_num):
    for t in range(start_num, start_num + test_count):
        N = random.randint(5 * 10**4, 10**5)
        A = []
        i = 0
        while i < N:
            value = random.randint(1, 10**6)
            repeat_count = random.randint(1, min(20, N-i))  # up to 20 consecutive duplicates
            A.extend([value] * repeat_count)
            i += repeat_count
        if len(A) > N:
            A = A[:N]
        write_input_file(4, t, len(A), A)

def write_input_file(subtask, test_num, N, A):
    os.makedirs("input", exist_ok=True)
    filename = f"input/{subtask}-{test_num:02d}.in"
    with open(filename, "w") as f:
        f.write(f"{N}\n")
        f.write(" ".join(map(str, A)) + "\n")
    print(f"Generated {filename}")

if __name__ == "__main__":
    generate_subtask_1(5)
    generate_subtask_2(5)
    generate_subtask_3(5)
    generate_subtask_3_strong(7, 6)  # generates 3-04.in, 3-05.in
    generate_subtask_4(5)
    generate_subtask_4_strong(7, 6)  # generates 4-04.in, 4-05.in

    # generate_subtask_3_strong(1, 12)  # generates 4-04.in, 4-05.in
