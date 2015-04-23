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
        assert self.pyTona.ask("What day is today" + self.question_mark) is not None
        self.assertRaises(Exception, self.pyTona.ask, 3)

    @requirements(['#0002'])
    def test_ask_valid(self):
        assert self.pyTona.ask("How am I" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        assert self.pyTona.ask("What am I" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        assert self.pyTona.ask("Where am I" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        assert self.pyTona.ask("Who am I" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        assert self.pyTona.ask("Why am I" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION

    @requirements(['#0003'])
    def test_ask_without_known_keyword(self):
        assert self.pyTona.ask("Do birds fly" + self.question_mark) == pyTona.main.NOT_A_QUESTION_RETURN

    @requirements(['#0004'])
    def test_ask_no_question_mark(self):
        assert self.pyTona.ask("What day is today") == pyTona.main.NOT_A_QUESTION_RETURN

    @requirements(['#0005'])
    def test_question_word_splitter(self):
        assert self.pyTona.ask("What      day, is today  " + self.question_mark) == pyTona.main.UNKNOWN_QUESTION

    @requirements(['#0006', '#0007', '#0008', '#0009', '#0010', '#0011', '#0015'])
    def test_sequence_matcher(self):
        assert self.pyTona.ask("How 0 many 1 days 2 are 3 there 4 in 5 five 6 years 7 earth 8 time" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        answer = str(365 * 5)
        assert self.pyTona.teach(answer) is None
        assert self.pyTona.ask("How many days are there in five years earth time" + self.question_mark) == answer #100% correct
        assert self.pyTona.ask("How many days are there in five years time" + self.question_mark) == answer #90% correct
        assert self.pyTona.ask("How many days are there in five years" + self.question_mark) != answer #80% correct

    @requirements(['#0012', '#0016'])
    def test_teach_without_question(self):
        self.pyTona.last_question = None
        assert self.pyTona.teach("4") == pyTona.main.NO_QUESTION

    @requirements(['#0013', '#0015'])
    def test_can_only_teach_once(self):
        assert self.pyTona.ask("What color is the sky" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        assert self.pyTona.teach("blue") is None
        assert self.pyTona.teach("yellow") == pyTona.main.NO_TEACH
        assert self.pyTona.ask("What color is the sky" + self.question_mark) == "blue"

    @requirements(['#0014'])
    def test_update_answer(self):
        assert self.pyTona.ask("What color is grass" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        assert self.pyTona.teach("green") is None
        assert self.pyTona.correct("pink") is None
        assert self.pyTona.ask("What color is grass" + self.question_mark) == "pink"

    @requirements(['#0017'])
    def test_feet_in_miles(self):
        answer = self.pyTona.ask("What is 23482.5 feet in miles" + self.question_mark).split(' ')
        assert round(float(answer[0]), 2) == 4.45
        assert answer[1] == "miles"

    @requirements(['#0018'])
    def test_how_many_seconds_since(self):
        input_time = datetime.datetime(1993, 5, 2, 15, 35, 12, 745)
        delta = datetime.datetime.now() - input_time
        result = self.pyTona.ask("How many seconds since 1993-05-02 15:35:12.000745" + self.question_mark).split(' ')

        seconds = 0
        try:
            seconds = int(result[0])
        except ValueError:
            self.fail("int() raised ValueError unexpectedly!")
        
        assert abs(delta.total_seconds() - seconds) <= 1 # assume 1 second margin of error for CPU time
        assert result[1] == "seconds"
        
    @requirements(['#0019'])
    def test_who_invented_python(self):
        assert self.pyTona.ask("Who invented Python" + self.question_mark) == "Guido Rossum(BFDL)"

    @requirements(['#0020'])
    def test_why_not_understand_me(self):
        assert self.pyTona.ask("Why don't you understand me" + self.question_mark) == "Because you do not speak 1s and 0s"

    @requirements(['#0021'])
    def test_why_not_shutdown(self):
        assert self.pyTona.ask("Why don't you shutdown" + self.question_mark) == ("I'm afraid I can't do that " + getpass.getuser())
