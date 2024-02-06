def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_names = []
    for name in names:
         badge_names.append(badge_maker(name))
    return badge_names

def assign_rooms(names):
    room_names = []
    room_number = 1
    for name in names:
        room_names.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
        room_number += 1
    return room_names

def printer(names):
    badge_names = batch_badge_creator(names)

    for message in badge_names:
        print(message)

    room_assignments = assign_rooms(names)

    for assignment in room_assignments:
        print(assignment)

