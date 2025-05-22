# Microservice A implementation: Word Analyzer Microservice
This microservice reads text based command requests from a file and returns analysis results. It is designed to be called progammatically bt another microservice via sipmle file I/O.

# Communication contract: This contract is fixed. Do not change onces implementation begins.

# Request data: Each request must be written on a new line in the format 
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

# How to implement the microservice:
//Write request to input.txt
with open("input.txt", "w") as f:
    f.write("vowels,hello\n")
    f.write("length,world\n")

//Call the microservice 
import subprocess
subprocess.run(["./word_analyzer"])

//Read result from output.txt
with open("output.txt", "r") as f:
    results = f.readlines()
    print("Results:", [r.strip() for r in results])

Build instructions:
python main.py

UML Sequence Diagram:

![image](https://github.com/user-attachments/assets/1b9423ab-ce16-49ff-a939-a1e5d110681a)
