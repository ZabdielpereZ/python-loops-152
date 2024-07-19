# List Comprehension are inline loops that produce a list

# syntax
# var = [<added item> for item in iterable]

# list comprehension with a simple for loop
students = [1,2,3]

shirt_list = [num * 2 for num in students] # one-line for loop
print(shirt_list)

other_list = []
for num in students:
    other_list.append(num * 2) 

print(other_list)

print('='*50)

# list comprehension with if statement

# syntax
# var = [<added item> for item in iterable if (conditio)]

nums = [1,2,3,4,5,6]

evens = [num + 2 for num in nums if num % 2 == 0] # one-line of code
print(evens)

even2 = []
for num in nums:
    if num % 2 == 0:
        even2.append(num)  #four lines of code
print(evens)

print('='*50)

# List comprehension with 'if' and 'else'

# syntax
# var = [<if True add> if (condition) else <else add> for item in iterable]

grades = [100, 98, 52, 87, 98, 68]

pass_fail = ['pass' if grade >= 70 else 'fail' for grade in grades]
print(pass_fail)
