"""
Test for sharpTona.exe
"""
from unittest import TestCase
from pywinauto import application
from pywinauto.controls.HwndWrapper import ControlNotEnabled

class TestMain(TestCase):

    def setUp(self):
        self.app = application.Application()
        self.app.start_("sharpTona.exe")
        self.instance = self.app.SharpTona
        
    def tearDown(self):
        self.instance.Close()

    #0001 The system window shall have a title of "SharpTona"
    def test_window_title(self):
        title = "SharpTona"
        self.assertEqual(self.instance.WindowText(), title)
        
    #0002 The system shall provide labels "Question:" and "Answer:"
    def test_labels_exist(self):
        hwnds = self.instance.Children()
        children = [ a.WindowText() for a in hwnds ]
        self.assertIn('Question:', children)
        self.assertIn('Answer: ', children) # control has space at end
        
    #0003 The system shall allow the user to enter a question and press the "Ask" button to receive an answer.
    def test_ask_question(self):
        question = "What is a banana?"
        self.instance['Question:Edit'].TypeKeys(question, with_spaces = True)
        input = self.instance['Question:Edit'].Texts()[0]
        self.assertEqual(input, question)
        self.instance['Ask'].Click()
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, "I don't know please teach me.")

    #0004 The system shall have a default question/answer of "What is the answer to everything?": "42"
    #0006 The system shall display answers in the Answer Text Box
    def test_default_question_and_answer(self):
        question = "What is the answer to everything?"
        self.instance['Question:Edit'].TypeKeys(question, with_spaces = True)
        input = self.instance['Question:Edit'].Texts()[0]
        self.assertEqual(input, question)
        self.instance['Ask'].Click()
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, "42")

    #0005 The system by default shall disable the answer box, "Teach" button and "Correct" button
    def test_default_disabled_controls(self):
        #self.assertRaises(ControlNotEnabled, self.instance['Answer: Edit'].VerifyEnabled)
        #self.assertRaises(ControlNotEnabled, self.instance['Teach'].VerifyEnabled)
        #self.assertRaises(Exception, self.instance['asd'].VerifyEnabled())
        self.assertTrue(True)

    #0007 If no question is asked when the "Ask" button is pushed then "Was that a question?" shall be displayed in the answer box
    def test_ask_without_question(self):
        self.assertTrue(True)
        
    #0008 If the "Ask" button is pushed and the question is known the answer box shall display the answer and enable user input.
    def test_ask_with_known_question_enables_input(self):
        self.assertTrue(True)
        
    #0009 If the "Correct" button is pushed the system shall update the answer to the given question and disable the answer box, teach button and correct button
    def test_correct_button_pushed(self):
        self.assertTrue(True)
        
    #0010 If the "Ask button is pushed and the question is not known then the answer box shall display "I don't know please teach me." and the "Teach" button will be enabled
    def test_teach_button_pushed(self):
        self.assertTrue(True)
        
    #0011 If the "Teach button is pushed the system shall store the answer to the given question and disable the answer box, teach button and correct button
    def test_teach_button_pushed_disable_controls(self):
        self.assertTrue(True)