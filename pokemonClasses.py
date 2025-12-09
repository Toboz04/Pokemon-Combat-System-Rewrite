class Pokemon:
    def __init__(self, id, name, species, description, type1, type2, height, weight, image, critchance, rarity, basestats, currenthp, attacks, statusalignments):
        self.id = int(id)
        self.name = str(name)
        self.species = str(species)
        self.description = str(description)
        self.type1 = str(type1)
        self.type2 = str(type2)
        self.height = str(height)
        self.weight = str(weight)
        self.image = str(image)
        self.critchance = int(critchance)
        self.rarity = str(rarity)
        self.basestats = basestats
        self.currenthp = int(currenthp)
        self.attacks = list(attacks)
        self.statusalignments = list(statusalignments)
        
    def p_attack(self, attack, attackingpokemon, defendingpokemon):
        print(f"{attackingpokemon.name} used {attack.name}!")
        if attack.attack_type == "physical":
            damage_count = Attack.calc_damage(1, attack.type, attackingpokemon.type1, attackingpokemon.type2, 1,
                                            attack.base_power, attackingpokemon.basestats.attack,
                                            defendingpokemon.basestats.defense, attackingpokemon.critchance, random.randint(85, 100),
                                            defendingpokemon.type1, defendingpokemon.type2)
        elif attack.attack_type == "status":
            if attack.secondary_effect.immunity == defendingpokemon.type1 or attack.secondary_effect.immunity == defendingpokemon.type2:
                print(f"{defendingpokemon.name} is immune!")
                damage_count = 0
            else:
                if attack.secondary_effect in defendingpokemon.statusalignments:
                    print(f"{defendingpokemon.name} is already poisoned!")
                    damage_count = 0
                else:
                    defendingpokemon.statusalignments.append(attack.secondary_effect)
                    print(f"{defendingpokemon.name} got {attack.secondary_effect.name}!")
                    damage_count = 0
        return damage_count

    def p_change_current_active(self, pokemonlist):
        while True:
            print(f"Which pokemon do you want to choose?")
            i = -1
            for x in pokemonlist:
                i += 1
                print(f"({i}) {x.name}")
            try:
                pokemonChoice = int(input())
            except ValueError:
                print("Invalid input!")
                continue
            if pokemonChoice > i:
                print("Invalid input!")
                continue
            else:
                currentPokemon = pokemonlist[pokemonChoice]
                return currentPokemon


      
class BaseStats:
    def __init__(self, hp, attack, defense, speed):
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.speed = int(speed)
        


class Attack:
    def __init__(self, attack_id,attack_type, name, type, base_power, accuracy, pp, secondary_effect):
        self.attack_id = int(attack_id)
        self.attack_type = str(attack_type)
        self.name = str(name)
        self.type = str(type)
        self.base_power = int(base_power)
        self.accuracy = float(accuracy)
        self.pp = int(pp)
        self.secondary_effect = secondary_effect

    def calc_damage(self, attacktype, attackertype1, attackertype2, level, basedmg, attack, defense, critchance, randint, type1, type2):
        effectiveness = 0
        try:
            if types[type1].effectiveness_defense[attacktype] == "weak":
                damageType1 = 2
                effectiveness += 1
            elif types[type1].effectiveness_defense[attacktype] == "resistant":
                damageType1 = 0.5
                effectiveness -= 1
            elif types[type1].effectiveness_defense[attacktype] == "no effect":
                damageType1 = 0
        except KeyError:
            damageType1 = 1
        try:
            if types[type2].effectiveness_defense[attacktype] == "weak":
                damageType2 = 2
                effectiveness += 1
            elif types[type2].effectiveness_defense[attacktype] == "resistant":
                damageType2 = 0.5
                effectiveness -= 1
            elif types[type2].effectiveness_defense[attacktype] == "no effect":
                damageType2 = 0
        except KeyError:
            damageType2 = 1
        if attacktype == attackertype1:
            STAB = 1.5
        elif attacktype == attackertype2:
            STAB = 1.5
        else:
            STAB = 1
        critCalculator = random.randint(critchance, 100)
        if critCalculator == 100:
            crit = 2
            print("It's a crit!")
        else:
            crit = 1
        damage = ((level * 2/5 + 2) * basedmg * ((attack + (level * 10)) / (50 * defense)) + 2 ) * crit * (randint / 100) * STAB * damageType1 * damageType2
        if effectiveness == 1:
            print("It's very effective")
        elif effectiveness == 2:
            print("It's EXTREMELY effective")
        elif effectiveness == -1:
            print("It's not effective")
        elif effectiveness == -2:
            print("It's EXTREMELY ineffective")
        elif damageType1 == 0 or damageType2 == 0:
            print("It has no effect")
        return int(damage)
    


class Status:
    def __init__(self, name, dpr, duration, immunity):
        self.name = str(name)
        self.dpr = dpr
        self.duration = int(duration)
        self.immunity = str(immunity)



class Type:
    def __init__(self, name, effectiveness_attack, effectiveness_defense):
        self.name = str(name)
        self.effectiveness_attack = dict(effectiveness_attack)
        self.effectiveness_defense = dict(effectiveness_defense)