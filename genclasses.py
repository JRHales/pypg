class Player:
  def __init__(self, name):
    self.name = name
    self.strength = 5
    self.vitality = 5
    self.energy = 5
    self.luck = 1
    self.agility = 5
    self.power = 5
    
    self.weaponDamage = 0
    self.attack = 0
    self.armor = 0
    self.defence = 0
    self.hitpoints = round((self.vitality+(self.strength/2)+(self.energy/3)))
  
  def setAttack(self):
    self.attack = self.strength+self.weaponDamage

  def setWeaponDamage(self, weapon):
    self.weaponDamage = weapon 
    self.setAttack()
    
  def redoHp(self):
    self.hitpoints = round((self.vitality+(self.strength/2)+(self.energy/3)))
