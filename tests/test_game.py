from craps.game import Game
from craps.player import Player
import unittest
from mock import Mock

class GameTest(unittest.TestCase):
    def test_player_wins_with_a_7(self):
        player = self.player_throws_and_gets_a(7)

        self.player_wins(player)

    def test_player_loses_with_a_2(self):
        expected = "House wins!"
        player = self.player_throws_and_gets_a(2)

        self.player_loses(player)

    def player_throws_and_gets_a(self, result):
        """
            Simulates Player throwing dices and returning
            a defined result
        """

        mock_spec = Mock(spec = Player)
        player = mock_spec.return_value
        player.roll_dices.return_value = result

        return player

    def player_wins(self, player):
        expected = "Player wins!"

        self.assert_game_cycle_ran(player, expected)

    def player_loses(self, player):
        expected = "House wins!"

        self.assert_game_cycle_ran(player, expected)

    def assert_game_cycle_ran(self, player, expected_result):
        """
            Run all asserts to confirm that a complete cycle was run.
            Checks if the player roll the dices and if the output is the
            expected one given as argument.
        """

        game = Game()
        result = game.cycle(player)

        self.assertEquals(expected_result, result)
        player.roll_dices.assert_called_once_with()
