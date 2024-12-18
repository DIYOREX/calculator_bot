numbers_map = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

def number_to_words(number: int) -> str:
    """
    Given a number, return its word representation in English.
    
    Parameters:
    number (int): The number to convert.
    
    Returns:
    str: The English word representation of the number.
    """
    
    if number == 0:
        return "zero"
    
    words = []
    
    # Handle hundreds place
    hundreds = number // 100
    if hundreds > 0:
        words.append(f'{numbers_map[hundreds]} hundred')
    
    # Handle tens and ones place
    tens_ones = number % 100
    if tens_ones > 0:
        if tens_ones <= 20:  # Special case for numbers between 1-20
            words.append(numbers_map[tens_ones])
        else:
            tens = (tens_ones // 10) * 10
            ones = tens_ones % 10
            words.append(numbers_map[tens])
            if ones > 0:
                words.append(numbers_map[ones])
    
    return ' '.join(words)

# Main logic for user input and output
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print(number_to_words(number))
    except ValueError:
        print("Please enter a valid integer.")
