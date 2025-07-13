# File name to read
filename = 'C:\\Users\\albert\\code\\DevOps-TuteDude\\PythonAndBashAssignment\\Task-04\\meaningful_random_text.txt'

try:
    # Open and read line by line
    with open(filename, 'r') as file:
        print("\nFile content (line by line):")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
    file.close()

    # Open and read line by line
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Content:")
        print(content)
    file.close()

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")