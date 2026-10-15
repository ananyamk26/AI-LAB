room = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


print("Initial State:")
print(room)

for i in range(6):
    print("\nCurrent Location:", location)
    print("Room Status:", room[location])

    action = simple_reflex_agent(location, room[location])
    print("Action:", action)

    if action == "Suck":
        room[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

print("\nFinal State:")
print(room)
