def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")

        # Print asterisks for the current row
        for k in range(1, 2 * i):
            print("*", end="")

        # Move to the next line after printing each row
        print()


# Example usage:
n = int(input("Enter the number of rows: "))
full_pyramid(n)
