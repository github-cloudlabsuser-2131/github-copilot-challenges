# A more refined example of a program in Python that prompts the user for the number of elements to sum, 
# takes those integers as input, and handles some basic error cases with improved practices.

MAX_ELEMENTS = 100

def calculate_sum(arr):
    """
    Calculate the sum of elements in the given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of the elements in the array.
    """
    return sum(arr)

def main():
    """
    Main function to execute the program logic.
    """
    while True:
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if 1 <= n <= MAX_ELEMENTS:
                break
            else:
                print("Invalid input. Please provide a digit ranging from 1 to 100.")
        except ValueError:
            print("Please enter a valid integer.")

    # Collecting user inputs in a more concise and safe manner
    arr = []
    for i in range(n):
        while True:
            try:
                element = int(input(f"Enter element {i+1}: "))
                arr.append(element)
                break
            except ValueError:
                print("Please enter a valid integer.")

    print(f"The sum of the entered elements is: {calculate_sum(arr)}")

if __name__ == "__main__":
    main()