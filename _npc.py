import random
import _inventory
class npc_component:
    name = ""
    health = 0
    damage = 0
    def __init__(self,_name,_health,_damage):
        self.name = _name
        self.damage = _damage
        self.health = _health
    def attack(self):
        attacktouse = random.randint(0,2)
        if attacktouse == 0:
            print(f"{self.name} punched you and delt {self.damage}")
            _inventory.hp = _inventory.hp - self.damage
        if attacktouse == 1:
            print(f"{self.name} kicked you and delt {self.damage}")
            _inventory.hp = _inventory.hp - self.damage
        if attacktouse == 2:
            print(f"{self.name} attemped to attack you and missed")
enemeys = [npc_component("Zombie",100,2),
           npc_component("Beast",150,5),
           npc_component("Skeleton",50,10),
           npc_component("Spider",15,3)]