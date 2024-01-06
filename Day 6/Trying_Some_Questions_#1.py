# Question 1:
print("Question 1:")
numbers=[] # Creating a list to add the numbers
for i in range(2000, 3201): # Range includes 2000 and 3200
    if i%7==0 and i%5!=0: # Numbers that are divisible by 7 and NOT divisible by 5
        numbers.append(str(i)) # Append the list after typecasting the number to string
        
print(','.join(numbers))

# Question 2:
print("\nQuestion 2:")
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def fact_finder():
    # Take user input
    num=int(input("Enter a number: "))
    
    result=factorial(num)
    print(f"The factorial of {num} is: {result}")
    
fact_finder()

# Question 3:
print("\nQuestion 3:")
def generate_square_dictionary(n):
    square_dictionary={i: i*i for i in range(1, n+1)}
    return square_dictionary
n=int(input("Enter an number: "))
result_dictionary=generate_square_dictionary(n)
print(result_dictionary)