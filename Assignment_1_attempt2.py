


import random


class Desk_Objects:

    def __init__(Self, Object, Position, Connection, Electronics, Fragile):
        Self.Item = Object
        if Position == 1:
            Self.Position = "on"
        elif Position == 2:
            Self.Position = "under"
        elif Position == 3:
            Self.Position = "next to"
        else:
            Self.Position = "not with the"
        
        if Connection == 1:
            Self.Connection = "computer on the desk"
        elif Connection == 2:
            Self.Connection = "paperwork on the desk"
        elif Connection == 3:
            Self.Connection = "clutter on the desk"
        else:
            Self.Connection = "other things laying around the room"

        if Electronics == 1:
            Self.Electronics = "needs electricity"
        else:
            Self.Electronics = "doesn't need electricity"

        if Fragile == 1:
            Self.Fragile = True
        else:
            Self.Fragile = False

    def To_String(Self):
        String = f"{Self.Item} is {Self.Position} the desk."
        String += f"\n{Self.Item} is part of the {Self.Connection}."
        String += f"\nWhen setting up you outlets, {Self.Item} {Self.Electronics}, so plan for that."
        if Self.Fragile:
            String += f"\nMake sure to not place {Self.Item} near the edge, {Self.Item} is fragile."
        return String

    def Desk_Attack(Self):
        Attacks = ["Cat", "Desk Bump", "Earthquake", "Drunk"]
        RandAttack = random.randint(0,5)
        if Self.Position == "on":
            if Self.Fragile:
                if Attacks[RandAttack] == "Cat":
                    print(f"Your cat decided to play on your desk! looks like {Self.Item} is a little damaged.")
                elif Attacks[RandAttack] == "Desk Bump":
                    print(f"Watch out! You bumped your desk, {Self.Item} could have broken.")
                elif Attacks[RandAttack] == "Earthquake":
                    print(f"That earthquake last night knocked {Self.Item} off your desk! Lets hope it's not broken")
                elif Attacks[RandAttack] == "Drunk":
                    print(f"You were pretty drunk last night, looks like you broke {Self.Item}. Got to be more careful when you drink.")
            else:
                print(f"I thought that that {Attacks[RandAttack]} was for sure going to break {Self.Item}. It's pretty sturdy.\n")

def Check_Quit(Quit):
    if Quit == 0 or Quit == "0":
        print("Thank you for using this program. Have a nice day.\n")
        quit()

def Add_To_Room():
    Item = input("\nWhat is the object:\n")
    Check_Quit(Item)
    Location = int(input("\nPress 1 if object on your desk: \n2 for under your desk: \n3 for next to your desk: \n4 if it is laying around your room:\n"))
    Check_Quit(Location)
    Piece = int(input("\nWhat purpose does the object serve? \nPress 1 for part of your computer set up: \n2 for paperwork: \n3 for clutter \n4 if it is not part of your deck set up\n"))
    Check_Quit(Piece)
    Power = int(input("\nPress 1 if it need to be plugged into an outlet: \n2 if it does not need to be plugged in:\n"))
    Check_Quit(Power)
    Break = int(input("\nPress 1 if it is fragile: \nPress 2 if it is not fragile:\n"))
    Check_Quit(Break)

    AddObject = Desk_Objects(Item, Location, Piece, Power, Break)
    return AddObject


def Main():

    Desk = {1:[], 2:[],3:[], 4:[]}

    Menu = "Press the number associated with the menu option you would like to do:\n\n"
    Menu += "1) Add an object to the room.\n"
    Menu += "2) Look at recent object.\n"
    Menu += "3) Look at the objects in the room.\n"
    Menu += "Put \"0\" in any input to exit the program.\n"

    MenuInput = ""
    Object = None

    while MenuInput != 0:
        MenuInput = input(f"{Menu}")
        try:
            MenuInput = int(MenuInput)
        except ValueError:
            print("\nPlease enter valid input.\n")
            continue
        Check_Quit(MenuInput)
        if MenuInput == 1:
            Object = Add_To_Room()
            if Object.Position == "on":
                Desk[1].append(Object.Item)
            if Object.Position == "under":
                Desk[2].append(Object.Item)
            if Object.Position == "next to":
                Desk[3].append(Object.Item)
            if Object.Position == "not with the":
                Desk[4].append(Object.Item)
        elif MenuInput == 2:
            if Object != None:
                String = Object.To_String()
                print(String)
                Object.Desk_Attack()
            else:
                print("\nNothing in the room yet. Please put objects in the room first.\n")
        elif MenuInput == 3:
            if Object == None:
                print("\nNothing in the room yet. Please put objects in the room first.\n")
            else:
                print(f"\n{Desk[4]} is/are laying around the room \n{Desk[1]} is/are on the desk\n{Desk[2]} is/are under the desk\n{Desk[3]} is/are next to the desk\n")
        else:
            print("Please enter valid input.\n")


if __name__ == "__main__":
    Main()