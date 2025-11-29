def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        # To move to the new line
        print()

main()

"""
The code you provided defines two functions, main() and print_square(size). 

The main() function is called at the end of the code, 
and it invokes the print_square() function with a parameter value of 3. 

The print_square() function is responsible for printing a square made of bricks with a given size.

Let's go through the code step by step:

The main() function is defined.

Inside the main() function, the print_square(3) function is called, 
passing the value 3 as the size parameter.

The print_square() function is defined, which takes a single parameter called size.

Inside the print_square() function, a loop is used to iterate over each row of the square. 

The loop variable i takes values from 0 to size - 1.

Inside the row loop, another loop is used to iterate over each brick in the current row. 

The loop variable j also takes values from 0 to size - 1.

Inside the brick loop, the character "#" is printed using the print() function, 
with the 'end parameter' set to an empty string to avoid printing a newline character after each brick.

After the inner loop completes, a newline character is printed using print() to move to the next line and start a new row.
The outer loop continues until all rows are printed.

The main() function is invoked, and the program execution starts.

"""

"""
easy understanding look at the code below:

for i in range(3):
    for i in range(3):
        print('#', end='')
    print()
"""