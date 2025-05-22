# Microservice A implementation: Word Analyzer Microservice
This microservice reads text based command requests from a file and returns analysis results. It is designed to be called progammatically bt another microservice via sipmle file I/O.

# Communication contract: 
This contract is fixed. Do not change onces implementation begins.

# Request data: 
Each request must be written on a new line in the format 
<command>,<word>

Commands supported:
length<word> : returns the number of characters
vowels,<word> : returns the number of vowels
repeats,<word> : returns the number of letters that appear more than once

Write your requests in the file input.txt. Example:
length,dog
vowels,cat
repeats,beachball

Response output (in output.txt):
3
1
3

# How to implement the microservice and programmatically data:
Write request to input.txt
Call the microservice 
Read result from output.txt

with open("input.txt", "w") as f:
    f.write("vowels,hello\n")
    f.write("length,world\n")


import subprocess
subprocess.run(["./word_analyzer"])


with open("output.txt", "r") as f:
    results = f.readlines()
    print("Results:", [r.strip() for r in results])

# Build instructions:
python main.py

UML Sequence Diagram:

![image](https://github.com/user-attachments/assets/84937e1e-7335-4242-8f02-13d4f2497f45)

