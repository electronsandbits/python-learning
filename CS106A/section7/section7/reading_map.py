import sys


# Reading map problems
def map_one():
    counting = [5, 6, 7, 8]
    jenny = [8, 6, 7, 5, 3, 0]
    lst = list(map(lambda lst: lst.append(9), [counting, jenny]))
    print(lst)

def map_two():
    counting = [5, 6, 7, 8]
    jenny = [8, 6, 7, 5, 3, 0]
    lst = list(map(lambda lst: lst + [9], [counting, jenny]))

def main():
    args = sys.argv[1:]
    if args[0] == '-map_one':
        map_one()
    if args[0] == "-map_two":
        map_two()

if __name__ == "__main__":
    main()