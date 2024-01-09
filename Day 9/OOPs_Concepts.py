# Customer is the base class, and GoldCustomer and PlatinumCustomer are subclasses with additional attributes 
# The CustomerSegmentation class is responsible for segmenting customers based on their type

class Customer:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        
class GoldCustomer(Customer):
    def __init__(self, name, age, gender, loyalty_points):
        super().__init__(name, age, gender)
        self.loyalty_points = loyalty_points
        
    def display_info(self):
        super().display_info()
        print(f"Loyalty Points: {self.loyalty_points}")
        
class PlatinumCustomer(GoldCustomer):
    def __init__(self, name, age, gender, loyalty_points, exclusive_benefits):
        super().__init__(name, age, gender, loyalty_points)
        self.exclusive_benefits = exclusive_benefits
    
    def display_info(self):
        super().display_info()
        print(f"Exclusive Benefits: {self.exclusive_benefits}")
        
class CustomerSegmentation:
# This class creates list objects. This list will contain the customer objects.
    def __init__(self):
        self.customers = [] # Creating an empty list to add customers
        
    def add_customer(self, customer): # Method to add customer to customers list
        self.customers.append(customer) # Append the customers list with customer
        
    # This method with be performed on the list of customer objects       
    def segment_customers(self):
        # isinstance function checks if an object is an instance of a particular class
        # It classifies the type of customer
        for customer in self.customers:
            if isinstance(customer, PlatinumCustomer):
                print(f"{customer.name} belongs to the Platinum segment.")
            elif isinstance(customer, GoldCustomer):
                print(f"{customer.name} belongs to the Gold segment.")
            else:
                print(f"{customer.name} belongs to the Standard segment.")
                
segmentation = CustomerSegmentation()

# Instantiate customer objects
standard_customer = Customer("Sanajay Kumar", 30, "Male")
gold_customer = GoldCustomer("Sunidhi Sudhir", 35, "Female", 1000)
platinum_customer = PlatinumCustomer("Karan Johnson", 40, "Male", 2000, "Free shipping")
      
# Add customers to segmentation
segmentation.add_customer(standard_customer) # add_customer() appends the customers list
segmentation.add_customer(gold_customer)
segmentation.add_customer(platinum_customer)

# Call segmentation function
segmentation.segment_customers() # segment_customers() segements the customer depending upon the object type

# Displaying the details of different customers (method overloading)
print("\nDisplaying the details of different customers:")
standard_customer.display_info()
print("_____________________________________")
gold_customer.display_info()
print("_____________________________________")
platinum_customer.display_info()
print("_____________________________________")