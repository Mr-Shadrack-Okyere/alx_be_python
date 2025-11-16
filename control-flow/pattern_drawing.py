# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop to handle rows
while row < size:
    # Inner loop to handle columns (printing asterisks in a row)
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after a row is printed
    row += 1  # Increment row counter
