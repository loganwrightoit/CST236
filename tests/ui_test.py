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
    #0008 If the "Ask" button is pushed and the question is known the answer box shall display the answer and enable user input.
    def test_default_question_and_answer(self):
        question = "What is the answer to everything?"
        self.instance['Question:Edit'].TypeKeys(question, with_spaces = True)
        input = self.instance['Question:Edit'].Texts()[0]
        self.assertEqual(input, question)
        
        # check that input is disabled first
        input_enabled = self.instance['Answer: Edit'].IsEnabled()
        self.assertFalse(input_enabled)
        
        self.instance['Ask'].Click()
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, "42")
        
        # check that input is now enabled
        input_enabled = self.instance['Answer: Edit'].IsEnabled()
        self.assertTrue(input_enabled)

    #0005 The system by default shall disable the answer box, "Teach" button and "Correct" button
    def test_default_disabled_controls(self):
        self.assertRaises(ControlNotEnabled, self.instance['Answer: Edit'].VerifyEnabled)
        self.assertRaises(ControlNotEnabled, self.instance['Teach'].VerifyEnabled)
        self.assertRaises(ControlNotEnabled, self.instance['Correct'].VerifyEnabled)

    #0007 If no question is asked when the "Ask" button is pushed then "Was that a question?" shall be displayed in the answer box
    def test_ask_without_question(self):
        input = self.instance['Question:Edit'].Texts()[0]
        self.assertEqual(input, '')
        self.instance['Ask'].Click()
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, "Was that a question?")
        
    #0009 If the "Correct" button is pushed the system shall update the answer to the given question and disable the answer box, teach button and correct button
    def test_correct_button_pushed(self):
        # change answer from 42 to 43
        question = "What is the answer to everything?"
        self.instance['Question:Edit'].TypeKeys(question, with_spaces = True)
        input = self.instance['Question:Edit'].Texts()[0]
        self.assertEqual(input, question)
        self.instance['Ask'].Click()
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, "42")
        self.instance['Answer: Edit'].SetText('43')
        self.instance['Correct'].Click()
        
        # test that controls disabled
        self.assertRaises(ControlNotEnabled, self.instance['Answer: Edit'].VerifyEnabled)
        self.assertRaises(ControlNotEnabled, self.instance['Teach'].VerifyEnabled)
        self.assertRaises(ControlNotEnabled, self.instance['Correct'].VerifyEnabled)

        # check that answer is not updated
        input = self.instance['Question:Edit'].Texts()[0]
        self.assertEqual(input, question)
        self.instance['Ask'].Click()
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, "43")

    #0010 If the "Ask button is pushed and the question is not known then the answer box shall display "I don't know please teach me." and the "Teach" button will be enabled
    #0011 If the "Teach button is pushed the system shall store the answer to the given question and disable the answer box, teach button and correct button
    def test_teach_button_pushed(self):
        # ask an unknown question
        question = "What is a banana?"
        self.instance['Question:Edit'].TypeKeys(question, with_spaces = True)
        input = self.instance['Question:Edit'].Texts()[0]
        self.assertEqual(input, question)
        
        # check that Teach button is disabled
        teach_enabled = self.instance['Teach'].IsEnabled()
        self.assertFalse(teach_enabled)
                
        # select Ask and check answer
        self.instance['Ask'].Click()
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, "I don't know please teach me.")
        
        # check that Teach button is now enabled
        teach_enabled = self.instance['Teach'].IsEnabled()
        self.assertTrue(teach_enabled)
        
        # teach answer
        expected = "a yellow fruit"
        self.instance['Answer: Edit'].TypeKeys(expected, with_spaces = True)
        self.instance['Teach'].Click()
        
        # check if answer has updated
        answer = self.instance['Answer: Edit'].Texts()[0]
        self.assertEqual(answer, expected)