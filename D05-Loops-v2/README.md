## Day 5 - Loops_2

grind is low today due to light and rain reasons will take care tomorrow and make a comeback :) .

- Remember that the classic game Mario has a hero jumping over bricks. Let’s create a textual representation of this game.

Begin coding as follows:

```python
print("#")
print("#")
****print("#")

#Better Approach for the same 
for _ in range(3):
	print("#")
```

Consider: Could we further abstract for solving more sophisticated problems later with this code? Modify your code as follows:

```python
**def** main():
  print_column(3)
	print_row(4)

#Printing row wise 
**def** print_column(height):
    **for** _ **in** range(height):
        print("#")

#Printing Horizontally in row wise 
**def** print_row(width):
    print("?" * width)

main()
```

Notice how our column can grow as much as we want without any hard coding.

Notice how we now have code that can create left to right blocks.

Consider, how could we implement both rows and columns within our code? Modify your code as follows:

```python
# mario.py
def main():
    print_column(3)
    print_row(5)
    print_square(3)
    square_newlogic(5)

def print_column(height):
    for _ in range(height):
        print("#")
## we can write print("#\n * height , end="")

def print_row(length):
    for _ in range(length):
        print("#" , end ="")
    print()

#For each row in square 
def print_square(size):
    print(f"Printing the Square of {size}")
    for row in range(size):

        #for each row in the square
        for column in range(size):

            #printing the brick of mario
            print("#", end="")

        #printing the next line for the column
        print()

def square_newlogic(size):
    for row in range(size):
        print_row(size)

main()
```

Notice that we have an outer loop addresses each row in the square. Then, we have an inner loop that prints a brick in each row. Finally, we have a `print` statement that prints a blank line.
