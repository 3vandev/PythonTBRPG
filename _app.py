from _Item import ItemClass
import _inventory
from _npc import npc_component
import _npc
import random


wooden = ItemClass("Wooden",5,0,"Old Fashioned Sword Made From a WaterLogged Stick", 100)

def purchase(item):
    if _inventory.money >= item.price:
        _inventory.money = _inventory.money - item.price
        _inventory.inv.append(item)
        print(f"You just bought {item.name} for {item.price}")
    else:
        print(f"You do not have enough money to buy {item.name}")

def dungeon(level):
    print(f"Entering Dungeon Level: {level}\n")
    print("How to play\nThe dungeon is infine and is controlled by commands\n1: attack <item to attack with>\nAttacks the enemy you are currently fighting with said weapon\n\n2: heal\nIf you have a healing potion in your inventory you are able to heal\n\n3: leave\nleaves the dungeon")
    finshed_dungeon = False
    iteration = 1
    while finshed_dungeon == False:
        iteration = iteration + 1
        npc = random.randint(0,len(_npc.enemeys) - 1)
        enemy = _npc.enemeys[npc]
        print(f"\nNow fighting: {enemy.name}")
        fight(enemy)

def fight(enemy):
    moneytoget = enemy.health * 2.5
    print(f"\nNow fighting {enemy.name}")
    while enemy.health > 0:
        enemy.attack()
        action = input("\nWHAT WILL YOU DO?:\n")
        if action == "forfeit":
            print(f"\n You Decided to forfeit against {enemy.name}")
            command()
            enemy.health = 0
        if action.startswith("attack "):
            itemtoattack = action[7::]
            weapon = None

            foundweapon = False
            iteration = 0
            if len(_inventory.inv) > 0:
                try:
                    while foundweapon == False:
                            if _inventory.inv[iteration].name == itemtoattack:
                                weapon = _inventory.inv[iteration]
                                foundweapon = True
                except:
                    print("No weapon was found")
            else:
                print("You do not have a weapon")
            if weapon == None:
                enemy.health = enemy.health - 5
                print(f"\nYou hit {enemy.name} with your fist and delt 5 damage\n{enemy.name} now has {enemy.health} health")
            else:
                enemy.health = enemy.health - weapon.damage
                print(f"\nYou hit {enemy.name} with your {weapon.name} and delt {weapon.damage}\n{enemy.name} now has {enemy.health} health")
    print(f"\nYou killed the enemy well done\n+{moneytoget} Coins")
    _inventory.money = _inventory.money + moneytoget

def fish():
    fishcaught = random.randint(0,2)
    cmd = input("Type cast when your ready to fish\n")
    if cmd == "cast":
        weight = 0
        price = 0
        if fishcaught == 0:
            weight = random.randint(6,12)
            print(f"-----\nFish: Cod\nWeight: {weight}lbs\nPrice: ${weight * 1.5}\nSize: {weight/5}cm\n-----")
            _inventory.money = _inventory.money + (weight * 1.5)
            command()
        if fishcaught == 1:
            weight = random.randint(3,100)
            print(f"-----\nFish: Salmon\nWeight: {weight}lbs\nPrice: ${weight * 1.5}\nSize: {weight/5}cm\n-----")
            _inventory.money = _inventory.money + (weight * 1.5)
            command()
        if fishcaught == 2:
            weight = random.randint(20,63)
            print(f"-----\nFish: Pike\nWeight: {weight}lbs\nPrice: ${weight * 1.5}\nSize: {weight * 2.5}cm\n-----")
            _inventory.money = _inventory.money + (weight * 1.5)
            command()
            
def command():
    cmd = input("\nInput your command here:\n")
    if cmd.startswith("buy "):
        itemtobuy = cmd[4::]
        found = False
        for i in range(0,len(_inventory.shop)):
            if _inventory.shop[i].name == itemtobuy:
                purchase(_inventory.shop[i])
                found = True
                command()
        if found == False:
            print(f"Item {itemtobuy} is not listed in the shop")
            command()
    elif cmd.startswith("dungeon "):
        level = cmd[8::]
        dungeon(int(level))
    elif cmd == "stats":
        print(f"----------\nYour Stats:\nMoney: {_inventory.money}\nHealth: {_inventory.hp}/100\nDefense: {_inventory.defense} \n----------")
        command()
    elif cmd == "help":
        print("\nTEXT RPG COMMANDS\n1: BUY <ITEM NAME>\nALLOWS YOU TO BUY AN ITEM FROM THE SHOP\n\n2: INVENTORY\nallows you to view items in your inventory\n\n3: STATS\nAllows you to view your stats\n\n4: DUNGEON <DIFFICULTY> \nTeleports you to a dungeon with a certain difficulty")
        command()
    elif cmd == "shop":
        for i in range(0,len(_inventory.shop)):
            print(f"----------\nItem{i+1}:\n{_inventory.shop[i].name}\n{_inventory.shop[i].desc}\nDamage: {_inventory.shop[i].damage}\nDefense: {_inventory.shop[i].defense}\nCosts ${_inventory.shop[i].price}\n")
        command()
    elif cmd == "inventory":
        if len(_inventory.inv) != 0:
            print(f"\nInventory: {len(_inventory.inv)}/32")
            for i in range(0,len(_inventory.inv)):
                print(f"Item {i+1}: {_inventory.inv[i].name}")
            command()
        else:
            print("0/32 Items in Inventory")
            command()
    elif cmd == "fish":
        iteration = 0
        hasFishingRod = False
        if len(_inventory.inv) < 0:
            print("\nYou cannot fish unless you have a Fishing Rod")
            command()
        else:
            for i in range(0,len(_inventory.inv)):
                if _inventory.inv[i].name == "Fishing Rod":
                    hasFishingRod = True
            if hasFishingRod == False:
                print("\nYou must have a Fishing Rod to fish")
                command()
            else:
                fish()
    else:
        print(f"{cmd} isn't a command")
        command()
command()
