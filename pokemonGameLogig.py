import random
from pokemonClassesAndTypes import *
from pokemonAttacks import *
from pokemonPokemons import *

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