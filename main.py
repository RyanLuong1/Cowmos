import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
def menu():
    print(f'1. Graph\n2. Exit\n')

def function_menu():
    print(f'1. mx + b\n2. x^n\n3. sqrt(x)\n4. |x|\n5. 1/x\n6. ln(x)\n7. e^x\n8. cos(x)\n9. sin(x)\n10. tan(x)\n11. ???')

def create_linear_function():
    #Start here to ask the user for m and b and return it as a string. If m is 5 and b is 10, then the return string is 5 * x + 10

def create_exponential_function():
    #Start here to ask the user for n and return it as a string. If n is 5, then the return string is x ^ 5
    
def create_function(val):
    #Start here to retrieve the Python version of the math function given the user input in a string
    #The only input you don't need to consider are 1 and 2 since those are linear and exponent function which will ask the user for additional information
    #If val is 11, then return ???

def math_function_name(function):
    function_names = {"x**(1/2)": "sqrt(x)", 
                      "abs(x)": "abs(x)",
                      "1/x": "1/x",
                      "math.log(x)": "ln(x)",
                      "math.exp(x)": "e^x",
                      "math.cos(x)": "cos(x)",
                      "math.sin(x)": "sin(x)",
                      "math.tan(x)": "tan(x)"}
    return function_names[function]

def min_max_math_function(function):
    function_range = {"x**(1/2)": (math.inf, -math.inf), 
                      "abs(x)": (math.inf, -math.inf),
                      "1/x": (1, math.inf),
                      "math.log(x)": (0, math.inf),
                      "math.exp(x)": (-math.inf, math.inf),
                      "math.cos(x)": (-math.inf, math.inf),
                      "math.sin(x)": (-math.inf, math.inf),
                      "math.tan(x)": (-math.inf, math.inf)}
    return function_range[function]

def x_values(function):
    x = []
    min, max = min_max_math_function(function)
    function_name = math_function_name(function)
    #Use these three variables to get the inputs from the user. 
    #Just initializing 
    minimum = -math.inf 
    maximum = math.inf
    interval = 0
    while not x:
        #Start here to get the min and max from the user and check if the minimum or maximum given by the user is within the range
        else:
            for i in range(minimum, maximum + 1, interval):
                x.append(i)
    print(x)
    return x

def y_values(function, x_values):
    y_values = []
    for x in x_values:
        x = x
        result = eval(function)
        y_values.append(result)
    return y_values

def graph(function):
    if function == "???":
        img = mpimg.imread("cow.png")
        cow_plot = plt.imshow(img)
    else:
        x_axis = x_values(function)
        y_axis = y_values(function, x_axis)
        plt.plot(x_axis,y_axis)
        plt.xlabel("X")
        plt.ylabel("Y")
        # Change "My graph" to the function name. If I plotted "1/x", then the graph title should be "1/x".
        #Note that if the original math function name and the Python version is different, use the original name
        #For example if I plotted "cos(x)", I want "cos(x)" as the title, not "math.cos(x)"
        plt.title("My graph")
    plt.show()
    
while True:
    try:
        menu()
        user_input = int(input("Enter your choice: "))
        if user_input <= 0 or user_input >= 3:
            print("Out of range\n")
            continue
        elif user_input == 2:
            break
        else:
            try:
                function_menu()
                user_input = int(input("Enter your choice: "))
                if user_input <= 0 or user_input >= 12:
                    print("Out of range\n")
                    continue
                else:
                    function = ""
                    if user_input == 1:
                        function = create_linear_function()
                    elif user_input == 2:
                        function = create_exponential_function()
                    else:
                        function = create_function(user_input)
                    graph(function)
            except ValueError:
                print("I don't understand that\n")
                continue
    except ValueError:
        print("I don't understand that")
        continue