class ItemClass:
    damage = 0
    defense = 0
    name = ""
    desc = ""
    price = 0

    def __init__(self,_name,_damage,_defense,_desc,_price):
        self.name = _name
        self.damage = _damage
        self.defense = _defense
        self.desc = _desc
        self.price = _price

