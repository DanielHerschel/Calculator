# Calculator
A calculator that solves an equation that is given by the user.

# How to run the project

This project requires python version 3.6.

To run the tests, it's required to install pytest. To install it run in the cmd:
`pip install pytest` and run each test from it's corresponding batch file.

1. Download the project.
2. Run the calculator.bat file.
3. In the open cmd window, enter an equation or type 'X' to exit and press enter!

# The thought process
First I thought on how to solve the equation. I had an idea in mind solving
the equations recursively by finding the most inner parentheses and solving the 
mathematical expression inside it, replacing the result with the old parentheses
and so on until the equation is solved.

Next I started creating the input validation. I had a hard time finding all the 
edge cases of the validation and ended up updating it every few days.
In the end I managed to finish the validation.

Next I added tests, and it was fun finding edge cases with my classmates.

After fixing bugs and making my code generic, I added the main method and
custom exceptions and caught them in the main method (and test functions).

Overall it was a fun project that made the whole class work together.