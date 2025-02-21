class Character:

    def __init__(self, name, speed, jump_height, power, defense, winning_cry):
        self.name = name
        self.speed = speed
        self.jump_height = jump_height
        self.power = power
        self.defense = defense
        self.winning_cry = winning_cry

    def upon_win(self):
        print(self.winning_cry)

bonzo = Character("Bonzo", 6, 2, 8, 5, "Hooray!")

print(f'''Character: {bonzo.name}
          Speed: {bonzo.speed}
          Jump Height: {bonzo.jump_height}
          Power: {bonzo.power}
          Defense: {bonzo.defense}
          Winning Cry: {bonzo.winning_cry}''')
bonzo.upon_win()