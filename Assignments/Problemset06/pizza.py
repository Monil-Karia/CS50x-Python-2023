import tabulate
import sys
import csv

if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
    with open(sys.argv[1]) as file:
        Lines = csv.DictReader(file)
        print(Lines)
        data = [row for row in Lines]   #mast line 
        print(data)
        print(tabulate.tabulate(data, headers="keys",tablefmt="pretty"))
elif len(sys.argv) > 2:
    sys.exit("Too many Command line Arguments")
elif len(sys.argv) < 2:
    sys.exit("Less number Command line Arguments")
