import numpy as np

infinity = 99999.0  # Make infinity a floating-point number

# inputs start here
# A will contain the coefficients of the constraints
A = np.array([[1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0],
              [4.0, 3.0, 5.0, 0.0, 0.0, 0.0, 1.0]])
# b will contain the amount of resources
B = np.array([700.0, 600.0, 400.0, 6000.0])
# z will contain the coefficients of the objective function
Z = np.array([14.0, 12.0, 20.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# R
R = np.array([infinity, infinity, infinity, infinity])
# cb contains the basic variables
CB = np.array([0, 0, 0, 1, 1, 1, 1])
Bt = np.transpose([B])

table = np.hstack((A, Bt))
# inputs end here


def print_table(index_entering_variable, index_leaving_variable):
    global table, Z, R
    np.set_printoptions(suppress=True)  # Suppress scientific notation
    print("Table: ")
    for row in table:
        print("[" + ", ".join(f"{cell:.2f}" for cell in row) + "]")  # Display each row with 2 decimal places
    print()
    print(f"Z: {Z}")
    print()
    print(f"R: {R}")
    print()

    print(f"Entering variable: {index_entering_variable}")
    print(f"Leaving variable: {index_leaving_variable}")
    p = table[index_leaving_variable][index_entering_variable]
    print(f"Pivot: {p}")
    print()


# control variables
optimal_reached = False
iteration = 1

# algorithm


def get_index_entering_variable():  # works
    global Z, R
    max_value = Z[0]
    index = 0
    for i in range(len(Z)):
        if Z[i] > max_value and Z[i] > 0:
            max_value = Z[i]
            index = i
    return index


def update_r():
    global R, table
    index_entering_variable = get_index_entering_variable()
    R = np.divide(table[:, -1], table[:, index_entering_variable], out=np.full_like(table[:, -1], infinity),
                  where=table[:, index_entering_variable] != 0)
    print("R of updated: ", R)


def get_index_leaving_variable():  # works
    global R
    update_r()
    index_leaving_variable = 0
    min_ratio = R[0]
    for i in range(len(R)):
        if 0 < R[i] < min_ratio:
            min_ratio = R[i]
            index_leaving_variable = i
    return index_leaving_variable


def pivot(index_entering_variable, index_leaving_variable):
    global R, table, CB, Z, infinity
    pivot_element = table[index_leaving_variable][index_entering_variable]

    # Handle division by zero
    if pivot_element == 0:
        print("Warning: Pivot element is zero. Division result will be set to infinity.")

    table[index_leaving_variable] = np.where(pivot_element != 0, np.divide(table[index_leaving_variable], pivot_element)
                                             , np.full_like(table[index_leaving_variable], infinity))

    CB[index_leaving_variable+3] = 0
    CB[index_entering_variable] = 1
    # Update other rows
    for i in range(len(table)):
        if i != index_leaving_variable:
            coefficient = table[i][index_entering_variable]
            table[i] -= coefficient * table[index_leaving_variable]
    coefficient = Z[index_entering_variable]
    Z -= coefficient * table[index_leaving_variable]


def main():
    global optimal_reached,Z
    while not optimal_reached:
        index_entering_variable = get_index_entering_variable()  # Find entering variable
        index_leaving_variable = get_index_leaving_variable()  # Find leaving variable
        print_table(index_entering_variable, index_leaving_variable)  # Print the current state of the table
        pivot(index_entering_variable, index_leaving_variable)  # Perform pivot operation
        # Check for optimality
        if all(Z <= 0):
            optimal_reached = True
            print("Optimal solution reached.")
            print("Final table:")
            print_table(index_entering_variable, index_leaving_variable)
            print("Optimal solution:")
            print(f"Z = {-Z[-1]}")
            break


if __name__ == "__main__":
    main()  # Call the main function when the script is executed
