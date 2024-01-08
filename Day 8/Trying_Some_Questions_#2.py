# Question 1:
print("Question 1:")
# Accepts a sequence of comma-separated numbers and generates a list and a tuple

input_sequence = input("Enter comma-separated numbers: ")
numbers_list = input_sequence.split(',')
numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)

# Question 2:
print("\nQuestion 2:")
# Defines a class with two methods: getString and printString

class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

# Test function
def testStringManipulator():
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()

# Test the class methods
testStringManipulator()

# Question 3:
print("\nQuestion 3:")
# Takes 2 digits as input and generates a 2-dimensional array

X, Y = map(int, input("Enter two digits separated by a comma: ").split(','))
result_array = [[i * j for j in range(Y)] for i in range(X)]

print(result_array)

# Question 4:
print("\nQuestion 4:")
# Accepts a comma-separated sequence of words and prints them alphabetically

input_words = input("Enter comma-separated words: ")
sorted_words = sorted(input_words.split(','))

output_sequence = ','.join(sorted_words)
print(output_sequence)

# Question 5:
print("\nQuestion 5:")
# Accepts sequence of lines and prints them in uppercase

input_lines = []
while True:
    line = input("Enter a line (press Enter to finish): ")
    if not line:
        break
    input_lines.append(line)

capitalized_lines = [line.upper() for line in input_lines]
for line in capitalized_lines:
    print(line)
