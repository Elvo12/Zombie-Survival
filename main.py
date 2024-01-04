from room import Room
from character import Friendly
from character import Enemy


front_door = Room("Front Door")
front_door.set_description("A grand wide door with an entry hole")

entry_hall = Room("Entry Hall")
entry_hall.set_description("A poorly lit room, with garbage on the ground")

upstairs = Room("Upstairs")
upstairs.set_description("Partially obsolete, still passable")

landing = Room("Landing")
landing.set_description("Strong stench of rotten flesh, wet and unpleasant")

hallway = Room("Hallway")
hallway.set_description("A dark and eerie hallway with two doors either side")

locked_door_left = Room("Door")
locked_door_left.set_description("The door is locked")
locked_door_right = Room("Door")
locked_door_right.set_description("The door is locked")

# kitchen = Room("Kitchen")
# kitchen.set_description("A dank and dirty room, buzzing with flies")

# ballroom = Room("Ballroom")
# ballroom.set_description("A fancy ballroom")

# dining_hall = Room("Dining Hall")
# dining_hall.set_description("A fancy dining hall")


front_door.link_room(entry_hall, "north")
entry_hall.link_room(front_door, "south")
entry_hall.link_room(upstairs, "up")
entry_hall.link_room(hallway, "north")
upstairs.link_room(entry_hall, "down")
upstairs.link_room(landing, "up")
landing.link_room(upstairs, "down")
hallway.link_room(entry_hall, "south")
hallway.link_room(locked_door_left, "west")
hallway.link_room(locked_door_right, "east")
locked_door_left.link_room(hallway, "south")
locked_door_right.link_room(hallway, "south")

# kitchen.link_room(dining_hall, "south") 
# dining_hall.link_room(kitchen, "north")
# dining_hall.link_room(ballroom, "west")
# ballroom.link_room(dining_hall, "east")






Jill = Friendly("Jill", "Very injured and dying")
Jill.set_conversation("Take this note to survive")
Jill.set_help
entry_hall.set_character(Jill)

Gregg = Enemy("Gregg", "A Smelly Zombie")
Gregg.set_conversation("Awchhhh blaacch urrrr")
Gregg.set_weakness("cheese")
Gregg.set_help
hallway.set_character(Gregg)

Roman = Enemy("Roman", "A Semi-sentient Zombie")
Roman.set_conversation("I wannn brannnnnn")
Roman.set_weakness("cheese")
Roman.set_help("you cann giiive bran to meeeh")
landing.set_character(Roman)

# Roman = Friendly("Jill", "An inZombie")
# Roman.set_conversation(" ")


current_room = front_door

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    interaction = current_room.get_character()

    if inhabitant is not None:
        inhabitant.describe()
        print("talk ,fight, help, run away") 
        command = input("\n> ")
                
        if command == "talk":   
            conversation = current_room.get_character()
            if conversation is not None:
                    conversation.talk()    

            if conversation is Jill:
                print("Jill has died")

                print("Note says:", " Cheese kills zombies.", "There are two of them around")
                print("--------------------------")
                print("\n")
                current_room.get_details()
                print("Which direction would you like to go? north, south, east, west")
                command = input("\n> ")
                if command in ["north", "south", "east", "west", "up", "down"]:
                    current_room = current_room.move(command)
                continue   

        elif command == "fight":             
            print("What will you fight with?")
            fight_with = input("\n>")
            current_character = current_room.get_character()
        
            if current_character is Jill:
                 Jill.fight(fight_with) is True
            elif current_character is not Jill:
                pass   
            
            if current_character is Gregg:
                Gregg.fight(fight_with) is True
                while True:
                    print("\n")
                    current_room.get_details()
                    interaction = current_room.get_character()
                    inhabitant = current_room.get_character()
                    print("Which direction would you like to go? north, south, east, west")
                    command = input("\n> ")
                    if command in ["north", "south", "east", "west", "up", "down"]:
                                current_room = current_room.move(command)  
                                # if inhabitant is not None:
                                #     inhabitant.describe()
                                #     print("talk ,fight, help, run away") 
                                #     command = input("\n> ")
                                            
                                if command == "talk":   
                                    conversation = current_room.get_character()
                                    if conversation is not None:
                                            conversation.talk()     
                                elif command == "fight":             
                                    print("What will you fight with?")
                                    if current_character is Roman:
                                        Roman.win(fight_with) is True
                                        break

                                elif command == "help":
                                    interaction = current_room.get_character()
                                    if interaction is not None:
                                        interaction.interact()        
                                elif command == "run away":
                                    print("You ran away, Game Over!!!")
                                    break
        elif command == "run away":
                print("You ran away, Game Over!!!")
                break
    

            # if current_character is Roman:
            #     Roman.win(fight_with) is True
            #     break

            # else:
            #     print("Game over!!!")
            #     break             
        elif command == "help":
                interaction = current_room.get_character()
                if interaction is not None:
                    interaction.interact()        

        elif command == "run away":
                print("You ran away, Game Over!!!")
                break

    else:
        print("Which direction would you like to go? north, south, east, west, up, down")
        command = input("\n> ")
        if command in ["north", "south", "east", "west", "up", "down"]:
            current_room = current_room.move(command)
    # current_room.get_details()       
    # inhabitant = current_room.get_character()
    # interaction = current_room.get_character()

    
                                              
