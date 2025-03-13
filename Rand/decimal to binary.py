def is_decimal(num):
    """Checks if the input is a valid integer (decimal number)."""
    try:
        int(num)  # Try converting to an integer
        return True
    except ValueError:
        return False

def decimal_to_binary():
    """Repeatedly asks for a valid decimal number and converts it to binary."""
    while True:  # Loop until a valid input is given
        num = input("Enter a Decimal Number: ")
        
        if is_decimal(num):  # Check if input is a valid integer
            decimal_num = int(num)
            binary_num = bin(decimal_num)[2:]  # Convert to binary, remove '0b' prefix
            print(f"Binary equivalent: {binary_num}")
            break  # Exit loop after successful conversion
        else:
            print("Invalid input! Please enter a valid decimal number.")

# Run the function
decimal_to_binary()
