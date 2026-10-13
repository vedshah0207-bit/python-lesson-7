print("Select your ride\nType 1 for bike\nType 2 for car")
choice = int(input(""))

if choice == 1:
    print("What type of bike\nType 1 for scooty\nType 2 for scooter")
    bike_choice = int(input(""))
    if bike_choice == 1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")
elif choice == 2:
    print("What type of car\nType 1 for SUV\nType 2 for sedan")
    car_choice = int(input(""))
    if car_choice == 1:
        print("You have selected SUV")
    else:
        print("You have selected sedan")
else:
    print("Please choose one of the options given.")