print("Hello, World! Welcome to my #CoffeeLovers chatbot.")

# Function to get a sensible answer
def get_sensible_answer(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ["yes", "no"]:
            return answer
        else:
            print("I'm not sure I understand... Please enter 'Yes' or 'No'.")

# Check if the user is a lover of coffee
answer = get_sensible_answer("Are you a lover of coffee? ")
if answer == "yes":
    print("Wow, me too!")
elif answer == "no":
    other_preference = input("Ok, what do you like instead? ")
    print(f"That's cool too! I also like {other_preference}.")
else:
    print("I'm not sure I understand...")

# Check if the user is a university student
answer = get_sensible_answer("Are you a university student? ")
if answer == "yes":
    print("Did you know that two large studies recently found that coffee drinkers lived longer than non–coffee drinkers? But drinking too much could cause anxiety, so please consume it responsibly :)")
elif answer == "no":
    print("Did you know that Americans aged 60 or older drink the most coffee? Around 72% of Americans who are 60 or older drink coffee every single day.")
else:
    print("I'm not sure I understand...")

# Check if the user knows that coffee is actually a fruit
answer = get_sensible_answer("Did you know that coffee is actually a fruit? ")
if answer == "no":
    print("Well, now you do! Despite it being called a ‘bean’, coffee is a fruit. The ‘beans’ grow on a bush and are found in the centre of a berry, known as a coffee cherry.")
elif answer == "yes":
    print("We got a smart cookie in our hands B)")
else:
    print("I'm not sure I understand...")
