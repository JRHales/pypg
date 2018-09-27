class Player:
  def __init__(self, name):
    self.name = name
    self.strength = 1
    self.vitality = 1
    self.energy = 1
    self.luck = 1
    self.agility = 1
    self.power = 1
    
    self.weaponDamage = 0
    self.attack = 1
    self.armor = 0
    self.defence = 1
    self.hitpoints = round((self.vitality+(self.strength/2)+(self.energy/3)))
  
  def setAttack(self):
    self.attack = self.strength+self.weaponDamage

  def setWeaponDamage(self, weapon):
    self.weaponDamage = weapon 
    self.setAttack()
    
  def maxHp(self):
    self.hitpoints = round((self.vitality+(self.strength/2)+(self.energy/3)))
   
  def setDefence(self):
    self.defence = self.strength+self.armor
  
  def setArmorDefence(self, armor):
    self.armor = armor
    self.setDefence()
