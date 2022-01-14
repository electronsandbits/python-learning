from grid import Grid

def can_bubble_up(grid, x, y):
    """
    Implement this function as described in the handout. Add some more doctests.
    >>> grid = Grid.build([[None, 'r', 'b'], ['b', 'b', 'b']])
    >>> can_bubble_up(grid, 0, 1)
    True
    >>> can_bubble_up(grid, 0, 0)
    False
    >>> can_bubble_up(grid, 2, 1)
    False
    """
    pass

def main():
    print("\nChecking solutions to problems...\n")
    grid = Grid.build([[None, 'r', 'b'], ['b', 'b', 'b']])
    print("grid = Grid.build([[None, 'r', 'b'], ['b', 'b', 'b']])")
    can_bubble_up(grid, 1, 0)
    print("Calling bubble_up(grid, 1) returns " + str(grid))

if __name__ == "__main__":
    main()