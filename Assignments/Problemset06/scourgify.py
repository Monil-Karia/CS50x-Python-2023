import csv
import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
    with open(sys.argv[1], "r") as file:
        Lines = csv.DictReader(file)
        for row in Lines:
            firstName, lastName = row["name"].split(", ")
            home = row["house"]
            data =[row for row in Lines]
            with open("after.csv", "a") as newfile:
                writer = csv.DictWriter(
                    newfile, fieldnames=["Firstname", "LastName", "Home"]
                )
                writer.writerow(
                    {"Firstname": firstName, "LastName": lastName, "Home": home}
                )
                print(tabulate(data,headers="keys"))
elif len(sys.argv) > 2:
    sys.exit("Too many Command line Arguments")
elif len(sys.argv) < 2:
    sys.exit("Less number Command line Arguments")
else:
    sys.exit("Invalid File")
