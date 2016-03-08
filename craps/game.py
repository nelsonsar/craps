class Game(object):
    def cycle(self, player):
        """
            This method represents a round of Craps.
            In each round player receive a pair of dices, rolls it and
            game analyze the sum of the throw to decide the winner
        """
        result = player.roll_dices()

        if result == 7:
            return "Player wins!"

        if result == 2:
            return "House wins!"
