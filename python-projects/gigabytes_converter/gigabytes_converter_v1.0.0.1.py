# Get user input for gigabytes and call conversion function.
def main():
    
    # Prompt for GB input.
    prompt = int(input("Enter the GB number: "))

    # Call function for conversion.
    output = bytes_converter(prompt)
    
    if output is not False:    # Check for errors. 
        print(f"{output:,}")    # Print result if successful.


# Convert gigabytes to bytes and handling errors.
def bytes_converter(prompt):
    
    if prompt <= 0:    # Check for invalid input.
        print("Error: \"Conversion from zero or negative gigabytes is not allowed\"")
        return False    # Signal error.
    else:
        # Reset prompt to 0.
        prompt = 0

        # Add 1 billion to prompt (assumes conversion logic).
        b = prompt + 1000000000
        return b    # Return the conversion result.
    

# Call the main function to execute the program.
main()