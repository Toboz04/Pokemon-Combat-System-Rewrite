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