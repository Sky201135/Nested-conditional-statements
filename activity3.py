print("select your ride option:")
print("1. Bike")
print("2. Car")
print("3. Bus")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("what type of bike is it")
    print("1. motorbike\n")
    print("2. bicycle\n")
    print("3. scooter\n")

    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected motorbike")
    elif choice2 == 2:
        print("You have selected bicycle")
    else:
        print("You have selected a scooter")

elif choice == 2:
    print("what type of car is it")
    print("1. sedan\n")
    print("2. suv\n")
    print("3. truck\n")

    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected sedan")
    elif choice2 == 2:
        print("You have selected suv")
    else:
        print("You have selected truck")

elif choice == 3:
    print("what type of bus is it")
    print("1. school bus\n")
    print("2. city bus\n")
    print("3. shuttle bus\n")

    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected school bus")
    elif choice2 == 2:
        print("You have selected city bus")
    else:
        print("You have selected shuttle bus")

else:
    print("Invalid choice")