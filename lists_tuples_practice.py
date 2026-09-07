# --------------------------------- Lists --------------------------------

# Q1. You have a list of fruits: ['Mango', 'Banana', 'Orange']. Add 'Pineapple' to the end using append(), 
# then add 'Apple' as the second item using insert(). Print the updated list and the total number of fruits.

fruits = ['Mango', 'Banana', 'Orange']
print(fruits)

fruits.append('Pineapple')
fruits.insert(1, 'Apple')
print(fruits)
print(len(fruits))

print(">" * 50)
print()

# Q2. Given a list of cities: ['Nairobi', 'Kisumu', 'Mombasa', 'Nakuru', 'Eldoret'],
#  use indexing to print the first city, the last city, 'Mombasa' using positive indexing, 
# and 'Nakuru' using negative indexing.

cities = ['Nairobi', 'Kisumu', 'Mombasa', 'Nakuru', 'Eldoret']
print(cities)
print()

print(cities[0])
print(cities[4])
print(cities[2])
print(cities[-2])

print(">" * 50)
print()

# Q3. You have a list of subjects: ['Math', 'English', 'Science', 'History']. 
# Change 'English' to 'Kiswahili' and 'History' to 'Geography' using indexing, then print the updated list.

subjects = ['Math', 'English', 'Science', 'History']
print(subjects)
print()

subjects[1] = 'Kiswahili'
subjects[3] = 'Geography'
print(subjects)

print(">" * 50)
print()
# Q4. Given a shopping list: ['Bread', 'Milk', 'Sugar', 'Rice', 'Eggs'], use remove() to remove 'Sugar', 
# then use pop() to remove the last item. Print the resulting list.

shopping_list = ['Bread', 'Milk', 'Sugar', 'Rice', 'Eggs']
print(shopping_list)

shopping_list.remove('Sugar')
print(shopping_list.pop()) 
#print(shopping_list.pop(3)) - Another way to remove last item
print(shopping_list)

print(">" * 50)
print()

# Q5. Given the list numbers = [10, 20, 30, 40, 50, 60, 70, 80], use slicing to print: the first 4 numbers,
#  the last 3 numbers, [20, 30, 40], every second number, and the list in reverse order.

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# print: the first 4 numbers
print(numbers[:4])
print(numbers[0:4])
print()
# the last 3 numbers
print(numbers[5:8])
print(numbers[-3:])
print()
#[20, 30, 40]
print(numbers[1:4])
print()
#every second number
print(numbers[1::2])
print()
#the list in reverse order
print(numbers[::-1])

print(">" * 50)
print()

# ------------------------- Lists • Loops -------------------------------
# Q6. You have a shopping list: ['Bread', 'Milk', 'Sugar', 'Rice']. Use a for loop to print each item in the format
#  'I need to buy Bread'.

shopping_list = ['Bread', 'Milk', 'Sugar', 'Rice']

for item in shopping_list:
    print(f"I need to buy {item}")

print(">" * 50)
print()

# Q7. Given the list numbers = [12, 7, 25, 4, 18, 30, 9], use a for loop to print only the numbers that 
# are greater than 10.

numbers = [12, 7, 25, 4, 18, 30, 9]

plus_ten = [number for number in numbers if number > 10]
print(plus_ten)

#Alternative

# for number in numbers:
#     if number > 10:
#         print(number)
    
print(">" * 50)
print()

# Q8. Given the list numbers = [10, 15, 22, 31, 44, 57, 60], 
# use a for loop to create a new list containing only the even numbers.

numbers = [10, 15, 22, 31, 44, 57, 60]

even_numbers = [number for number in numbers if (number%2) == 0 ]
print(even_numbers)

#Alternative

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)

print(">" * 50)
print()

# Q9. You have a list of scores: [45, 78, 92, 33, 67, 88, 21]. 
# Using a loop, count how many students passed (50 or above) and how many failed. Print both totals.

scores = [45, 78, 92, 33, 67, 88, 21]

passed = 0
fail = 0

for score in scores:
    if score >= 50:
        passed += 1
    else:
        fail += 1
print(f"Passed: {passed}")
print(f"Failed: {fail}")

print(">" * 50)
print()

# Q10. You have a list of prices: [100, 250, 75, 300, 150]. Use a for loop to calculate the total price.
#  Do not use sum().

prices = [100, 250, 75, 300, 150]

total = 0

for price in prices:
    total += price

print(f"Total is {total}")

print(">" * 50)
print()

# ------------------------------ Tuples ------------------------------------
# Q11. Create a tuple called person containing ('Charleen', 20, 'Kenya', 'Computing'). 
# Print the name, age, country, and course using indexing only.

person = ('Charleen', 20, 'Kenya', 'Computing')
print(person[0])
print(person[1])
print(person[2])
print(person[3])

print(">" * 50)
print()

# Q12. Given the tuple student = ('Brian', 85), unpack it into two variables, name and score, in one line. 
# Then print 'Brian scored 85'.

student = ('Brian', 85)

name, score = student
print(f"{name} scored {score}")

print(">" * 50)
print()
# Q13. Given the tuple coordinates = (-1.286389, 36.817223), unpack it into latitude and longitude,
#  then print each value with a suitable label.

coordinates = (-1.286389, 36.817223)
latitude, longtitude = coordinates

print(f"Latitude is: {latitude}")
print(f"Longtitude is: {longtitude}")

print(">" * 50)
print()

# Q14. Given the tuple dimensions = (15, 8), unpack it into length and width in one line. 
# Calculate and print the area and perimeter.

dimensions = (15, 8)

length, width = dimensions
print(f"Area is {length * width}")

# perimeter= 2 * (length + width)
print(f"Perimeter is {2 * (length + width)}")

print(">" * 50)
print()

# ----------------------- Lists • Tuples ---------------------
# Q15. A list contains three tuples representing students and their scores: 
# [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88)]. 
# Loop through the list and print each student's name and score in the format 'Amos scored 78'. 
# (Hint: unpack each tuple directly in the for line.)

students = [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88)]

for name, score in students:
    print(f"{name} scored {score}")

print(">" * 50)
print()

# Q16. Using the same list of students and scores, loop through the list 
# and print only the students who scored 70 or above.

students = [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88)]

for name, score in students:
    if score >= 70:
        print(name)

print(">" * 50)
print()

# Q17. A list contains the following students and scores:
# [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88)]. 
# Use a loop to find and print the student with the highest score. Do not use max().

students = [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88)]

highest_score = 0
highest_student = ""

for name, score in students:
    if score > highest_score:
        highest_score = score
        highest_student = name
print(f"{highest_student} has the highest score of {highest_score}")

print(">" * 50)
print()

# Q18. Using the same list, use a loop to calculate and print the average score. Do not use sum().

students = [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88)]

total = 0

for name, score in students:
    total += score

avg = total / len(name)
print(f"Average score is {avg}")

print(">" * 50)
print()

# ------------------------ Lists • Tuples • Conditionals -----------------------------------
# Q19. A list contains five students and their scores: 
# [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88), ('Amina', 45)]. 
# Loop through the list and assign grades using these rules: 80+ = A, 70-79 = B, 50-69 = C, below 50 = D.
#  Print each student's name, score, and grade in the format 'Amos: 78 --> B'.

students = [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88), ('Amina', 45)]

for name, score in students:
    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'D'

    print(f"{name}: {score} --> {grade}")

print(">" * 50)
print()

# Q20. Using the same list of students and scores, create two empty lists called passed and failed. 
# Loop through the students and place students who scored 50 or above into passed and everyone else into failed. 
# Print both lists.

students = [('Amos', 78), ('Faith', 92), ('Brian', 65), ('Grace', 88), ('Amina', 45)]

passed = []
failed = []

for name, score in students:
    if score >= 50:
        passed.append(name)
    else:
        failed.append(name)
print(f"Passed: {passed}")
print(f"Failed: {failed}")

print(">" * 50)
print()

# ------------------------------------ Challenge --------------------------------------------
# Q21. A shop has a list of products and prices: 
# [('Bread', 60), ('Milk', 70), ('Sugar', 150), ('Rice', 200)]. 
# Loop through the list and calculate the total cost. Print the total.

stock = [('Bread', 60), ('Milk', 70), ('Sugar', 150), ('Rice', 200)]

total = 0

for product, price in stock:
    total += price
print(f"Total cost is Ksh.{total}")

print(">" * 50)
print()

# Q22. Using the same product list, loop through it and print only the products that cost more than 100, 
# in the format 'Sugar: 150'.

stock = [('Bread', 60), ('Milk', 70), ('Sugar', 150), ('Rice', 200)]

for product, price in stock:
    if price > 100:
        print(f"{product}: {price}")

print(">" * 50)
print()

#Another way to go about it

stocks = [('Bread', 60), ('Milk', 70), ('Sugar', 150), ('Rice', 200)]

plus_hundred = [(product,price) for (product,price) in stocks if price > 100]

for product, price in plus_hundred:
    print(f"{product}: {price}")

print(">" * 50)
print()

# Q23. A shop has the following products and prices: [('Bread', 60), ('Milk', 70), ('Sugar', 150), ('Rice', 200)].
#  Apply a 10% discount to every product and print the product name and discounted price.

stocks = [('Bread', 60), ('Milk', 70), ('Sugar', 150), ('Rice', 200)]

discount = 0.9

for product, price in stocks:
    amount = discount * price
    print(f"{product}: {amount}")

print(">" * 50)
print()

# Q24. Using the same product list, use a loop to find and print the cheapest product and its price. Do not use min().

stocks = [('Bread', 60), ('Milk', 70), ('Sugar', 150), ('Rice', 200)]

cheapest_product = ""
cheapest_price = 0

for product, price in stocks:
    if cheapest_price == 0 or price < cheapest_price:
        cheapest_price = price
        cheapest_product = product
print(f"Cheapest product is {cheapest_product} and price is {cheapest_price}")

print(">" * 50)
print()

# Q25. A list contains three students, each with a name and a list of three scores: 
# [['Amos', [78, 85, 90]], ['Faith', [92, 88, 95]], ['Brian', [65, 70, 60]]]. 
# Use loops and indexing to print each student's name and all three scores. 
# Then calculate each student's average score.

students = [['Amos', [78, 85, 90]], ['Faith', [92, 88, 95]], ['Brian', [65, 70, 60]]]

for student in students:
    name = student[0]
    scores = student[1]

    print(f"{name}: {scores}")

    total = 0

    for score in scores:
        total += score
        avg = total / len(scores)

    print(f"Average score: {avg}")
    print()

print(">" * 50)
print()

# Q26. CHALLENGE: Using the nested student list from Q25,
#  calculate each student's average score and assign a grade using these rules:
#  80+ = A, 70-79 = B, 50-69 = C, below 50 = D. Print each student's name, average, and grade. 
#Use a loop, list indexing, another loop for the scores, and a conditional.


students = [['Amos', [78, 85, 90]], ['Faith', [92, 88, 95]], ['Brian', [65, 70, 60]]]

for student in students:
    name = student[0]
    scores = student[1]

    total = 0

    for score in scores:
        total += score
    avg = total / len(scores)
    # print(avg)

    if avg >= 80:
        grade = 'A'
    elif avg >= 70:
        grade = 'B'
    elif avg >= 50:
        grade = 'C'
    else:
        grade = 'D'

    print(f"Name: {name}")
    print(f"Average: {avg}")
    print(f"Grade: {grade}")
    print()

print(">" * 50)
print()
