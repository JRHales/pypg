
# Partially tested

class Player:
  
  def __init__(self, name):
    self.name = name
    self.strength = 1
    self.vitality = 1
    self.energy = 1
    self.luck = 1
    self.agility = 1
    self.power = 1
    self.exp = 0
    self.level = 1
    
    self.weaponDamage = 0
    self.attack = 1
    self.armor = 0
    self.defence = 1
    self.hitpoints = round((self.vitality+(self.strength/2)+(self.energy/3)))
  
  def setAttack(self, weaponVal):
    self.weaponDamage = weaponVal
    self.attack = self.strength+self.weaponDamage
    
  def setMaxHp(self): # use to update max HP
    self.hitpoints = round((self.vitality+(self.strength/2)+(self.energy/3)))
   
  def setDefence(self,  armorVal):
    self.armor = armorVal
    self.defence = self.strength+self.armor
    
  def getName():
    return self.Name
  
#End Player Class ---------------------------------------------------------------
class Monster:
  
  def __init__(self, name, strength, vitality, energy, agility, power, attack, defence):
    self.name = name
    self.strength = 1
    self.vitality = 1
    self.energy = 1
    self.agility = 1
    self.power = 1
    self.attack = 1
    self.defence = 1
    self.hitpoints = round((self.vitality+(self.strength/2)+(self.energy/3)))
    
#End Monster Class ----------------------------------------------------------------------
