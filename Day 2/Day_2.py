# This is a simple calculator program

ch=input("-This is a SIMPLE CALCULATOR- Proceed? Y/N ")
ch=ch.lower() # Making user input case insensitive
while ch=="y":
    a=input("Enter the first number: ") # Taking the first number
    a=int(a) # Typcasting it as an integer. Then doing the same to the second number.
    b=input("Enter the second number: ")
    b=int(b)

    # Creating a function to validate the operator input
    def get_sensible_operator(symbol):
        while True:
            op=input(symbol)
            # Only these operators are valid
            if op in ["+", "-", "*", "/", "%"]:
                return op
            else:
                print("ERROR! Enter a valid operator.")
            
    op=get_sensible_operator("Enter the operation (+, -, *, /, %): ")
    
    # Creating a calculator function to perform operations
    def calculator(a, b):
        if op=='+':
            return a+b
        elif op=='-':
            return a-b
        elif op=='*':
            return a*b
        elif op=='/':
            return a/b
        elif op=='%':
            return a%b
        else:
            return "ERROR! Enter a valid operator."

    result=calculator(a, b)
    print("--------------------------")
    print("The result is:", result)
    print("--------------------------")

    ch=input("Do you want to continue? Y/N ")

