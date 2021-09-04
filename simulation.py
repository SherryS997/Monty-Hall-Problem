import random

while True:
    doors = int(input("The Number of Doors for the Problem(Greater than two): "))
    if doors > 2:
        break

win_prob = round((doors-1)/doors*100, 2)

state = [0] * doors

win_door = random.randint(1,doors) - 1

state[win_door] = 1

while True:
    usr_opt = int(input("Please choose a door number: ")) - 1
    if usr_opt < doors:
        break

closed_doors = [usr_opt, win_door]

if usr_opt == win_door:
    while True:
        randdoor = random.randint(0, doors-2)
        if randdoor not in closed_doors:
            closed_doors.append(randdoor)
            break

print()
print("Monty Hall opens all doors except your door of choice and a random door. All the open doors are the wrong answers.")
print("Remember, Monty knows behind which door the right answer is.")

print("Would you like to switch?")
    
while True:
    usr_choice = int(input("Choose 1 for Switch and choose 0 for otherwise: "))
    if usr_choice in [0,1]:
        break

print()

if usr_choice == 1:
    for i in closed_doors:
        if i != usr_opt:
            new_usr_opt = i
else:
    new_usr_opt = usr_opt

if state[new_usr_opt] == 1:
    print("You win!")
else:
    print("You lose:(")

print(f"The probability of victory was {win_prob}")
print(f"The winning door was {win_door+1}")
