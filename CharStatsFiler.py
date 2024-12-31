class Character :
    def __init__(self, charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = ''):
        #individuials name(s)
        self.charName = charName
        #dwarf, dragon, goblin, etc.
        self.race = race
        #paladin, ranger, wizard, etc.
        self.abilityClass = abilityClass
        #stands for background
        self.bkgrd = bkgrd
        #strengths/talents
        self.strength = strength
        #weaknesses, both phyisical and phycological
        self.weakness = weakness
        #brief-ish discription of the character's appearance
        self.disc = disc
        #brief-ish discription of the character's personality
        self.persona = persona
        #eqipment, duh!
        self.equip = equip
        
    #defining the mutator methods (setters)
    def set_name(self, charName) :
        self.charName = charName
        
    def set_race(self, race) :
        self.race = race
        
    def set_Class(self, abilityClass) :
        self.abilityClass = abilityClass
        
    def set_bkgrd(self, bkgrd) :
        self.bkgrd = bkgrd
        
    def set_strength(self, strength) :
        self.strength = strength
        
    def set_weakness(self, weakness) :
        self.weakness = weakness
        
    def set_disc(self, disc) :
        self.disc = disc
        
    def set_persona(self, persona) :
        self.persona = persona
        
    def set_equip(self, equip) :
        self.equip = equip
    
    #defining the accesor methods (getters)    
    def get_name(self) :
        return self.charName
    
    def get_race(self) :
        return self.race
    
    def get_Class(self) :
        return self.abilityClass
    
    def get_bkgrd(self) :
        return self.bkgrd
    
    def get_strength(self) :
        return self.strength
    
    def get_weakness(self) :
        return self.weakness   
    
    def get_disc(self) :
        return self.disc
    
    def get_persona(self) :
        return self.persona
    
    def get_equip(self) :
        return self.equip

#making subclasses

#class player(Character) :
    #def __init__(self, charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '', NEWATTRIBUTE = '') :
        #super().__init__(charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '')
        #self.NEWATTRIBUTE = NEWATTRIBUTE
    
    #def set_NEWATTRIBUTE(self, NEWATTRIBUTE) :
        #self.NEWATTRIBUTE = NEWATTRIBUTE
        
    #def get_NEWATTRIBUTE(self) :
        #return self.NEWATTRIBUTE

class player(Character) :
    def __init__(self, charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '', playerName = '') :
        super().__init__(charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '')
        self.playerName = playerName
    
    def set_playerName(self, playerName) :
        self.playerName = playerName
        
    def get_playerName(self) :
        return self.playerName

class npc(Character) :
    def __init__(self, charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '', attitude = '') :
        super().__init__(charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '')
        self.attitude = attitude
    
    def set_attitude(self, attitude) :
        self.attitude = attitude
        
    def get_attitude(self) :
        return self.attitude
    
class enemy(Character) :
    def __init__(self, charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '', challenge = '') :
        super().__init__(charName = '', race = '', abilityClass = '', bkgrd = '', strength = '', weakness = '', disc = '', persona = '', equip = '')
        self.challenge = challenge
    
    def set_challenge(self, challenge) :
        self.challenge = challenge
        
    def get_challenge(self) :
        return self.challenge

#actually use the class:

def main():
    
    def getCharType() :
        charType = (input('Please choose which type of character (type 1 for a player character, 2 for an npc, 3 for an enemy/opponent/villian, or 4 to view previously made characters in this directory)'))

        if charType == '1' :
            char = player(Character)
            char.set_playerName(input("Player's name: "))
            print(f'Wait, did you say "{char.get_playerName()}"?')
        
        elif charType == '2' :
            pass
        
        elif charType == '3' :
            pass
        
        elif charType == '4' :
            pass
        
        else :
            pass
    
    getCharType()

    #print(f'Status: {char.get_status()}')

main()
