
restaurant = 'starting'
burgers = 0
game_running = True

while game_running:

    if restaurant == 'starting':
        print("You find yourself in a beautiful restaurant.")
        print("To your left, a giant door with two burger slots.")
        print("To your right, a large, cavernous kitchen.")
        print("Enter '1' to unlock the door. Enter '2' to enter the big room.")

        answer = input("1-2: ")

        if answer == "1":
            restaurant = "door"
        elif answer == "2":
            restaurant = "big"
        else:
            print("Are you a bit slow in the head?? choose again ")

    elif restaurant == "door":

        if burgers >= 2:
            print("You win!")
            game_running = False
        else:
            print("You need two burgers to get through this door, but you only have " + str(burgers) + "!")
            restaurant = 'starting'

    elif restaurant == "big":
        print("You have entered the massive room.")
        print("To your left, you see a physics equation.")
        print("To your right, you see a geometry problem.")
        print("Enter '1' for physics, '2' for geometry, '3' to go back.")

        answer = input("1-3: ")

        if answer == "1":
            restaurant = "physics"
        elif answer == "2":
            restaurant = "math"
        elif answer == "3":
            restaurant = "starting"
        else:
            print("Are you a bit slow in the head?? choose again ")

    elif restaurant == "physics":
        print("You see in front of you the following puzzle:")
        print("What is the height of a person such that when a stone")
        print("is dropped from his head to the ground, the time taken is 2.4 seconds?")
        print("Assume the person is at the surface of Earth.")

        print("Choose your answer below:")
        print("a: 28m")
        print("b: 30m")
        print("c: 44.5m")
        print("d: 15m")

        answer = input().lower()

        if answer == "b" or answer == "c" or answer == "d":
            print("That is incorrect. Get better!")
            restaurant = "big"

        elif answer == "a":
            print("That is absolutely correct! You get 1 burger.")
            burgers += 1
            restaurant = "big"

        else:
            print("Are you a bit slow in the head?? choose again ")

    elif restaurant == "math":
        print("You see a geometry problem.")
        print(" What is the circumference of circle with area 156m square . assume that the value of pi= 3.14")

        answer = input("type your  answer").strip().lower()

        if answer == "seventyeight":
            print("corret answer. expected if you are asian to be honest")
            burgers += 1
            restaurant = "big"
        else:
            print("You are actually dumb unless you are a 6th grader which you clearly arent")
            restaurant = "big"

