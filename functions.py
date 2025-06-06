#Well wishes
def well_wishes():
    print("hello")
    print("how are you?")

well_wishes()

#Weather conditions
def weather_condition():
    print('The weather is pleasant in:', spring)
    print('The weather is same in:', autumn)

spring = "summer"
autumn = "autumn"
weather_condition()

#Calculator
def add(P,Q):
    #This function is used for adding two numbers
    return P + Q
def subtract (P,Q):
    #This function is used for subrtacting two numbers
    return P - Q
def multiply(P,Q):
    #This function is used for multiplying two numbers
    return P * Q
def divide(P,Q):
    #This function is used for dividing
    return P / Q

#Now we will take inputs from the user
print("Please select the operation")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter your choice: ")

num_1 = int (input("Please enter the first number: "))
num_2 = int (input("Please enter the second number"))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2) )
    
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
    
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1,num_2))

else:
    print("This is an invalid input")
    

#Finding area of square

def area_of_square(a):
    return a * a


num = int(input("Enter the side of a square: "))
print("The area of the square is", area_of_square(num))


