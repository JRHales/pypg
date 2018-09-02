class Player:
  def __init__(self, name, strength):
    self.name = name
    self.strength = strength
    self.weaponDamage = 0
    self.attack = 0
    self.armor = 0
    self.defence = 0
    self.hitpoints = (strength+(strength/2))*3
  
  def setAttack(self):
    self.attack = self.strength+self.weaponDamage

  def setWeaponDamage(self, weapon):
    self.weaponDamage = weapon 
    self.setAttack()
