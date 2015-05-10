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
        self.thread_pool = []

    def runTest(self):
        self.pyTona.last_question = None

    def tearDown(self):
        if answer_funcs.seq_finder is not None:
            answer_funcs.seq_finder.stop()
        if answer_funcs.fact_finder is not None:
            answer_funcs.fact_finder.stop()
        if answer_funcs.num_counter is not None:
            answer_funcs.num_counter.stop()
        if answer_funcs.num_opp_counter is not None:
            answer_funcs.num_opp_counter.stop()
        for a in self.thread_pool:
            a.stop()

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
        temp = pyTona.main.Interface()
        for a in range(0, 1000000):
            question = "What " + str(uuid.uuid4()).replace('-', ' ') + self.question_mark
            temp.question_answers[question] = QA(question, 'an answer')
        self.assertGreater(len(temp.question_answers), 999999)

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
        for a in range(0, 50):
            question = "What is %s feet in miles%s" % (str(a * 123.2), self.question_mark)
            start = time.clock()
            resp = self.pyTona.ask(question)
            proc_time = time.clock() - start
            self.assertNotEqual(resp, None)
            self.assertNotIn(resp, self.static_responses)
            self.assertLess(proc_time, .005)

    @requirements(['#0033', '#0034'])
    def test_fibonacci_sequence_time_and_length(self):
        answer_funcs.seq_finder = answer_funcs.FibSeqFinder()
        answer_funcs.seq_finder.start()
        time.sleep(60)
        self.assertFalse(answer_funcs.seq_finder.isAlive())
        self.assertEqual(answer_funcs.seq_finder.num_indexes, 1000)
        
    #0039 The system shall support 1000 concurrent user counters
    @requirements(['#0039'])
    def test_current_count_load(self):
        for a in range(0, 1000):
            self.thread_pool.append(answer_funcs.IndexIncrementer())
            self.thread_pool[-1].start()
        
        time.sleep(10)
        
        counts = []
        for a in self.thread_pool:
            counts.append(a.count)
            a.stop()
        for a in counts:
            self.assertGreater(a, 98)
    
    #0040 The system shall support 1000 concurrent user opposite counters
    @requirements(['#0040'])
    def test_opposite_current_count_spike_load(self):
        # begin load threads
        for a in range(0, 1000):
            self.thread_pool.append(answer_funcs.IndexDecrementer())
            self.thread_pool[-1].start()
        
        time.sleep(10)
                
        # check counts for load threads
        counts = []
        for a in self.thread_pool:
            counts.append(a.count)
            a.stop()
        for a in counts:
            self.assertLess(a, -98)
            
        self.thread_pool = []
            
        # begin excess threads
        for a in range(0, 2000):
            self.thread_pool.append(answer_funcs.IndexDecrementer())
            self.thread_pool[-1].start()
            
        time.sleep(10)
            
        # check counts for excess threads
        counts = []
        for a in self.thread_pool:
            counts.append(a.count)
            a.stop()
        for a in counts:
            self.assertLess(a, -98)
        
    #0041 The system shall generate the first 100 factorial sequence numbers in under 30 seconds
    @requirements(['#0041'])
    def test_factorial_sequence_elapsed_time_and_length(self):
        answer_funcs.fact_finder = answer_funcs.FactSeqFinder()
        answer_funcs.fact_finder.start()
        time.sleep(30)
        self.assertFalse(answer_funcs.fact_finder.isAlive())
        self.assertEqual(answer_funcs.fact_finder.num_indexes, 100)        
        
    #0042 The system shall complete 100 system calls when requesting root directory listing in less than 100ms
    @requirements(['#0042'])
    def test_root_list_load(self):
        total_time = 0
        for a in range(0, 100):
            start = time.clock()
            resp = self.pyTona.ask("What files are in the root directory" + self.question_mark)
            total_time += time.clock() - start
        self.assertLess(total_time, .1)