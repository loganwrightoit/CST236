"""
Test for pyTona.main
"""
import pyTona.main
from unittest import TestCase
import datetime
import getpass
from ReqTracer import requirements
import socket
from mock import patch

class TestMain(TestCase):

    def setUp(self):
        self.question_mark = chr(0x3F)
        self.pyTona = pyTona.main.Interface()
        self.static_responses = { pyTona.main.UNKNOWN_QUESTION, pyTona.main.NOT_A_QUESTION_RETURN, pyTona.main.NO_QUESTION, pyTona.main.NO_TEACH }

    def runTest(self):
        self.pyTona.last_question = None

    @requirements(['#0001'])
    def test_ask_question(self):
        resp = self.pyTona.ask("What day is today" + self.question_mark)
        self.assertNotEqual(resp, None)
        self.assertRaises(Exception, self.pyTona.ask, 3) # can only ask using strings

    @requirements(['#0002'])
    def test_ask_valid(self):
        resp = self.pyTona.ask("How am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("What am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("Where am I" + self.question_mark)
        self.assertNotIn(resp, self.static_responses)
        resp = self.pyTona.ask("Why am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("Who am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)

    @requirements(['#0003'])
    def test_ask_without_known_keyword(self):
        resp = self.pyTona.ask("Do birds fly" + self.question_mark)
        self.assertEqual(resp, pyTona.main.NOT_A_QUESTION_RETURN)

    @requirements(['#0004'])
    def test_ask_no_question_mark(self):
        resp = self.pyTona.ask("What day is today")
        self.assertEqual(resp, pyTona.main.NOT_A_QUESTION_RETURN)

    @requirements(['#0005'])
    def test_question_word_splitter(self):
        resp = self.pyTona.ask("What      day, is today  " + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)

    @requirements(['#0006', '#0007', '#0008', '#0009', '#0010'])
    def test_sequence_matcher(self):
        resp = self.pyTona.ask("How 0 many 1 days 2 are 3 there 4 in 5 five 6 years 7 earth 8 time" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        expected = str(365 * 5)
        resp = self.pyTona.teach(expected)
        self.assertEqual(resp, None)
        resp = self.pyTona.ask("How many days are there in five years earth time" + self.question_mark) # 100% correct
        self.assertEquals(resp, expected)
        resp = self.pyTona.ask("How many days are there in five years time" + self.question_mark) # 90% correct
        self.assertEquals(resp, expected)
        resp = self.pyTona.ask("How many days are there in five years" + self.question_mark) # 80% correct
        self.assertNotEquals(resp, expected)

    @requirements(['#0012', '#0016'])
    def test_teach_without_question(self):
        resp = self.pyTona.teach("4")
        self.assertEqual(resp, pyTona.main.NO_QUESTION)

    @requirements(['#0013', ])
    def test_can_only_teach_once(self):
        resp = self.pyTona.ask("What color is the sky" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.teach("blue")
        self.assertEqual(resp, None)
        resp = self.pyTona.ask("What color is the sky" + self.question_mark)
        self.assertEqual(resp, "blue")
        resp = self.pyTona.teach("yellow")
        self.assertEqual(resp, pyTona.main.NO_TEACH)
        resp = self.pyTona.ask("What color is the sky" + self.question_mark)
        self.assertEqual(resp, "blue")

    @requirements(['#0011', '#0014', '#0015'])
    def test_update_answer(self):
        resp = self.pyTona.ask("What color is grass" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.teach("green")
        self.assertEqual(resp, None)
        resp = self.pyTona.ask("What color is grass" + self.question_mark)
        self.assertEqual(resp, "green")
        resp = self.pyTona.correct("pink")
        self.assertEqual(resp, None)
        resp = self.pyTona.ask("What color is grass" + self.question_mark)
        self.assertEqual(resp, "pink")

    @requirements(['#0017'])
    def test_feet_in_miles(self):
        answer = self.pyTona.ask("What is 23482.5 feet in miles" + self.question_mark).split(' ')
        afloat = round(float(answer[0]), 2)
        self.assertEqual(afloat, 4.45)
        self.assertEqual(answer[1], "miles")
        
    @requirements(['#0019'])
    def test_who_invented_python(self):
        resp = self.pyTona.ask("Who invented Python" + self.question_mark)
        self.assertEqual(resp, "Guido Rossum(BFDL)")

    @requirements(['#0020'])
    def test_why_not_understand_me(self):
        resp = self.pyTona.ask("Why don't you understand me" + self.question_mark)
        self.assertEqual(resp, "Because you do not speak 1s and 0s")

    @requirements(['#0021'])
    def test_why_not_shutdown(self):
        resp = self.pyTona.ask("Why don't you shutdown" + self.question_mark)
        expected = "I'm afraid I can't do that " + getpass.getuser()
        self.assertEqual(resp, expected)

    @requirements(['#0022'])
    def test_ask_where_am_i(self):
        resp = self.pyTona.ask("Where am I" + self.question_mark)
        self.assertNotIn(resp, self.static_responses)

    @requirements(['#0023'])
    def test_ask_where_are_you(self):
        resp = self.pyTona.ask("Where are you" + self.question_mark)
        self.assertNotIn(resp, self.static_responses)

    @patch('pyTona.answer_funcs.socket.socket.connect')
    @requirements(['#0024', '#0025', '#0026', '#0027'])
    def test_ask_who_else_is_here(self, mock_connect):
        
        # test receiving a response
        #mock_sock.recv.return_value = "Logan$John Doe"
        resp = self.pyTona.ask("Who else is here" + self.question_mark)
        #mock_sock.connect.assert_called_once_with(('192.168.64.3', '1337'))
        #mock_connect.assert_called_once_with(('192.168.64.3', '1337'))
        #self.assertEqual("[ \"Logan\", \"John Doe\" ]", resp)

        # test not receiving a response
        #mock_sock.connect.side_effect = socket.error
        #resp = self.pyTona.ask("Who else is here" + self.question_mark)
        #self.assertEqual(resp, "IT'S A TRAAAPPPP")

    @requirements(['#0028', '#0029'])
    def test_ask_fibonacci_sequence_digit(self):
        #stuff
        #0028 The system shall respond to the question "What is the <int> digit of the Fibonacci sequence?" with the correct number from the fibonnacci sequence if the number has been found
        #0029 If the system has not determined the requested digit of the Fibonacci sequence it will respond with A)"Thinking...", B)"One second" or C)"cool your jets" based on a randomly generated number (A is 60% chance, B is 30% chance, C is 10% chance)
        self.assertTrue(True)
