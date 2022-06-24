def gymlog():
    if day == 1:
        var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/gymlogs/Push/'
        var2 = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Push Day.txt'
    elif day == 2:
        var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/gymlogs/Pull/'
        var2 = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Pull Day.txt'
    elif day == 3:
        var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/gymlogs/Legs/'
        var2 = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Leg Day.txt'
    date = var + str(input('Enter the date MM.DD.YYYY format: \n')) + '.txt'
    with open(date, 'w') as logwrite:
        pushday = open(var2, 'r')
        for y in pushday:
            print(y)
            reps = input('Weight per set: ')
            logwrite.write(y)
            logwrite.write(reps)
            logwrite.write('\n')
    logwrite.close()
    pushday.close()
def gymremove():
    with open('C:/Users/joosi/OneDrive/Desktop/GymApp/temp.txt', 'w') as tempcopy:
        if day == 1:
            var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Push Day.txt'
        elif day == 2:
            var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Pull Day.txt'
        elif day == 3:
            var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Leg Day.txt'
        with open(var, 'r') as dayedit:
            for y in dayedit:
                print(y)
                remove = int(input('Remove? \n 1. Yes \n 2. No \n'))
                if remove == 1:
                        continue
                if remove == 2:
                    tempcopy.write(y)
    dayedit.close()
    tempcopy.close()
    with open(var, 'w') as dayrevise:
        tempwrite = open('C:/Users/joosi/OneDrive/Desktop/GymApp/temp.txt', 'r')
        for y in tempwrite:
            dayrevise.write(y)
    tempwrite.close()
    dayrevise.close()
def gymadd():
    if day == 1:
        var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Push Day.txt'
    elif day == 2:
        var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Pull Day.txt'
    elif day == 3:
        var = 'C:/Users/joosi/OneDrive/Desktop/GymApp/Leg Day.txt'
    with open(var, 'a') as dayadd:
        workoutadd = input('Enter the name of the workout, sets, and reps (Ex(0x0)): \n')
        dayadd.write('\n' + workoutadd)
    dayadd.close()
print('Welcome to your workout logger & planner')
choice = int(input('Will you: \n 1. Log a workout \n 2. Edit a workout \n 3. View maxes \n'))
#Logs a workout session for either push, pull, or leg day
if choice == 1:
    day = int(input('Did you do \n 1. Push \n 2. Pull \n 3. Legs \n'))
    gymlog()
#Allows the user to edit a workout, located in a .txt file, by adding or removing exercises from the routine
elif choice == 2:
    day = int(input('Which day would you like to edit: \n 1. Push \n 2. Pull \n 3. Legs \n'))
    addremove = int(input('Would you like to \n 1. Remove Workout \n 2. Add Workout'))
    if addremove == 1:
        gymremove()
    if addremove == 2:
        gymadd()
#User can compare max-outs from different files for different exercises, separated by push, pull, or leg days
elif choice == 3:
    print('Under Construction')