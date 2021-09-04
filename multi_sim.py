import random
    

sims = int(input("No of simulations: "))

while True:
    doors = int(input("No of doors(Greater than two): "))
    if doors > 2:
        break

switch = bool(int(input("Should you switch?(Answer Yes as 1 and No as 0): ")))
counter = 0
    
def simulation(doors, switch):
    win_door = random.randint(1,doors) - 1
    usr_opt = random.randint(1,doors) - 1

    closed_doors = [usr_opt, win_door]

    if usr_opt == win_door:
        while True:
            randdoor = random.randint(0, doors-2)
            if randdoor not in closed_doors:
                closed_doors.append(randdoor)
                break


    if switch:
        for i in closed_doors:
            if i != usr_opt:
                new_usr_opt = i
    else:
        new_usr_opt = usr_opt


    if new_usr_opt == win_door:
        return True
    else:
        return False



for i in range(sims):
    if simulation(doors, switch):
        counter += 1

print(f"\nThe number of victories was {counter}")
print(f"The percentage of victories was {round((counter/sims)*100, 2)}")