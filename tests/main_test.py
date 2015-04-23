"""
Test for pyTona.main
"""
import pyTona.main
from unittest import TestCase
import datetime
import getpass
from ReqTracer import requirements

class TestMain(TestCase):

    def setUp(self):
        self.question_mark = chr(0x3E)
        self.pyTona = pyTona.main.Interface()

    @requirements(['#0001'])
    def test_ask_question(self):
        resp = self.pyTona.ask("What day is today" + self.question_mark)
        self.assertNotEqual(resp, None)
        self.assertRaises(Exception, self.pyTona.ask, 3) # can only ask using strings

    @requirements(['#0002'])
    def test_ask_valid(self):
        resp = self.pyTona.ask("How am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("How am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("What am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("Where am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("Who am I" + self.question_mark)
        self.assertEqual(resp, pyTona.main.UNKNOWN_QUESTION)
        resp = self.pyTona.ask("Why am I" + self.question_mark)
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
        self.pyTona.last_question = None
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

    @requirements(['#0018'])
    def test_how_many_seconds_since(self):
        input_time = datetime.datetime(1993, 5, 2, 15, 35, 12, 745)
        delta = datetime.datetime.now() - input_time
        resp = self.pyTona.ask("How many seconds since 1993-05-02 15:35:12.000745" + self.question_mark).split(' ')

        seconds = 0
        try:
            seconds = int(resp[0])
        except ValueError:
            self.fail("int() raised ValueError unexpectedly!")

        self.assertTrue(abs(delta.total_seconds() - seconds) <= 1) # assume 1 second margin of error for CPU time
        self.assertEqual(resp[1], "seconds")
        
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
