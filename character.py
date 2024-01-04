class Character():
    def __init__(self,char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.help = None

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_help(self, help):
        self.help = help

    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says :{self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def interact(self):
        if self.help is not None:
            print(f"{self.name} says : {self.help}")
        else:
            print(f"You cannot help {self.name}")
    
    def fight(self,combat_item):
        print(f"{self.name} does not want to fight you.")
        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.char_weakness =  None
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
        self.help = None
   
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off, using {combat_item}.")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            print("Game Over!!!")
            return False
        
    def win(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off, using {combat_item},")
            print("Game End!!")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer! ")
            return False
        
    def set_help(self, help):
        self.help = help

    def interact(self):
        if self.help is not None:
            print(f"{self.name} says : {self.help}")
        else:
            print(f"You cannot help {self.name}")
            
            
class Friendly(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.char_weakness = None
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    # def fight(self,combat_item):
    #     print(f"{self.name} does not want to fight you.")
    #     return True
        
    # def interact(self):
    #     if self.help is None:
    #         print(f"You cannot help {self.name}") 
    #     else:
    #         print(f"{self.name} says : {self.help}")
       
    # def interact(self):
    #     if self.help is None:
    #         print(f"It is too late to help {self.name}")  
    # def fight(self,combat_item):
    #     print(f"{self.name} does not want to fight you.")
    #     return True