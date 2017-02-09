import unittest
from unittest.mock import patch
import hangman
import display


class TestGenerateNumber(unittest.TestCase):

    # TestCase 1 - this test will select a word and verify it is in the list of playable words
    def test_select_word(self):
        # select a word
        m = hangman.Main()

        word = m.select_word()

        self.assertIn(word, m.words)

    # TestCase 2 - test select main menu input
    def test_menu_input(self):
        m = hangman.Main()
        self.assertTrue(display.is_valid_menu_option(0, m.start_menu_options))
        self.assertTrue(display.is_valid_menu_option(1, m.start_menu_options))
        self.assertFalse(display.is_valid_menu_option('A', m.start_menu_options))
        self.assertFalse(display.is_valid_menu_option(-1, m.start_menu_options))
        self.assertFalse(display.is_valid_menu_option(3.3, m.start_menu_options))

    # test user guesses
    @patch('builtins.input', side_effect=['1', '#', 'zz', 'C', 'c'])
    @patch('builtins.print')
    def test_guess(self, mock_print, mock_input):
        m = hangman.Main()
        m.reset_game()

        guess = m.get_guess()
        self.assertFalse(m.is_in_available_letters(guess))
        mock_print.assert_called_with('\nThat\'s not a valid guess.\n')

        guess = m.get_guess()
        self.assertFalse(m.is_in_available_letters(guess))

        # zz
        guess = m.get_guess()
        self.assertFalse(m.is_in_available_letters(guess))

        # C
        guess = m.get_guess()
        self.assertTrue(m.is_in_available_letters(guess))

        guess = m.get_guess()
        m.remove_from_available_letters(guess)
        self.assertFalse(m.is_in_available_letters(guess))

    @patch('builtins.print')
    def test_blank_display(self, mock_print):
        word = 'abcdefg'
        display.game_board(word)
        mock_print.assert_called_with('\n_ _ _ _ _ _ _')

        word = '142ASF!@FA'
        display.game_board(word)
        mock_print.assert_called_with('\n_ _ _ _ _ _ _ _ _ _')

    @patch('builtins.print')
    def test_correct_letter_display(self, mock_print):

        word = 'looping'

        guessed_letters = ['l', 'o', '1', '5', 1, '33', None, '']

        display.correct_guessed_letters(word, guessed_letters)

        mock_print.assert_called_with('l o o _ _ _ _')

    def test_bad_guess_count(self):

        m = hangman.Main()

        m.reset_bad_guess_count('m')

        self.assertEqual(m.bad_guesses, 7)

        m.reset_bad_guess_count(None)

        self.assertEqual(m.bad_guesses, 7)

        m.reset_bad_guess_count(10)

        self.assertEqual(m.bad_guesses, 10)

        m.reset_bad_guess_count('2')

        self.assertEqual(m.bad_guesses, 2)
