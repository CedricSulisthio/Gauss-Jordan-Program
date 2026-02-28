# Gauss - Jordan

def GaussJordan(matrix): # Defines a function named GaussJordan that takes one argument matrix.
    n = len(matrix) # Gets the number of rows in the matrix and assigns it to the variable n.
    for i in range(n): # Starts a loop that will iterate n times. The variable i will take the values from 0 to n - 1 in each iteration.
        # Initializes the maximum element in the current column to the element at the current row and column and the maximum row to the current row.
        maxelements = abs(matrix[i][i])
        maxrows = i
        # Searches for the maximum element in the current column below the current row. If a larger element is found, updates the maximum element and the maximum row.
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > maxelements:
                maxelements = abs(matrix[k][i])
                maxrows = k
        # Explanation: Swap row {i} with row {maxrows} to make the current column non-zero.
        matrix[i], matrix[maxrows] = matrix[maxrows], matrix[i]
        # Rounds the numbers in the matrix to two decimal places
        for j in range(n + 1):
            matrix[i][j] = round(matrix[i][j], 2)
        # Prints a message indicating that the rows have been swapped and then prints the current state of the matrix.
        print(f"Swapped row {i} with row {maxrows} :")
        for row in matrix:
            print([round(x, 2) for x in row])
        for k in range(i + 1, n):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] += c * matrix[i][j]
                matrix[k][j] = round(matrix[k][j], 2)
            # Multiply row {i} by {c} and add it to row {k} to make the first column zero below row {i}.
            print(f"Explanation : Multiply row {i} by {c} and add it to row {k} to make the first column zero below row {i}.")
        # Prints a message indicating that the rows below the current row have been made zero in the current column and then prints the current state of the matrix.
        print(f"Made rows below row {i} zero in current column :")
        for row in matrix:
            print([round(x, 2) for x in row])
    for i in range(n):
        c = 1 / matrix[i][i]
        for j in range(n + 1):
            matrix[i][j] *= c
            matrix[i][j] = round(matrix[i][j], 2)
        print(f"Made leading coefficient 1 in row {i} :")
        for row in matrix:
            print([round(x, 2) for x in row])
    for i in range(n - 1, -1, -1): # Divide each element in the current row by the leading coefficient to make the leading coefficient 1.
        for k in range(i - 1, -1, -1):
            c = matrix[k][i]
            for j in range(n + 1):
                matrix[k][j] -= c * matrix[i][j]
                matrix[k][j] = round(matrix[k][j], 2)
            print(f"Explanation : Subtract {c} times row {i} from row {k} to make the coefficient zero above row {i}.")
        print(f"Made coefficients zero above row {i} :")
        for row in matrix:
            print([round(x, 2) for x in row])
    x = [[round(matrix[i][n], 1)] for i in range(n)]
    return x
# Defines a function named main.
def main():
    # Starts a try block to catch any exceptions that may be raised.
    try:
        # Asks the user to enter the number of variables and converts the input to an integer.
        n = int(input("Enter the number of variables (maximum = 10) : "))
        # Checks if the number of variables is within the valid range. If not, raises a ValueError exception.
        if n <= 0 or n > 10:
            raise ValueError("The number of variables must be between 1 and 10.")
        # Sets the number of equations to be equal to the number of variables.
        m = n
        # Initializes an empty list matrix to store the coefficients and results of the equations.
        matrix = []
        # Asks the user to enter the coefficients and results of the equations and stores them in the matrix.
        for i in range(m): # i refers to the equation and its result.
            row = []
            for j in range(n): # j refers to the coefficient.
                coefficient = float(input("Coefficient {} for equation {} : ".format(j + 1, i + 1)))
                row.append(coefficient)
            result = float(input("Result for equation {} : ".format(i + 1)))
            row.append(result)
            matrix.append(row)
        # Prints the matrix before applying the Gauss - Jordan elimination.
        print("Matrix before Gauss - Jordan :")
        for row in matrix:
            print(row)
        # Calls the Gauss - Jordan function to solve the system of equations and stores the solution in the solution variable.
        solution = GaussJordan(matrix)
        # Checks if the solution is a string. If so, prints the error message. Otherwise, prints the solution.
        if isinstance(solution, str):
            print(solution)
        else:
            print("Solution : ", solution)
    # Catches any ValueError exceptions that may be raised and prints an error message.
    except ValueError as e:
        print("Error :", e)
main() # Calls the main function to start the program.