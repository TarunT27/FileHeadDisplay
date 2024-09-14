import random

# Open the file for reading 
with open('random_numbers.txt') as f:
  numbers = f.readlines()

# Convert each line to an integer
numbers = [int(num.strip()) for num in numbers] 

# Print the numbers  
print("The random numbers are:")
for num in numbers:
  print(num)

# Calculate total and count
total = sum(numbers)
count = len(numbers)

print(f"The total of the numbers is: {total}") 
print(f"The number of random numbers is: {count}")
def display_file_head(filename):
  """Displays the first five lines of a file's contents.

  Args:
    filename: The name of the file to read from.
  """

  with open(filename, "r") as f:
    lines = f.readlines()
    num_lines = min(5, len(lines))  
    for i in range(num_lines):
      print(lines[i].rstrip())  

def main():
  """Prompts the user for the filename and displays the file's head."""

  filename = input("Enter the name of the file: ")
  display_file_head(filename)

if __name__ == "__main__":
  main()
