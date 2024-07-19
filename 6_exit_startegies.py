# there are 3 ways to exit a while loop 

# Break condition, Flags, control variable state 

#--- Break, terminate the loop permaturly

while True:
    fave_food = input("What's your favorite food?")

    if fave_food == 'tacos':
        print("That is correct, well done. Enjoy the fiesta!!")
        break
    else:
        print("WRONG ANSWER, TRY AGAIN!!")

print('='*50)

#-- FLAG : allows the rest of the code block to execute, but terminates the loop afterward

searching = True 
hours = 0

while searching:
    found = input("Has anyone found my keys? ")
    if found == 'yes':
        searching = False
    hours += 1
    if not searching:
        print("Thanks you for all your help in finding my keys") 
        print("It only took", hours, "hours")


#--- Control Variable : Change this condition to eventually be False 

count = 0 

while count <= 10:
    print("Running my code!", count)
    count += 2

# print(count)