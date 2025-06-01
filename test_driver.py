# test_driver.py
import subprocess

# Call the microservice
subprocess.run(["python", "microservice.py"])

# Read output
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())
