def print_diamond(n):
    # Upper part of the diamond
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))

    # Lower part of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))

# Set the size of the diamond
size = 5
print_diamond(size)
