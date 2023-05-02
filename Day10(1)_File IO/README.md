# File I/O
We are using Files for using the data and use the data and  we will store in file.

### Must Watch Lecture , Vast as well as Informative

- sorted() → It is a keyword to use when we want a sorted list or an dict
- https://docs.python.org/3/library/functions.html?highlight=sorted#sorted
 
- open() →  We use open keyword to open a file in a system
    
    Docs → [https://docs.python.org/3/library/functions.html?highlight=open#open](https://docs.python.org/3/library/functions.html?highlight=open#open)
    
    
    ```python
    
    name = input("What's your name? ")
    
    #Opens the names.txt in the writing mode 
    # file = open("names.txt" , "a") we are using a to append in the file 
    file = open("names.txt" , "w")
    #Writing the name in  the File
    file.write(name)
    # After writing the names in the file we close the file and save it 
    file.close()
    
    ```
    
- with() → The **`with` statement** in Python is used for resource management and exception handling. You’d most likely find it when working with file streams
    
     For example, the statement ensures that the file stream process doesn’t block other processes if an exception is raised, but terminates properly.
    
    The code block below shows the `try`-`finally` approach to file stream resource management.
    
    ```python
    file = open('file-path', 'w')
    try:
        file.write('Lorem ipsum')
    finally:
        file.close()
    
    ```
    
    Normally, you’d want to use this method for writing to a file, but the `with` statement offers a cleaner approach:
    
    ```python
    with open('file-path', 'w') as file:
        file.write('Lorem ipsum')
    
    ```
    
    The `with` statement simplifies our `write` process to just two lines.
    
    It is also used in database CRUD processes. This example was taken from [this site](https://mherman.org/blog/flask-for-node-developers/):
    
    ```python
    def get_all_songs():
        with sqlite3.connect('db/songs.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM songs ORDER BY id desc")
            all_songs = cursor.fetchall()
            return all_songs
    
    ```
    
    Here, `with` is used to query an SQLite database and return its content.
    
- readlines() → readlines is the function which we are using for the reading the line of the file.
    
    ```python
    #name_v3
    with open("names.txt" , "r") as file:
        #Beware that readline() is also a function which just reads the lines of the code 
        lines = file.readlines()
    
    for line in lines:
        print("Hello," , line.rstrip())
    ```
    

CSV → Comma Separated Values

Imp → Python allows us to give the arguments to other functions of the functions 

Example → 

```python
students = []

with open("students.csv") as file:
    for line in file:
        name , house = line.rsplit().split(",")
        #one liner code 
        student = {"name": name , "house" : house}
        # same as above code but mor lines 
        # student["name"] = name
        # student["house"] = house
        students.append(student)

def get_name(student):
    return student['name']

#get_name we are giving the value of function in a sorted function
for student in sorted(students , key = get_name):
    #Why Single Quote?
    #In dict when we use to index in it then we use the single quote instead of double 
    # 
    print(f"{student['name']} is in {student['house']}")
```

Lambda Function : It is function which doesn't have a name we will call it anonymously 

- Example →
    
    ```python
    students = []
    
    with open("students.csv") as file:
        for line in file:
            name , house = line.rstrip().split(",")
            #one liner code 
            student = {"name": name , "house" : house}
            # same as above code but mor lines 
            # student["name"] = name
            # student["house"] = house
            students.append(student)
    
    def get_name(student):
        return student['name']
    
    #not passing parenthesis beacuse sorted will call it by itself and also 
    #Lambda Function 
    for student in sorted(students , key=lambda student:student["name"]):
        #Why Single Quote?
        #In dict when we use to index in it then we use the single quote instead of double 
        # 
        print(f"{student['name']} is in {student['house']}")
    ```
