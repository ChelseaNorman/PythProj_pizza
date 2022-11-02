from tabulate import tabulate
import sys
import csv

def main():
    check_argv()
    menu_output = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            pizza_menu = csv.reader(csvfile)
            for row in pizza_menu:
                menu_output.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(menu_output[1:], headers=menu_output[0], tablefmt="grid"))


def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()