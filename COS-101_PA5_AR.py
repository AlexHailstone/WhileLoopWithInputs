# For Programming Assignment 5, you are required to write a Python program 
# that asks the user for two positive integer values. 
# It would then use a while loop to compute the sum of all integers between (and including) 
# the two inputs before printing out the sum. 
# 
# 
# Sample runs would be as follows.

## Enter first positive integer: 2
## Enter second positive integer: 5
### The sum of integers between 2 and 5 (inclusive) is 14

## Enter first positive integer: 4
## Enter second positive integer: 6
### The sum of integers between 4 and 6 (inclusive) is 15



class SumBetweenIntegers:

    # Reusable method
    def get_positive_integer(self, prompt):
        # Prompt the user for a positive integer
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive integer greater than 0.")
            except ValueError:
                print("Invalid input; please enter an integer.")


    def calculate_and_print_sum(self):
        # Prompt for two positive integers, calculate and show the work for summing all integers between them 
        # (inclusive), and print the result
        first_int = self.get_positive_integer("Enter first positive integer: ")
        second_int = self.get_positive_integer("Enter second positive integer: ")

        if first_int > second_int:
            first_int, second_int = second_int, first_int  # Swap the values

        # Initialize total sum to set later
        total_sum = 0
        
        # Initialize an empty string to accumulate the work
        work_str = ""  

        # String builder for-loop to build out the string to show the work for the solution
        for current in range(first_int, second_int + 1):
            total_sum += current
            if current > first_int:  
                work_str += f"+{current}"
            else:
                work_str += f"{current}"
        
        # Outputs the final solution showing the first and second integer
        # Also outputs the final string from the string builder showing the work        
        print(f"The sum of integers between {first_int} and {second_int} (inclusive) is {total_sum}. Work: {work_str} = {total_sum}")

# To execute, create an instance of the class and then call the method
calculator = SumBetweenIntegers()
calculator.calculate_and_print_sum()

