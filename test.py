import random

def append_random_number(num):
    # Generate a random number with 4 digits
    num2 = random.randint(1000, 9999)

    # Combine the numbers and ensure the total is 6 digits
    combined_number = int(str(num2) + str(num).zfill(2))  # Convert to int to remove leading zeros
    combined_number_str = str(combined_number)

    return combined_number_str

# Example usage:
given_number1 = 9
result1 = append_random_number(given_number1)
print(f"{given_number1} -> {result1}")

given_number2 = 98
result2 = append_random_number(given_number2)
print(f"{given_number2} -> {result2}")