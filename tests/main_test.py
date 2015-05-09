"""
Test for pyTona.main
"""
import pyTona.main
from pyTona import answer_funcs
from unittest import TestCase
import datetime
import getpass
from ReqTracer import requirements
import socket
from mock import patch
from mock import Mock
import time
import uuid
from pyTona.question_answer import QA

class TestMain(TestCase):

    def setUp(self):
        self.question_mark = chr(0x3F)
        self.pyTona = pyTona.main.Interface()
        self.static_responses = { pyTona.main.UNKNOWN_QUESTION, pyTona.main.NOT_A_QUESTION_RETURN, pyTona.main.NO_QUESTION, pyTona.main.NO_TEACH }

    def runTest(self):
        self.pyTona.last_question = None

    def tearDown(self):
        if answer_funcs.seq_finder is not None:
            answer_funcs.seq_finder.stop() # stop sequence finder thread

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

    @requirements(['#0012'])
    def test_teach_without_question(self):
        resp = self.pyTona.teach("4")
        self.assertEqual(resp, pyTona.main.NO_QUESTION)

    @requirements(['#0016'])
    def test_correct_without_question(self):
        resp = self.pyTona.correct("4")
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
    def test_too_many_extra_parameters(self):
        self.assertRaises(Exception, self.pyTona.ask, "What is 232.5 134.6 feet in miles" + self.question_mark)
        
    @requirements(['#0019'])
    def test_who_invented_python(self):
        resp = self.pyTona.ask("Who invented Python" + self.question_mark)
        self.assertEqual(resp, "Guido Rossum(BDFL)")

    @requirements(['#0020'])
    def test_why_not_understand_me(self):
        resp = self.pyTona.ask("Why don't you understand me" + self.question_mark)
        self.assertEqual(resp, "Because you do not speak 1s and 0s")

    @requirements(['#0021'])
    def test_why_not_shutdown(self):
        resp = self.pyTona.ask("Why don't you shutdown" + self.question_mark)
        expected = "I'm afraid I can't do that " + getpass.getuser()
        self.assertEqual(resp, expected)

    @patch('pyTona.answer_funcs.subprocess.Popen')
    @requirements(['#0022'])
    def test_ask_where_am_i(self, mock_popen):
        # test filled tuple branch
        mock_popen().communicate.return_value = ( 'aBranch', 'bBranch' )
        resp = self.pyTona.ask("Where am I" + self.question_mark)
        mock_popen().communicate.assert_called_once_with()
        self.assertEqual(resp, "aBranch")

        # test empty tuple branch
        mock_popen().communicate.return_value = ( '', '' )
        resp = self.pyTona.ask("Where am I" + self.question_mark)
        self.assertEqual(resp, "Unknown")

        # test exception branch
        mock_popen().communicate.side_effect = Exception
        resp = self.pyTona.ask("Where am I" + self.question_mark)
        self.assertEqual(resp, "Unknown")

    @patch('pyTona.answer_funcs.subprocess.Popen')
    @requirements(['#0023'])
    def test_ask_where_are_you(self, mock_popen):
        # test filled tuple branch
        mock_popen().communicate.return_value = ( 'aValue', 'bValue' )
        resp = self.pyTona.ask("Where are you" + self.question_mark)
        mock_popen().communicate.assert_called_once_with()
        self.assertEqual(resp, "aValue")

        # test empty tuple branch
        mock_popen().communicate.return_value = ( '', '' )
        resp = self.pyTona.ask("Where are you" + self.question_mark)
        self.assertEqual(resp, "Unknown")

        # test exception branch
        mock_popen().communicate.side_effect = Exception
        resp = self.pyTona.ask("Where are you" + self.question_mark)
        self.assertEqual(resp, "Unknown")
        
    @patch('pyTona.answer_funcs.socket.socket')
    @requirements(['#0024', '#0025', '#0026'])
    def test_ask_who_else_is_here_with_response(self, mock_sock):
        mock_sock().recv.return_value = "Logan$User"
        resp = self.pyTona.ask("Who else is here" + self.question_mark)
        mock_sock().connect.assert_called_once_with(('192.168.64.3', 1337))
        mock_sock().send.assert_called_once_with('Who?')
        self.assertEqual(resp, [ "Logan", "User" ])

    @patch('pyTona.answer_funcs.socket.socket')
    @requirements(['#0027'])
    def test_ask_who_else_is_here_without_response(self, mock_sock):
        mock_sock().recv.return_value = False
        resp = self.pyTona.ask("Who else is here" + self.question_mark)
        self.assertEqual(resp, "IT'S A TRAAAPPPP")

    @requirements(['#0028', '#0029'])
    def test_ask_fibonacci_sequence_digit(self):
        oob_resp = [ "Thinking...", "One second", "cool your jets" ]
                    
        # initiate fibonacci thread and verify a waiting response
        resp = self.pyTona.ask("What is the 10 digit of the Fibonacci sequence" + self.question_mark) 
        self.assertIn(resp, oob_resp)
        
        # let fibonacci thread accumulate ~12 results
        time.sleep(.5)
        
        # test fibonacci number
        resp = self.pyTona.ask("What is the 10 digit of the Fibonacci sequence" + self.question_mark) 
        self.assertEqual(resp, 55)
        
        # test chance ratios against expected responses (prone to failure)
        #count = [ 0, 0, 0 ]
        #for a in range(1000, 1100):
        #    resp = self.pyTona.ask("What is the " + str(a) + " digit of the Fibonacci sequence" + self.question_mark)
        #    count[oob_resp.index(resp)] += 1
        #self.assertAlmostEqual(count[0], 60, delta=20) # requirement is 60%
        #self.assertAlmostEqual(count[1], 30, delta=15) # requirement is 30%
        #self.assertAlmostEqual(count[2], 10, delta=5) # requirement is 10%
        
    @requirements(['#0030'])
    def test_store_one_million_qas(self):
        for a in range(0, 1000000):
            question = "What " + str(uuid.uuid4()).replace('-', ' ') + self.question_mark
            self.pyTona.question_answers[question] = QA(question, 'an answer')
        self.assertGreater(len(self.pyTona.question_answers), 999999)

    @requirements(['#0031'])
    def test_store_answer_time_elapsed(self):
        for a in range(0, 100):
            self.pyTona.last_question = "What " + str(uuid.uuid4()).replace('-', ' ') + self.question_mark
            start = time.clock()
            resp = self.pyTona.teach("an answer")
            proc_time = time.clock() - start
            self.assertEqual(resp, None)
            self.assertLess(proc_time, .005)

    @requirements(['#0032'])
    def test_response_time_elapsed(self):
        for a in range(0, 100):
            start = time.clock()
            self.pyTona.ask("What is " + str(a) + " feet in miles" + self.question_mark).split(' ')
            proc_time = time.clock() - start
            self.assertLess(proc_time, .005)

    @requirements(['#0033', '#0034'])
    def test_fibonacci_sequence_time_and_length(self):
        # start a new fibonacci thread
        seq_finder = answer_funcs.FibSeqFinder()
        seq_finder.start()
        time.sleep(60)
        self.assertFalse(seq_finder.isAlive())
        self.assertEqual(seq_finder.num_indexes, 1000)