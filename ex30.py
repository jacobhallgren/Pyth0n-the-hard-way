people = 30
cars = 40
trucks = 15

print(people < cars)


if cars > people: 
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars")
else: 
    print("We cant't decide")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars: 
    print("Maybe we could take trucks")

else: 
    print("We still cant't deice.")


if people > trucks: 
    print ("Allright, lets just take the trucks")

else: 
    print("Fine, lets stay home then.")


