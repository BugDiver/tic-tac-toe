import unittest

from src.lib.game import Game


class TestGameTest(unittest.TestCase):
    def test_game_should_return_user_symbol(self):
        game = Game("X")
        self.assertEquals(game.getUserSymbol(), 'X')

    def test_isSpaceFree_should_tell_if_given_position_is_free(self):
        game = Game('X')
        self.assertTrue(game.isSpaceFree(1))
        self.assertTrue(game.isSpaceFree(2))
        self.assertTrue(game.isSpaceFree(3))
        self.assertTrue(game.isSpaceFree(4))
        self.assertTrue(game.isSpaceFree(5))
        self.assertTrue(game.isSpaceFree(6))
        self.assertTrue(game.isSpaceFree(7))
        self.assertTrue(game.isSpaceFree(8))
        self.assertTrue(game.isSpaceFree(9))

    def test_make_move_should_make_users_move(self):
        game = Game('X')
        game.makeMove(1, 'X')
        self.assertFalse(game.isSpaceFree(1))

    def test_make_move_should_not_make_users_move_if_there_is_no_space(self):
        game = Game('X')
        game.makeMove(1, 'X')
        game.makeMove(1, 'X')
        self.assertFalse(game.isSpaceFree(1))

    def test_isBoardFull_should_return_true_if_there_is_no_any_space_to_move(self):
        game = Game('X')
        game.makeMove(1, 'X')
        game.makeMove(2, 'X')
        game.makeMove(3, 'X')
        self.assertFalse(game.isBoardFull())

        game.makeMove(4, 'X')
        game.makeMove(5, 'X')
        game.makeMove(6, 'X')
        game.makeMove(7, 'X')
        game.makeMove(8, 'X')
        game.makeMove(9, 'X')
        self.assertTrue(game.isBoardFull())

    def test_getBotSymbol_should_decide_symbol_for_bot_according_to_player_symbol(self):
        game = Game('X')
        self.assertEquals(game.getBotSymbol(), 'O')
        game2 = Game('O')
        self.assertEquals(game2.getBotSymbol(), 'X')

    def test_isWinner_should_tell_if_given_symbol_has_won_the_game(self):
        game = Game('X')
        game.makeMove(1, 'X')
        game.makeMove(2, 'X')
        game.makeMove(3, 'X')

        self.assertTrue(game.isWinner('X'))

    # =============================A.I.==============================================================================

    def test_getBotMove_should_try_to_move_in_middle_if_it_is_free(self):
        game = Game('X')
        self.assertEquals(game.getBotMove(), 5)

    def test_getBotMove_should_try_to_take_a_corner_if_center_is_not_free(self):
        game = Game('X')
        game.makeMove(5, 'X')
        self.assertTrue(game.getBotMove() in [1, 3, 7, 9])

    def test_getBotMove_should_block_if_player_can_win_in_next_round(self):
        game = Game('X')
        game.makeMove(1, 'X')
        game.makeMove(3, 'X')
        self.assertEquals(game.getBotMove(), 2)

    def test_getBotMove_should_try_to_be_winner_if_it_can(self):
        game = Game('X')
        game.makeMove(1, 'O')
        game.makeMove(3, 'O')
        self.assertEquals(game.getBotMove(), 2)

    def test_getInitialTurn_should_choose_random_turn_between_player_and_bot(self):
        game = Game('X')
        self.assertTrue(game.getInitialMove() in ['Player', 'Bot'])

    def test_getBoard_should_give_array_representation_of_game(self):
        game = Game('X')
        self.assertListEqual(game.getBoard(), ['...'] * 10)
        game.makeMove(1, 'X')
        self.assertListEqual(game.getBoard(), ['...', 'X', '...', '...', '...', '...', '...', '...', '...', '...'])
        game.makeMove(game.getBotMove(), game.getBotSymbol())
        self.assertListEqual(game.getBoard(), ['...', 'X', '...', '...', '...', 'O', '...', '...', '...', '...'])


if __name__ == "__main__":
    unittest.main()
