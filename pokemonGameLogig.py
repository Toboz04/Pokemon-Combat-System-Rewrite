import random
from pokemonClassesAndTypes import *
from pokemonAttacks import *
from pokemonPokemons import *

def playerPokemonPick():
    while True:
        playerPokemonInput = input("Choose a Pokemon:\n(0)Charmander\n(1)Bulbasaur\n(2)Squirtle\n(3)Caterpie\n")
        try:
            if playerPokemonInput == "0":
                playerPokemonTotal.append(charmander)
                pokemonTotal.remove(charmander)
                if len(playerPokemonTotal) < 2:
                    continue
                else:
                    break
            elif playerPokemonInput == "1":
                playerPokemonTotal.append(bulbasaur)
                pokemonTotal.remove(bulbasaur)
                if len(playerPokemonTotal) < 2:
                    continue
                else:
                    break
            elif playerPokemonInput == "2":
                playerPokemonTotal.append(squirtle)
                pokemonTotal.remove(squirtle)
                if len(playerPokemonTotal) < 2:
                    continue
                else:
                    break
            elif playerPokemonInput == "3":
                playerPokemonTotal.append(caterpie)
                pokemonTotal.remove(caterpie)
                if len(playerPokemonTotal) < 2:
                    continue
                else:
                    break
            else:
                print("Invalid input.")
        except ValueError:
            print("You have already selected that Pokemon.")



def opponentAttackChoice():
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
    return opponentAttack

def playerAttackDecision():
    while True:
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
                        break
                elif playerAttackInput == 1:
                    if playerPokemonPP2 == 0:
                        print("You can't use that attack!")
                        continue
                    else:
                        playerPokemonPP2 -= 1
                        break
                elif playerAttackInput == 2:
                    if playerPokemonPP3 == 0:
                        print("You can't use that attack!")
                        continue
                    else:
                        playerPokemonPP3 -= 1
                        break
                elif playerAttackInput == 3:
                    if playerPokemonPP4 == 0:
                        print("You can't use that attack!")
                        continue
                    else:
                        playerPokemonPP4 -= 1
                        break
            except IndexError:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
    return playerAttackInput



def checkPlayerAlive():
    if playerPokemonHP <= 0:
        print(f"{playerPokemon.name} was defeated!")
        return False
    else:
        return True

def checkOpponentAlive():
    if opponentPokemonHP <= 0:
        print(f"{opponentPokemon.name} was defeated!")
        return False
    else:
        return True



def opponentStatusAlignment():
    for opponentPokemonStatus in opponentPokemon.statusalignments:
        if int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp) < 1:
            opponentPokemonHP -= 1
            print(f"{opponentPokemon.name} received 1 poison damage!")
            opponentPokemonAlive = checkOpponentAlive()
            return opponentPokemonAlive
        else:
            opponentPokemonHP -= int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)
            print(
                f"{opponentPokemon.name} received {int(opponentPokemonStatus.dpr * opponentPokemon.basestats.hp)} poison damage!")
            opponentPokemonAlive = checkOpponentAlive()
            return opponentPokemonAlive

def playerStatusAlignment():
    for playerPokemonStatus in playerPokemon.statusalignments:
        if int(playerPokemonStatus.dpr * playerPokemon.basestats.hp) < 1:
            playerPokemonHP -= 1
            print(f"{playerPokemon.name} received 1 poison damage!")
            playerPokemonAlive = checkPlayerAlive()
            return playerPokemonAlive
        else:
            playerPokemonHP -= int(
                playerPokemonStatus.dpr * playerPokemon.basestats.hp)
            print(
                f"{playerPokemon.name} received {int(playerPokemonStatus.dpr * playerPokemon.basestats.hp)} poison damage!")
            playerPokemonAlive = checkPlayerAlive()
            return playerPokemonAlive


      
def opponentTurn():
    opponentAttack = opponentAttackChoice()
    opponentMissCalculator = random.randint(0, 100)
    if opponentMissCalculator > opponentAttack.accuracy:
        print(f"{opponentPokemon.name} used {opponentAttack.name}\n{opponentPokemon.name}  missed!")
        return playerPokemonAlive
    else:
        playerDamage = opponentPokemon.p_attack(opponentAttack, opponentPokemon, playerPokemon)
        playerPokemonHP -= playerDamage
        print(f"{playerPokemon.name} received {playerDamage} damage!")
        playerPokemonAlive = checkPlayerAlive()
        if playerPokemonAlive == False:
            return playerPokemonAlive
        else:
            if len(opponentPokemon.statusalignments) > 0:
                opponentPokemonAlive = opponentStatusAlignment()
                return opponentPokemonAlive
                
def playerTurn():
    playerDecisionInput = input(f"(0) Attack\n(1) Switch\n")
    if playerDecisionInput == "1":
        playerPokemon.currenthp = playerPokemonHP
        playerPokemon.currentpp[0] = playerPokemonPP1
        playerPokemon.currentpp[1] = playerPokemonPP2
        playerPokemon.currentpp[2] = playerPokemonPP3
        playerPokemon.currentpp[3] = playerPokemonPP4
        playerPokemon = playerPokemon.p_change_current_active(playerPokemonTotal)
        playerPokemonHP = playerPokemon.currenthp
        playerPokemonPP1 = playerPokemon.currentpp[0]
        playerPokemonPP2 = playerPokemon.currentpp[1]
        playerPokemonPP3 = playerPokemon.currentpp[2]
        playerPokemonPP4 = playerPokemon.currentpp[3]
        return opponentPokemonAlive
    elif playerDecisionInput == "0":
        playerAttackInput = playerAttackDecision()
        playerMissCalculator = random.randint(0, 100)
        if playerMissCalculator > playerPokemon.attacks[playerAttackInput].accuracy:
            print(
                f"{playerPokemon.name} used {playerPokemon.attacks[playerAttackInput].name}\n{playerPokemon.name} missed!")
            return opponentPokemonAlive
        else:
            opponentDamage = playerPokemon.p_attack(playerPokemon.attacks[int(playerAttackInput)], playerPokemon,
                                                    opponentPokemon)
            opponentPokemonHP -= opponentDamage
            print(f"{opponentPokemon.name} received {opponentDamage} damage!")
            opponentPokemonAlive = checkOpponentAlive()
            if opponentPokemonAlive == False:
                return opponentPokemonAlive
            else:
                if len(playerPokemon.statusalignments) > 0:
                    playerPokemonAlive = playerStatusAlignment()
                    return playerPokemonAlive


def combat():
    pokemonAlive = True
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

        if playerPokemon.basestats.speed > opponentPokemon.basestats.speed:
            pokemonAlive = playerTurn()
            if pokemonAlive == False:
                return
            pokemonAlive = opponentTurn()
            if pokemonAlive == False:
                return
        elif playerPokemon.basestats.speed < opponentPokemon.basestats.speed:
            pokemonAlive = opponentTurn()
            if pokemonAlive == False:
                return
            pokemonAlive = playerTurn()
            if pokemonAlive == False:
                return 
        else:
            turnRandomizer = random.randint(0, 1)
            if turnRandomizer == 0:
                pokemonAlive = playerTurn()
                if pokemonAlive == False:
                    return
                pokemonAlive = opponentTurn()
                if pokemonAlive == False:
                    return
            elif turnRandomizer == 1:
                pokemonAlive = opponentTurn()
                if pokemonAlive == False:
                    return
                pokemonAlive = playerTurn()
                if pokemonAlive == False:
                    return


if __name__ == "__main__":
    pokemonTotal = [charmander, bulbasaur, squirtle, caterpie]
    playerPokemonTotal = []
    
    playerPokemonPick()
    opponentPokemonTotal = pokemonTotal
    
    print(pokemonTotal)
    print(playerPokemonTotal)
    print(opponentPokemonTotal)

    playerPokemonAlive = True
    opponentPokemonAlive = True
    
    playerPokemon = playerPokemonTotal[0]
    opponentPokemon = random.choice(opponentPokemonTotal)

    playerPokemonHP = playerPokemon.currenthp
    opponentPokemonHP = opponentPokemon.currenthp
    
    playerPokemonPP1 = playerPokemon.currentpp[0]
    playerPokemonPP2 = playerPokemon.currentpp[1]
    playerPokemonPP3 = playerPokemon.currentpp[2]
    playerPokemonPP4 = playerPokemon.currentpp[3]
    
    opponentPokemonPP1 = opponentPokemon.currentpp[0]
    opponentPokemonPP2 = opponentPokemon.currentpp[1]
    opponentPokemonPP3 = opponentPokemon.currentpp[2]
    opponentPokemonPP4 = opponentPokemon.currentpp[3]
    
    while True:
        combat()
        
        if playerPokemonAlive:
            opponentPokemonTotal.remove(opponentPokemon)
            if len(opponentPokemonTotal) == 0:
                print("You have won!")
                break
            else:
                opponentPokemon = random.choice(opponentPokemonTotal)
                opponentPokemonHP = opponentPokemon.currenthp
                opponentPokemonPP1 = opponentPokemon.currentpp[0]
                opponentPokemonPP2 = opponentPokemon.currentpp[1]
                opponentPokemonPP3 = opponentPokemon.currentpp[2]
                opponentPokemonPP4 = opponentPokemon.currentpp[3]
                opponentPokemonAlive = True
                continue
        elif opponentPokemonAlive:
            playerPokemonTotal.remove(playerPokemon)
            if len(playerPokemonTotal) == 0:
                print("You have lost!")
                break
            else:
                playerPokemon = playerPokemonTotal[0]
                playerPokemonHP = playerPokemon.currenthp
                playerPokemonPP1 = playerPokemon.currentpp[0]
                playerPokemonPP2 = playerPokemon.currentpp[1]
                playerPokemonPP3 = playerPokemon.currentpp[2]
                playerPokemonPP4 = playerPokemon.currentpp[3]
                playerPokemonAlive = True
                continue