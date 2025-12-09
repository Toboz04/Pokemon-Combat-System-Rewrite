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