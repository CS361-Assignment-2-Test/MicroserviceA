# microservice.py

from collections import Counter

def analyze_line(command, word):
    word = word.lower()
    if command == "length":
        return str(len(word))
    elif command == "vowels":
        return str(sum(1 for char in word if char in "aeiou"))
    elif command == "repeats":
        counts = Counter(word)
        return str(sum(1 for c in counts.values() if c > 1))
    else:
        return "error"

def process_file(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            parts = line.strip().split(",")
            if len(parts) != 2:
                outfile.write("error\n")
                continue
            command, word = parts
            result = analyze_line(command, word)
            outfile.write(result + "\n")

if __name__ == "__main__":
    process_file("input.txt", "output.txt")
