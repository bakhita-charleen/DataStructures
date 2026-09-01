# # ================= Creating and printing a list ==================

# shopping_list = ["Bread", "Milk", "Sugar", "Rice"]
# print(shopping_list)
# print(len(shopping_list))    # len returns total number of items in a list
# print()

# # ================= Example 2: Indexing =====================
# shopping_list = ['Bread', 'Milk', 'Sugar', 'Rice']
# #indexing           0       1       2          3
# # -ve indexing      -4      -3      -2        -1

# print(shopping_list[0]) #first item
# print(shopping_list[2]) #thirs item
# print(shopping_list[-1]) # last item - negative counts from the end
# print(shopping_list[-2]) #second to last
# print()

# # ============= Example 3: Looping over a list =================
# shopping_list = ['Bread', 'Milk', 'Sugar', 'Rice']

# for item in shopping_list:
#     print(f"Buy: {item}")

# print()

# # ============= Example 4: Changing an item by index
# shopping_list = ['Bread', 'Milk', 'Sugar', 'Rice']
# shopping_list[1] = 'Fresh Milk'
# shopping_list[2] = 'Sony Sugar'
# print(shopping_list)
# print()

# # ============= Example 4: Creating a list

# scores = [78, 87, 65, 43, 91] #list of numbers
# prices = [120.5, 250.0, 85.75] # list of floats
# mixed = ["Amina", 24, True, 3.14] # mixed types
# empty = [] #empty list
# nested = [[1,2,3], [4,5,6], [7,8,9]] #list of list
# #Nested indexing
# print(nested[0][1]) # What happens is python retrieves the list in index 0 which is [1, 2, 3] 
# #then in the list, it again retrieves index 1 which is 2. Therefore it returns two.

# # ======================= LIST METHODS ========================

# ''''
# Adding to a list 
#                 -append (item) adds one item to the end of the list

# '''
# students = ['Amos', 'Allan', 'Alaria', 'Alex']
# students.append('Alfred') # Adds Alfred at the end of the list
# print(students)

# students.insert(2, 'Alvin') # Adds Alvin at index 2
# print(students)

# students.extend(['Amari', 'Aiden']) #Adds them at the end of the list
# print(students)
# print("-" * 50)

# '''
# Removing from a list: 
#         .remove: Removes the first matching values
# '''
# students = ['Amos', 'Allan', 'Alaria', 'Alex', 'Alfred', 'Amari', 'Aiden']
# students.remove('Aiden') # Removes Aiden from the list
# print(students)
# print()

# last_student = students.pop() # removes and returns the last item
# print(last_student)
# print(students)
# print()

# print(students.pop(0)) # Removes index 0
# print(students)
# print()

# students = ['Amos', 'Allan', 'Aiden', 'Alaria', 'Alex', 'Alfred', 'Amari', 'Aiden']
# del students[1]
# print(students)
# print()

# students.clear() #removes all items from the list
# print(students)

# students = ['Amos', 'Allan', 'Alaria', 'Alex', 'Alfred', 'Amari', 'Aiden']
# print(students.pop(2)) #removes the item at index 2
# print(students)
# print("-" * 75)
# print() 


# '''
# Sorting a list
# '''
# students = ['Amos', 'Allan', 'Alaria', 'Alex', 'Alfred', 'Amari', 'Aiden']
# students.sort() #sorts the list in ascending order
# print(students)
# print()

# students = ['Amos', 'Allan', 'Alaria', 'Alex', 'Alfred', 'Amari', 'Aiden']
# students.sort(reverse=True) #sorts the list in descending order
# print(students)
# print()

# students = ['Amos', 'Allan', 'Alaria', 'Alex', 'Alfred', 'Amari', 'Aiden']
# students.sort(key=len) #sorts the list by length of the items
# print(students)
# print()

# students = ['Amos', 'Allan', 'Alaria', 'Alex', 'Alfred', 'Amari', 'Aiden']
# new_order = sorted(students)
# print(new_order)
# print()
# print(students) # unchanged
# print()


# students = ['Amos', 'Grace', 'Faith', 'Wanjiku', 'Brian', 'Dennis', 'Mercy']
 
# result = ' -> '.join(students)
# print(result)

# # ================= Topic 2: Slicing - Cutting out a part of a list =================

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# #indexes    0   1   2   3   4   5   6   7   8
# #indexes    -9  -8  -7  -6  -5  -4  -3  -2  -1

# #numbers [start: stop- stope before the specified index]

# print(numbers[1:4]) # prints items from index 1 to 3 - position 1 upto but not including position 4
# print()

# print(numbers[:5]) # prints items from index 0 to 4
# print()

# print(numbers[5:]) # prints items from index 5 to the end
# print()

# print(numbers[-4:-1]) # prints items from index -4 to -2
# print()

# # [start : stop : step]
# print(numbers[::2]) # basically jumping by 2: 0->2->4->6->8 
# print()

# print(numbers[::-1]) # prints the list in reverse order
# print()

# print(numbers[1:8:3]) # start at index 1, stop before index 8(7) jumping by 3: 1->4->7
# print()

# =================== Topic 3: Tuples - Immutable lists(Cannot be modified) ===================
#Uses round brackets () instead of square brackets []

# Creating and indexing a tuple

student = ('Njeri', 19, 'Kisumu')
print(student[0]) # prints the first item in the tuple
print(student[1]) # prints the second item in the tuple 

# Trying to change an item in a tuple 
#student[1] = 20 # This will raise an error because tuples are immutable

# Tuple unpacking
student = ('Njeri', 19, 'Kisumu')

name, age, city = student
print(f" {name} is {age} years old, from {city}.")

# Given the tuple dimensions = (12, 8), 
# unpack it into two variables length and width in one line, 
# then print the area (length * width).

dimensions = (12, 8)
length, width = dimensions
print(f"Area: {length * width}")
print()

# student = ("Amina Wanjiku", 24, "Data Science", 87.5), 
# storing name, age, track, and GPA in that order. 
# Unpack the tuple into four variables — name, age, track, gpa 
# — in a single line, then print each one on its own line in the format:
# Name: Amina
# Age: 24
# Track: Data Science 
# GPA: 87.5

student = ("Amina Wanjiku", 24, "Data Science", 87.5)

name, age, track, gpa = student
print(f"Name:   {name}")
print(f"Age:    {age}")
print(f"Track:  {track}")
print(f"GPA:    {gpa}")

# Tuple in a list
students = [
    ('Brian', 89),
    ('Bob', 67),
    ('Faith', 95)
]

for name, score in students:
    if score > 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    else:
        grade = 'C'

    print(f"{name}: {score} --> {grade}") 
