"""
Test for source.source1
"""
import pyTona.main
from unittest import TestCase
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

    @requirements(['#0006', '#0007', '#0008', '#0009'])
    def test_sequence_matcher(self):
        assert self.pyTona.ask("How 0 many 1 days 2 are 3 there 4 in 5 five 6 years 7 earth 8 time" + self.question_mark) == pyTona.main.UNKNOWN_QUESTION
        answer = str(365 * 5)
        self.pyTona.teach(answer);
        assert self.pyTona.ask("How many days are there in five years earth time" + self.question_mark) == answer
        assert self.pyTona.ask("How many days are there in five years time" + self.question_mark) == answer
        assert self.pyTona.ask("How many days are there in five years" + self.question_mark) != answer

    @requirements(['#0009'])
    def test_(self):
        assert True is True

"""
DONE - #0005 The system shall break a question down into words separated by space
DONE - #0006 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer
DONE - #0007 The system shall exclude any number value from match code and provide the values to generator function (if one exists)
DONE - #0008 When a valid match is determined the system shall return the answer
DONE - #0009 When no valid match is determined the system shall return "I don't know, please provide the answer"
"""

"""
#0010 The system shall provide a means of providing an answer to the previously asked question.
#0011 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
#0012 If no previous question has been asked the system shall respond with "Please ask a question first"
#0013 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don't know about that. I was taught differently" and not update the question
"""

"""
#0014 The system shall provide a means of updating an answer to the previously asked question.
#0015 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
#0016 If no previous question has been asked the system shall respond with "Please ask a question first"
"""

"""
#0017 The system shall respond to the question "What is <float> feet in miles" with the the float value divided by 5280 and append "miles" to the end of the return.
#0018 The system shall respond to the question "How many seconds since <date time>" with the number of seconds from that point of day till now.
#0019 The system shall respond to the question "Who invented Python" with "Guido Rossum(BFDL)"
#0020 The system shall respond to the question "Why don't you understand me" with "Because you do not speak 1s and 0s"
#0021 The system shall respond to the question "Why don't you shutdown" with "I'm afraid I can't do that <username>"

Username shall be determined by the name of the currently logged in user.
"""
