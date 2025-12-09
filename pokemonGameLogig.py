import random

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

class CommonPokemon(Pokemon):
    pass

class RarePokemon(Pokemon):
    pass

class EpicPokemon(Pokemon):
    pass

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

normal = Type(
    'normal',
    effectiveness_attack = {
        "rock" : "ineffective",
        "ghost" : "no effect"
    },
    effectiveness_defense = {
        "fighting" : "weak",
        "ghost" : "no effect"
    }
)

grass = Type(
    "grass",
    effectiveness_attack = {
        "grass" : "ineffective",
        "fire" : "ineffective",
        "water" : "effective",
        "flying" : "ineffective",
        "poison" : "ineffective",
        "ground" : "effective",
        "rock" : "effective",
        "bug" : "ineffective",
        "dragon" : "ineffective"
    },
    effectiveness_defense = {
        "grass" : "resistant",
        "fire" : "weak",
        "water" : "resistant",
        "electric" : "resistant",
        "flying" : "weak",
        "poison" : "weak",
        "ground" : "resistant",
        "bug" : "weak",
        "ice" : "weak"
    }
)

fire = Type(
    'fire',
    effectiveness_attack = {
        "grass" : "effective",
        "fire" : "ineffective",
        "water" : "ineffective",
        "rock" : "ineffective",
        "bug" : "effective",
        "ice" : "effective",
        "dragon" : "ineffective"
    },
    effectiveness_defense = {
        "grass" : "resistant",
        "fire" : "resistant",
        "water" : "weak",
        "ground" : "weak",
        "rock" : "weak",
        "bug" : "resistant"
    }
)

water = Type(
    'water',
    effectiveness_attack = {
        "grass" : "ineffective",
        "fire" : "effective",
        "water" : "ineffective",
        "ground" : "effective",
        "rock" : "effective",
        "dragon" : "ineffective"
    },
    effectiveness_defense = {
        "grass" : "weak",
        "fire" : "resistant",
        "water" : "resistant",
        "electric" : "weak",
        "ice" : "resistant"
    }
)

bug = Type(
    "bug",
    effectiveness_attack = {
        "grass" : "effective",
        "fire" : "ineffective",
        "fighting" : "ineffective",
        "flying" : "ineffective",
        "poison" : "effective",
        "psychic" : "effective",
        "ghost" : "ineffective"
    },
    effectiveness_defense = {
        "grass" : "resistant",
        "fire" : "weak",
        "fighting" : "resistant",
        "flying" : "weak",
        "poison" : "weak",
        "ground" : "resistant",
        "rock" : "weak"
    }
)

types = {
    "normal" : normal,
    "grass" : grass,
    "fire" : fire,
    "water" : water,
    "bug" : bug
}


vineWhip = Attack(
    22,
    "physical",
    "Vine Whip",
    "grass",
    45,
    100,
    25,
    None
)

razorLeaf = Attack(
    75,
    "physical",
    "Razor Leaf",
    "grass",
    55,
    95,
    25,
    None
)

poison = Status(
    "poison",
    (1 / 16),
    -1,
    "poison"
)

poisonPowder = Attack(
    77,
    "status",
    "Poison Powder",
    "poison",
    0,
    75,
    35,
    poison
)

scratch = Attack(
    10,
    "physical",
    "Scratch",
    "normal",
    40,
    100,
    35,
    None
)

ember = Attack(
    52,
    "physical",
    "Ember",
    "fire",
    40,
    100,
    25,
    None
)

waterGun = Attack(
    55,
    "physical",
    "Water Gun",
    "water",
    40,
    100,
    25,
    None
)

tackle = Attack(
    33,
    "physical",
    "Tackle",
    "normal",
    50,
    100,
    35,
    None
)

bugBite = Attack(
    450,
    "physical",
    "Bug Bite",
    "bug",
    60,
    100,
    20,
    None
)


bulbasaurBaseStats = BaseStats(
    45,
    49,
    49,
    45
)

bulbasaur = Pokemon(
    1,
    "Bulbasaur",
    "Seed Pokemon",
    "Bulbasuar can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's"
    "rays, the seed grows progrssively larger.",
    "grass",
    "poison",
    "0.7 m",
    "6.9 kg",
    "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/001.png",
    1,
    "no rarity",
    bulbasaurBaseStats,
    bulbasaurBaseStats.hp,
    attacks=[vineWhip, razorLeaf, tackle, poisonPowder],
    statusalignments = []
)


charmanderBaseStats = BaseStats(
    39,
    52,
    43,
    65
)

charmander = Pokemon(
    4,
    "Charmander",
    "Lizard Pokemon",
    "The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when"
    "Charmander is enjoying itself. If the Pokemon becomes enraged, the flame burns fiercely",
    "fire",
    None,
    "0,6 m",
    "8.5 kg",
    "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/004.png",
    1,
    "no rarity",
    charmanderBaseStats,
    charmanderBaseStats.hp,
    attacks=[scratch, ember, tackle, poisonPowder],
    statusalignments = []
)

squirtleBaseStats = BaseStats(
    44,
    48,
    65,
    43
)

squirtle = Pokemon(
    7,
    "Squirtle",
    "Tiny Turtle Pokemon",
    "Squirtle's shell is not merely used for protection. The shell's rounded shape and the grooves on its"
    "surface help minimize resistance in water, enabling this Pokemon to swim at high speeds.",
    "water",
    None,
    "0.5 m",
    "9 kg",
    "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/007.png",
    1,
    "no rarity",
    squirtleBaseStats,
    squirtleBaseStats.hp,
    attacks=[waterGun, tackle, scratch, poisonPowder],
    statusalignments = []
)


caterpieBaseStats = BaseStats(
    45,
    30,
    35,
    45
)

caterpie = Pokemon(
    10,
    "Caterpie",
    "Worm Pokemon",
    "Its body is soft and weak. In nature, it's perpetual fate is to be seen by others as food.",
    "bug",
    None,
    "0.3 m",
    "2.9 kg",
    "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/010.png",
    1,
    "no rarity",
    caterpieBaseStats,
    caterpieBaseStats.hp,
    attacks = [tackle, bugBite, scratch, poisonPowder],
    statusalignments = []
)

pokemonTotal = [charmander,bulbasaur, squirtle, caterpie]
playerPokemonTotal = []

while True:
    playerPokemonInput = input("Choose a Pokemon:\n(0)Charmander\n(1)Bulbasaur\n(2)Squirtle\n(3)Caterpie\n")
    try:
        if playerPokemonInput == "0":
            playerPokemonTotal.append(charmander)
            pokemonTotal.remove(charmander)
            if len(playerPokemonTotal) < 2:
                continue
            else:
                opponentPokemonTotal = pokemonTotal
                break
        elif playerPokemonInput == "1":
            playerPokemonTotal.append(bulbasaur)
            pokemonTotal.remove(bulbasaur)
            if len(playerPokemonTotal) < 2:
                continue
            else:
                opponentPokemonTotal = pokemonTotal
                break
        elif playerPokemonInput == "2":
            playerPokemonTotal.append(squirtle)
            pokemonTotal.remove(squirtle)
            if len(playerPokemonTotal) < 2:
                continue
            else:
                opponentPokemonTotal = pokemonTotal
                break
        elif playerPokemonInput == "3":
            playerPokemonTotal.append(caterpie)
            pokemonTotal.remove(caterpie)
            if len(playerPokemonTotal) < 2:
                continue
            else:
                opponentPokemonTotal = pokemonTotal
                break
        else:
            print("Invalid input.")
    except ValueError:
        print("You have already selected that Pokemon.")

playerPokemonAlive = True
opponentPokemonAlive = True

playerPokemon = playerPokemonTotal[0]
opponentPokemon = random.choice(opponentPokemonTotal)

playerPokemonHP = playerPokemon.currenthp
opponentPokemonHP = opponentPokemon.currenthp

playerPokemonPP1 = playerPokemon.attacks[0].pp
playerPokemonPP2 = playerPokemon.attacks[1].pp
playerPokemonPP3 = playerPokemon.attacks[2].pp
playerPokemonPP4 = playerPokemon.attacks[3].pp
opponentPokemonPP1 = opponentPokemon.attacks[0].pp
opponentPokemonPP2 = opponentPokemon.attacks[1].pp
opponentPokemonPP3 = opponentPokemon.attacks[2].pp
opponentPokemonPP4 = opponentPokemon.attacks[3].pp

while True:
    if not playerPokemonAlive:
        playerPokemon = playerPokemonTotal[0]
        playerPokemonHP = playerPokemon.currenthp
        playerPokemonPP1 = playerPokemon.attacks[0].pp
        playerPokemonPP2 = playerPokemon.attacks[1].pp
        playerPokemonPP3 = playerPokemon.attacks[2].pp
        playerPokemonPP4 = playerPokemon.attacks[3].pp
        playerPokemonAlive = True
    elif not opponentPokemonAlive:
        opponentPokemon = random.choice(opponentPokemonTotal)
        opponentPokemonHP = opponentPokemon.currenthp
        opponentPokemonPP1 = opponentPokemon.attacks[0].pp
        opponentPokemonPP2 = opponentPokemon.attacks[1].pp
        opponentPokemonPP3 = opponentPokemon.attacks[2].pp
        opponentPokemonPP4 = opponentPokemon.attacks[3].pp
        opponentPokemonAlive = True

    while True:
        if len(playerPokemon.statusalignments) > 0:
            print(f"You: {playerPokemon.name} {playerPokemonHP}/{playerPokemon.basestats.hp}HP "
                  f"{playerPokemon.statusalignments[0].name}")
        else:
            print(f"You: {playerPokemon.name} {playerPokemonHP}/{playerPokemon.basestats.hp}HP")
        if len(opponentPokemon.statusalignments) > 0:
            print(f"Opponent: {opponentPokemon.name} {opponentPokemonHP}/{opponentPokemon.basestats.hp}HP "
                  f"{opponentPokemon.statusalignments[0].name}")
        else:
            print(f"Opponent: {opponentPokemon.name} {opponentPokemonHP}/{opponentPokemon.basestats.hp}")
        playerDecisionInput = input(f"(0) Attack\n(1) Switch\n")
        if playerDecisionInput == "1":
            playerPokemon.currenthp = playerPokemonHP
            playerPokemon = playerPokemon.p_change_current_active(playerPokemonTotal)
            playerPokemonHP = playerPokemon.currenthp
            while True:
                opponentAttack = random.choice(opponentPokemon.attacks)
                if opponentAttack == opponentPokemon.attacks[0]:
                    if opponentPokemonPP1 == 0:
                        continue
                    else:
                        opponentPokemonPP1 -= 1
                        break
                elif opponentAttack == opponentPokemon.attacks[1]:
                    if opponentPokemonPP2 == 0:
                        continue
                    else:
                        opponentPokemonPP2 -= 1
                        break
                elif opponentAttack == opponentPokemon.attacks[2]:
                    if opponentPokemonPP3 == 0:
                        continue
                    else:
                        opponentPokemonPP3 -= 1
                        break
                elif opponentAttack == opponentPokemon.attacks[3]:
                    if opponentPokemonPP4 == 0:
                        continue
                    else:
                        opponentPokemonPP4 -= 1
                        break
            opponentMissCalculator = random.randint(0, 100)
            if opponentMissCalculator > opponentAttack.accuracy:
                print(f"{opponentPokemon.name} used {opponentAttack.name}\n{opponentPokemon.name}  missed!")
            else:
                playerDamage = opponentPokemon.p_attack(opponentAttack, opponentPokemon, playerPokemon)
                playerPokemonHP -= playerDamage
                print(f"{playerPokemon.name} received {playerDamage} damage!")
                if playerPokemonHP <= 0:
                    print(f"{playerPokemon.name} was defeated!")
                    playerPokemonAlive = False
                    break
                else:
                    if len(opponentPokemon.statusalignments) > 0:
                        for opponentPokemonStatus in opponentPokemon.statusalignments:
                            if int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp) < 1:
                                opponentPokemonHP -= 1
                                print(f"{opponentPokemon.name} received 1 poison damage!")
                                if opponentPokemonHP <= 0:
                                    print(f"{opponentPokemon.name} was defeated!")
                                    opponentPokemonAlive = False
                                    break
                            else:
                                opponentPokemonHP -= int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)
                                print(f"{opponentPokemon.name} received {int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)} poison damage!")
        elif playerDecisionInput == "0":
            try:
                playerAttackInput = int(input(f"\nChoose an attack!\n(0){playerPokemon.attacks[0].name}"
                                              f" {playerPokemonPP1}/{playerPokemon.attacks[0].pp} PP"
                                              f"\n(1){playerPokemon.attacks[1].name} {playerPokemonPP2}/"
                                              f"{playerPokemon.attacks[1].pp} PP\n(2){playerPokemon.attacks[2].name}"
                                              f" {playerPokemonPP3}/{playerPokemon.attacks[2].pp} PP\n"
                                              f"(3){playerPokemon.attacks[3].name} {playerPokemonPP4}/"
                                              f"{playerPokemon.attacks[3].pp} PP\n"))
                try:
                    validInputCheck = playerPokemon.attacks[playerAttackInput]
                    if playerAttackInput == 0:
                        if playerPokemonPP1 == 0:
                            print("You can't use that attack!")
                            continue
                        else:
                            playerPokemonPP1 -= 1
                    elif playerAttackInput == 1:
                        if playerPokemonPP2 == 0:
                            print("You can't use that attack!")
                            continue
                        else:
                            playerPokemonPP2 -= 1
                    elif playerAttackInput == 2:
                        if playerPokemonPP3 == 0:
                            print("You can't use that attack!")
                            continue
                        else:
                            playerPokemonPP3 -= 1
                    elif playerAttackInput == 3:
                        if playerPokemonPP4 == 0:
                            print("You can't use that attack!")
                            continue
                        else:
                            playerPokemonPP4 -= 1
                    playerMissCalculator = random.randint(0, 100)
                    while True:
                        opponentAttack = random.choice(opponentPokemon.attacks)
                        if opponentAttack == opponentPokemon.attacks[0]:
                            if opponentPokemonPP1 == 0:
                                continue
                            else:
                                opponentPokemonPP1 -= 1
                                break
                        elif opponentAttack == opponentPokemon.attacks[1]:
                            if opponentPokemonPP2 == 0:
                                continue
                            else:
                                opponentPokemonPP2 -= 1
                                break
                        elif opponentAttack == opponentPokemon.attacks[2]:
                            if opponentPokemonPP3 == 0:
                                continue
                            else:
                                opponentPokemonPP3 -= 1
                                break
                        elif opponentAttack == opponentPokemon.attacks[3]:
                            if opponentPokemonPP4 == 0:
                                continue
                            else:
                                opponentPokemonPP4 -= 1
                                break
                    opponentMissCalculator = random.randint(0, 100)
                    if playerPokemon.basestats.speed > opponentPokemon.basestats.speed:
                        if playerMissCalculator > playerPokemon.attacks[playerAttackInput].accuracy:
                            print(f"{playerPokemon.name} used {playerPokemon.attacks[playerAttackInput].name}\n{playerPokemon.name} missed!")
                        else:
                            opponentDamage = playerPokemon.p_attack(playerPokemon.attacks[int(playerAttackInput)], playerPokemon, opponentPokemon)
                            opponentPokemonHP -= opponentDamage
                            print(f"{opponentPokemon.name} received {opponentDamage} damage!")
                            if opponentPokemonHP <= 0:
                                print(f"{opponentPokemon.name} was defeated!")
                                opponentPokemonAlive = False
                                break
                            else:
                                if len(playerPokemon.statusalignments) > 0:
                                    for playerPokemonStatus in playerPokemon.statusalignments:
                                        if int(playerPokemonStatus.dpr * playerPokemon.basestats.hp) < 1:
                                            playerPokemonHP -= 1
                                            print(f"{playerPokemon.name} received 1 poison damage!")
                                            if playerPokemonHP <= 0:
                                                print(f"{playerPokemon.name} was defeated!")
                                                playerPokemonAlive = False
                                                break
                                        else:
                                            playerPokemonHP -= int(
                                                playerPokemonStatus.dpr * playerPokemon.basestats.hp)
                                            print(
                                                f"{playerPokemon.name} received {int(playerPokemonStatus.dpr * playerPokemon.basestats.hp)} poison damage!")
                        if opponentMissCalculator > opponentAttack.accuracy:
                            print(f"{opponentPokemon.name} used {opponentAttack.name}\n{opponentPokemon.name}  missed!")
                        else:
                            playerDamage = opponentPokemon.p_attack(opponentAttack, opponentPokemon, playerPokemon)
                            playerPokemonHP -= playerDamage
                            print(f"{playerPokemon.name} received {playerDamage} damage!")
                            if playerPokemonHP <= 0:
                                print(f"{playerPokemon.name} was defeated!")
                                playerPokemonAlive = False
                                break
                            else:
                                if len(opponentPokemon.statusalignments) > 0:
                                    for opponentPokemonStatus in opponentPokemon.statusalignments:
                                        if int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp) < 1:
                                            opponentPokemonHP -= 1
                                            print(f"{opponentPokemon.name} received 1 poison damage!")
                                            if opponentPokemonHP <= 0:
                                                print(f"{opponentPokemon.name} was defeated!")
                                                opponentPokemonAlive = False
                                                break
                                        else:
                                            opponentPokemonHP -= int(
                                                opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)
                                            print(
                                                f"{opponentPokemon.name} received {int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)} poison damage!")
                    elif playerPokemon.basestats.speed < opponentPokemon.basestats.speed:
                        if opponentMissCalculator > opponentAttack.accuracy:
                            print(f"{opponentPokemon.name} used {opponentAttack.name}\n{opponentPokemon.name} missed!")
                        else:
                            playerDamage = opponentPokemon.p_attack(opponentAttack, opponentPokemon, playerPokemon)
                            playerPokemonHP -= playerDamage
                            print(f"{playerPokemon.name} received {playerDamage} damage!")
                            if playerPokemonHP <= 0:
                                print(f"{playerPokemon.name} was defeated!")
                                playerPokemonAlive = False
                                break
                            else:
                                if len(opponentPokemon.statusalignments) > 0:
                                    for opponentPokemonStatus in opponentPokemon.statusalignments:
                                        if int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp) < 1:
                                            opponentPokemonHP -= 1
                                            print(f"{opponentPokemon.name} received 1 poison damage!")
                                            if opponentPokemonHP <= 0:
                                                print(f"{opponentPokemon.name} was defeated!")
                                                opponentPokemonAlive = False
                                                break
                                        else:
                                            opponentPokemonHP -= int(
                                                opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)
                                            print(
                                                f"{opponentPokemon.name} received {int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)} poison damage!")
                        if playerMissCalculator > playerPokemon.attacks[playerAttackInput].accuracy:
                            print(f"{playerPokemon.name} used {playerPokemon.attacks[playerAttackInput].name}\n{playerPokemon.name}  missed!")
                        else:
                            opponentDamage = playerPokemon.p_attack(playerPokemon.attacks[int(playerAttackInput)], playerPokemon, opponentPokemon)
                            opponentPokemonHP -= opponentDamage
                            print(f"{opponentPokemon.name} received {opponentDamage} damage!")
                            if opponentPokemonHP <= 0:
                                print(f"{opponentPokemon.name} was defeated!")
                                opponentPokemonAlive = False
                                break
                            else:
                                if len(playerPokemon.statusalignments) > 0:
                                    for playerPokemonStatus in playerPokemon.statusalignments:
                                        if int(playerPokemonStatus.dpr * playerPokemon.basestats.hp) < 1:
                                            playerPokemonHP -= 1
                                            print(f"{playerPokemon.name} received 1 poison damage!")
                                            if playerPokemonHP <= 0:
                                                print(f"{playerPokemon.name} was defeated!")
                                                playerPokemonAlive = False
                                                break
                                        else:
                                            playerPokemonHP -= int(
                                                playerPokemonStatus.dpr * playerPokemon.basestats.hp)
                                            print(
                                                f"{playerPokemon.name} received {int(playerPokemonStatus.dpr * playerPokemon.basestats.hp)} poison damage!")
                    else:
                        turnRandomizer = random.randint(0, 1)
                        if turnRandomizer == 0:
                            if playerMissCalculator > playerPokemon.attacks[playerAttackInput].accuracy:
                                print(f"{playerPokemon.name} used {playerPokemon.attacks[playerAttackInput].name}\n{playerPokemon.name}  missed!")
                            else:
                                opponentDamage = playerPokemon.p_attack(playerPokemon.attacks[int(playerAttackInput)], playerPokemon, opponentPokemon)
                                opponentPokemonHP -= opponentDamage
                                print(f"{opponentPokemon.name} received {opponentDamage} damage!")
                                if opponentPokemonHP <= 0:
                                    print(f"{opponentPokemon.name} was defeated!")
                                    opponentPokemonAlive = False
                                    break
                                else:
                                    if len(playerPokemon.statusalignments) > 0:
                                        for playerPokemonStatus in playerPokemon.statusalignments:
                                            if int(playerPokemonStatus.dpr * playerPokemon.basestats.hp) < 1:
                                                playerPokemonHP -= 1
                                                print(f"{playerPokemon.name} received 1 poison damage!")
                                                if playerPokemonHP <= 0:
                                                    print(f"{playerPokemon.name} was defeated!")
                                                    playerPokemonAlive = False
                                                    break
                                            else:
                                                playerPokemonHP -= int(
                                                    playerPokemonStatus.dpr * playerPokemon.basestats.hp)
                                                print(
                                                    f"{playerPokemon.name} received {int(playerPokemonStatus.dpr * playerPokemon.basestats.hp)} poison damage!")
                            if opponentMissCalculator > opponentAttack.accuracy:
                                print(f"{opponentPokemon.name} used {opponentAttack.name}\n{opponentPokemon.name}  missed!")
                            else:
                                playerDamage = opponentPokemon.p_attack(opponentPokemon.attacks[random.randint(0, 1)], opponentPokemon,
                                                                        playerPokemon)
                                playerPokemonHP -= playerDamage
                                print(f"{playerPokemon.name} received {playerDamage} damage!")
                                if playerPokemonHP <= 0:
                                    print(f"{playerPokemon.name} was defeated!")
                                    playerPokemonAlive = False
                                    break
                                else:
                                    if len(opponentPokemon.statusalignments) > 0:
                                        for opponentPokemonStatus in opponentPokemon.statusalignments:
                                            if int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp) < 1:
                                                opponentPokemonHP -= 1
                                                print(f"{opponentPokemon.name} received 1 poison damage!")
                                                if opponentPokemonHP <= 0:
                                                    print(f"{opponentPokemon.name} was defeated!")
                                                    opponentPokemonAlive = False
                                                    break
                                            else:
                                                opponentPokemonHP -= int(
                                                    opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)
                                                print(
                                                    f"{opponentPokemon.name} received {int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)} poison damage!")
                        elif turnRandomizer == 1:
                            if opponentMissCalculator > opponentAttack.accuracy:
                                print(f"{opponentPokemon.name} used {opponentAttack.name}\n{opponentPokemon.name}  missed!")
                            else:
                                playerDamage = opponentPokemon.p_attack(opponentPokemon.attacks[random.randint(0, 1)], opponentPokemon,
                                                                        playerPokemon)
                                playerPokemonHP -= playerDamage
                                print(f"{playerPokemon.name} received {playerDamage} damage!")
                                if playerPokemonHP <= 0:
                                    print(f"{playerPokemon.name} was defeated!")
                                    playerPokemonAlive = False
                                    break
                                else:
                                    if len(opponentPokemon.statusalignments) > 0:
                                        for opponentPokemonStatus in opponentPokemon.statusalignments:
                                            if int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp) < 1:
                                                opponentPokemonHP -= 1
                                                print(f"{opponentPokemon.name} received 1 poison damage!")
                                                if opponentPokemonHP <= 0:
                                                    print(f"{opponentPokemon.name} was defeated!")
                                                    opponentPokemonAlive = False
                                                    break
                                            else:
                                                opponentPokemonHP -= int(
                                                    opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)
                                                print(
                                                    f"{opponentPokemon.name} received {int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)} poison damage!")
                            if playerMissCalculator > playerPokemon.attacks[playerAttackInput].accuracy:
                                print(f"{playerPokemon.name} used {playerPokemon.attacks[playerAttackInput].name}\n{playerPokemon.name}  missed!")
                            else:
                                opponentDamage = playerPokemon.p_attack(playerPokemon.attacks[int(playerAttackInput)], playerPokemon, opponentPokemon)
                                opponentPokemonHP -= opponentDamage
                                print(f"{opponentPokemon.name} received {opponentDamage} damage!")
                                if opponentPokemonHP <= 0:
                                    print(f"{opponentPokemon.name} was defeated!")
                                    opponentPokemonAlive = False
                                    break
                                else:
                                    if len(playerPokemon.statusalignments) > 0:
                                        for playerPokemonStatus in playerPokemon.statusalignments:
                                            if int(playerPokemonStatus.dpr * playerPokemon.basestats.hp) < 1:
                                                playerPokemonHP -= 1
                                                print(f"{playerPokemon.name} received 1 poison damage!")
                                                if playerPokemonHP <= 0:
                                                    print(f"{playerPokemon.name} was defeated!")
                                                    playerPokemonAlive = False
                                                    break
                                            else:
                                                playerPokemonHP -= int(
                                                    playerPokemonStatus.dpr * playerPokemon.basestats.hp)
                                                print(
                                                    f"{playerPokemon.name} received {int(playerPokemonStatus.dpr * playerPokemon.basestats.hp)} poison damage!")
                except IndexError:
                    print("Invalid input!")
            except ValueError:
                print("Invalid input!")

    if playerPokemonAlive:
        opponentPokemonTotal.remove(opponentPokemon)
        if len(opponentPokemonTotal) == 0:
            print("You have won!")
            break
        else:
            continue
    elif opponentPokemonAlive:
        playerPokemonTotal.remove(playerPokemon)
        if len(playerPokemonTotal) == 0:
            print("You have lost!")
            break
        else:
            continue