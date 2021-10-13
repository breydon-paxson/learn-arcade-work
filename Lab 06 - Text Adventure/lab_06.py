class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.quit = quit


def main():
    global user_choice
    room_list = []
    room_0 = Room("""The room is brightly lit with the flames from the torches.
There is a solid stone door to the north of you!
""", north=1, east=None, south=None, west=None)
    room_list.append(room_0)

    # Room 1(Stairway)
    room_1 = Room("""This room is as black as the midnight sky.
You stumble into some stairs.
All you can see is the small flicker of the candle in the middle of the stairwell.
To the south of you is a heavy stone door and towards the east you hear the wind howling!
""", north=None, east=2, south=0, west=None)
    room_list.append(room_1)

    # Room 2(outside)
    room_2 = Room("""The sun is beating down on your face, you are standing outside in a large garden.
On the north side of the castle you hear waves crashing into rocks.
On the east side of the garden you smell fresh bread baking.
If you get tired of carrying your armor just lay down by typing "q" or "quit".
""", north=3, east=4, south=None, west=1)
    room_list.append(room_2)

    # Room 3(Balcony)
    room_3 = Room("""The wind is gushing towards the castle while flowing off the ocean.
You are on a balcony that is on top of a sheer rock cliff into the ocean.
There is a large stone door to the south.
""", north=None, east=None, south=2, west=None)
    room_list.append(room_3)

    # Room 4(kitchen)
    room_4 = Room("""The smell of bread is overwhelming in the kitchen.
There are cooks running around getting ready to feed The Kingdom!
To the south there is a giant double door.
And to the west you can still hear the wind howling like a wolf.
""", north=None, east=None, south=5, west=2)
    room_list.append(room_4)

    # Room 5
    room_5 = Room("""You have no idea where you are,
the room is pitch black with no trace of light.
Going east may be dangerous with no sight.
""", north=4, east=6, south=None, west=None)
    room_list.append(room_5)

    # Room 6
    room_6 = Room("""As soon as you enter this room you are met by a cliff.
Any step but west will result in plunging toward your death!
""", north=None, east=None, south=None, west=5)
    room_list.append(room_6)

    current_room = 0

    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_choice = input("How shall you proceed? ")

        # Codes for all the rooms
        if user_choice.lower() == "north" or user_choice.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "east" or user_choice.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "south" or user_choice.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "west" or user_choice.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "quit" or user_choice.lower() == "q":
            done = True


main()
