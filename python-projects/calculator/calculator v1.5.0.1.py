def main():
    # These three lines prompts the user to enter two numbers and an arithmetic operator.
    num1 = input("First number: ")
    o = input("Choose an operator: ")
    num2 = input("Second number: ")
    
    # Calls the basic_arith function.
    c1 = basic_arith(num1, o, num2)

    # Calls the intermediate_arith function.
    c2 = intermediate_arith(num1, o, num2)

    # Calls the advansed_arith function.        
    c3 = advansed_arith(num1, o, num2)

    
    # Prints the result of the arithmetic operations
    print("Equals:", c1, c2, c3)


# This function performs basic arithmetic operations.
def basic_arith(num1, o, num2):
    
    # These two lines checks for the addition operator (+); if found, it triggers addition.
    if o == "+":
        a = int(num1) + int(num2)
        
        # Returns the result of the addition.
        return a

    # These two lines checks for the subtraction operator (-); if found, it triggers subtraction.
    elif o == "-":
        s = int(num1) - int(num2)
        
        # Returns the result of the subtraction.
        return s    
    
    # These two lines checks for the multiplication operator (*); if found, it triggers multiplication.
    elif o == "*":
        m = int(num1) * int(num2)
        
        # Returns the result of the multiplication.
        return m
    
    # These two lines checks for the division operator (/); if found, it triggers division.
    elif o == "/":
        d = int(num1) / int(num2)
        
        # Returns the result of the division. 
        return d


# This function performs intermediate arithmetic operations.
def intermediate_arith(num1, o, num2):

    # These two lines checks for the exponentiation operator (**); if found, it triggers exponentiation.
    if o == "**":
        p = int(num1) ** int(num2)
        
        # Returns the result of the exponentiation.
        return p


# This function performs advansed arithmetic operations.
def advansed_arith(num1, o, num2):

    # These two lines checks for the modulo operater (%); if found, it triggers modulo.
    if o == "%":
        d = int(num1) % int(num2)

        # Returns the result of the modulo.
        return d


# Calls the main function to execute the program.
main()
