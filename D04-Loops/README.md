# Loops
We need loops in the programming because loops allow a task to shorten what could be hundred of lines to code tom just a few.

### While Loop -

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

- Example Code :
    
    We can improve our code, to start counting with zero:
    
    ```python
    i = 0
    **while** i < 3:
        print("meow")
        i += 1
    ```
    

### List - Square brackets represents the list []

It is basically related to real life that a list of something means list of multiple values in the same thing . 

- Example Code →
    
    ```python
    #Usage of for loop and list in the same program 
    for i in [0 ,1 , 2]:
        print("Meow")
    #Better way of writing the same code instead of writing the list number 
    for i in range(10):
        print("Meow")
    ```
    

<aside>
💡 God Logic’s and Important concepts

```python
#if a variable name is not used in futher code we use _
for _ in range(3):
    print("Meow")
#God logic 
print("Meow" * 3)   #Output ->MeowMeowMeow
```

</aside>

### Continue and Break keywords

`continue`explicitly tells Python to go to the next iteration of a loop. `break`, on the other hand, tells Python to “break out” of a loop early, before it has finished all of its iterations. In this case, we’ll  `continue`  to the next iteration of the loop when `n` is less than 0—ultimately prompting the user with “What’s n?”. If though, `n` is greater than or equal to 0, we’ll `break` out of the loop and allow the rest of our program to run.

### For Loop -

It is used to iterate and do things in the program to iterate over something uptill the limit 

we have code such as 

```python
students = ["Hermoine" , "Harry" , "Ron"]

print(students)     #Output -> ['Hermoine', 'Harry', 'Ron']

for student in students:   #we used Student as we r gonna used in print statment
    print(student)
#In Python we have already intilised the student to first index of the students list and 
# as python is quite easy and readable to 3rd person as we write this Syntax 
```

```python
students = ["Hermoine" , "Harry" , "Ron"]

print(students)     #Output -> ['Hermoine', 'Harry', 'Ron']

for i in range(len(students)):   #we nested the range of student length 
    print(i+ 1, students[i])
# we have done some syntatically the changes and also printed the i varaible in print 
```

### Function → length() - used to get length of any list we have defined

### Data structure → dict - Important Concept

- Bunch of Words and Definations ,m but as per the CS student we have keys and Values .
- More powerful than list  , list is only a bunch of values whereas we have dictionary with keys and value
- As a list uses an index to acess some the elemets in the list but the dict uses actual words to find the information out
- its kind of 2D uses of dict
- Syntax Example →
    
    ```python
    #Now we are using dict as per our use name= {key : value}
    students = {
        "Hermoine": "Gryffindor",
        "Harry" : "Gryffindor" , 
        "Ron" : "Gryffindor" , 
        "Draco" : "Slytherin"
    }
    
    #calling
    print(students["Hermoine"])
    #We can only use key values 
    
    ```
    
- Printing the dictionary will be (key value only)→
    
    ```python
    for student in students:
        print(student)
    ```
    
    Upgraded format:
    
    ```python
    for student in students:
        print(student , students[student] ,  sep =" , ")
    
    #output will be 
    # Hermoine , Gryffindor
    # Harry , Gryffindor
    # Ron , Gryffindor
    # Draco , Slytherin
    ```
