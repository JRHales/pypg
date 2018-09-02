class Player:
  def __init__(self, name, strength, defence):
    self.name = name
    self.strength = strength
    self.defence = defence
    self.hitpoints = (strength+defence)*3
