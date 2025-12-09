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
