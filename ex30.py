people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")

elif cars < people:
    print("not taking the car")

else:
    print("Can't decide")


if trucks > cars:
    print("That's too many trucks")

elif trucks < cars:
     print("could take the car")

else:
     print("can't decide")

if people > trucks:
    print("let's take the car")
else:
    print("stay home")
