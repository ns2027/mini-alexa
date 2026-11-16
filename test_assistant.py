"""Deterministic acceptance checks; no external test runner needed."""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
import calculator
import ai_concepts
import content
import game
import main


class AssistantTests(unittest.TestCase):
    def test_arithmetic(self):
        for expression, expected in [('12+8',20), ('10-3',7), ('-2*-3',6), ('9/2',4.5), ('.5 + -2',-1.5)]:
            with self.subTest(expression=expression):
                self.assertEqual(calculator.calculate(*calculator.parse_expression(expression)), expected)

    def test_invalid_arithmetic(self):
        for expression in ['hello', '2**3', '__import__("os")', '1+2+3', 'NaN + 2', '']:
            with self.subTest(expression=expression), self.assertRaises(ValueError):
                calculator.parse_expression(expression)
        for expression in ['5/0', '1e999+1', '1e308*1e308']:
            with self.subTest(expression=expression), self.assertRaises(ValueError):
                calculator.calculate(*calculator.parse_expression(expression))

    def test_recommendation_boundaries(self):
        expected = {0:'Rest',4:'Rest',5:'Have breakfast',11:'Have breakfast',12:'Have lunch',16:'Have lunch',17:'Take a walk',20:'Take a walk',21:'Have dinner',23:'Have dinner'}
        for hour, prefix in expected.items():
            self.assertTrue(ai_concepts.recommend_activity(hour).startswith(prefix))

    def test_neuron(self):
        for inputs, output in [([1,0],1),([0,1],0),([0,0],0),([1,1],0)]:
            self.assertEqual(ai_concepts.perceptron(inputs)[1], output)
        for values in [[], [1], [1,2,3], [float('nan'),1], [float('inf'),1]]:
            with self.assertRaises(ValueError):
                ai_concepts.perceptron(values)

    def test_content_selection(self):
        for getter, items in [(content.get_random_quote,content.QUOTES),(content.get_random_joke,content.JOKES),(content.get_random_fact,content.FACTS)]:
            with patch('content.random.choice', side_effect=items):
                self.assertEqual({getter() for _ in items}, set(items))

    def run_game(self, guesses):
        buffer = io.StringIO()
        with patch('game.random.randint', return_value=10), patch('builtins.input', side_effect=guesses), redirect_stdout(buffer):
            result = game.play_guessing_game()
        return result, buffer.getvalue()

    def test_game_hints_and_win(self):
        result, transcript = self.run_game(['5','15','10'])
        self.assertIn('won in 3', result)
        self.assertIn('higher', transcript)
        self.assertIn('lower', transcript)

    def test_game_limit_invalid_and_cancel(self):
        result, _ = self.run_game(['abc','0','21','1','2'])
        self.assertIn('No tries left', result)
        self.assertEqual(self.run_game(['cancel'])[0], 'Game cancelled.')

    def test_routing_no_substring_false_matches(self):
        for command in ['sometimes', 'update', '', 'unknown']:
            with redirect_stdout(io.StringIO()) as output:
                self.assertTrue(main.respond(command, 'Shubh'))
            self.assertIn('not sure', output.getvalue())
        for command in ['exit','quit','bye','bye!']:
            self.assertFalse(main.respond(command, 'Shubh'))

    def test_full_session(self):
        inputs = ['Shubh','hello','name','time','date','calculate 12 + 8','calculate 10 - 2','calculate 3 * 4','calculate 9 / 2','calculate 5 / 0','calculate nope','quote','joke','fact','recommend','concepts','perceptron','1 0','perceptron','nan 1','game','cancel','help','unknown','','exit']
        with patch('builtins.input', side_effect=inputs), redirect_stdout(io.StringIO()) as output:
            main.main()
        transcript = output.getvalue()
        for phrase in ['Nice to meet you, Shubh','Hello, Shubh','Your name is Shubh','The result is 20',"can't divide by zero",'Output: 1','Invalid input','Goodbye, Shubh']:
            self.assertIn(phrase, transcript)

    def test_interruptions(self):
        for error in [EOFError, KeyboardInterrupt]:
            for inputs in [[error], ['Shubh',error], ['Shubh','game',error], ['Shubh','perceptron',error], ['Shubh','calculate',error]]:
                with patch('builtins.input', side_effect=inputs), redirect_stdout(io.StringIO()) as output:
                    main.main()
                self.assertIn('Goodbye', output.getvalue())


if __name__ == '__main__':
    unittest.main()
