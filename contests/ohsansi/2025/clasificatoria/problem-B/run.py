import os
import subprocess

def generate_outputs():
    # Create 'output' directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Compile the C++ solution
    compile_result = subprocess.run(["g++", "-O2", "-std=c++14", "sol.cpp", "-o", "sol"], capture_output=True)
    if compile_result.returncode != 0:
        print("Compilation failed:")
        print(compile_result.stderr.decode())
        return

    # List all input files
    input_files = sorted(os.listdir("input"))

    for infile in input_files:
        if infile.endswith(".in"):
            infile_path = os.path.join("input", infile)
            outfile_path = os.path.join("output", infile.replace(".in", ".out"))

            # Run the solution with the input file and capture the output
            with open(infile_path, "r") as fin, open(outfile_path, "w") as fout:
                subprocess.run(["./sol"], stdin=fin, stdout=fout)

            print(f"Generated: {outfile_path}")

if __name__ == "__main__":
    generate_outputs()
