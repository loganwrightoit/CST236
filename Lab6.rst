Welcome to CST 236 Lab 6
------------------------

In this weeks lab you will be building UI tests for the SharpTona UI. There are new 
requirements to cover.


.. note::

    drone.io is not required this week. 

Grading
*******

+---------------------------------------+---------+
| Proper testing of requirements        | 30 pts  |
| (automated)                           |         |
+---------------------------------------+---------+
| Proper testing of requirements        | 20 pts  |
| (manual)                              |         |        
+---------------------------------------+---------+
| Coding Style / Readability            | 10 pts  |
+---------------------------------------+---------+
| Analysis Questions                    | 30 pts  |
+---------------------------------------+---------+
| Drone.io passing                      | 10 pts  |
+---------------------------------------+---------+
| **Total**                             | 100 pts |
+---------------------------------------+---------+

Steps
*****

#. Pull SharpTona.exe
#. Create manual tests in write up for UI requirements (see template below)
#. Create automated tests in a new ui_test.py file

Manual Test Template
********************

**<Test Name>**

*Setup*

#. <list of steps to prepare for test execution>
#. <list of steps to prepare for test execution>

*Procedure*

#. <action to take ie "Press button xyz">
#. <check to perform ie "#0042: Verify box abc is updated to display 'awesome'"
#. etc

UI Requirements
***************

#0001 The system window shall have a title of "SharpTona"
#0002 The system shall provide labels "Question:" and "Answer:"
#0003 The system shall allow the user to enter a question and press the "Ask" button to receive an answer.
#0004 The system shall have a default question/answer of "What is the answer to everything?": "42"
#0005 The system by default shall disable the answer box, "Teach" button and "Correct" button
#0006 The system shall display answers in the Answer Text Box
#0007 If no question is asked when the "Ask" button is pushed then "Was that a question?" shall be displayed in the answer box
#0008 If the "Ask" button is pushed and the question is known the answer box shall display the answer and enable user input.
#0009 If the "Correct" button is pushed the system shall update the answer to the given question and disable the answer box, teach button and correct button
#0010 If the "Ask button is pushed and the question is not known then the answer box shall display "I don't know please teach me." and the "Teach" button will be enabled
#0011 If the "Teach button is pushed the system shall store the answer to the given question and disable the answer box, teach button and correct button

Analysis Questions
******************

#. What are the advantages and disadvantages of manual testing?
#. What are the advantages and disadvantages of automated testing?
#. What new bugs did you encounter with the new code?
#. How many UI tests did you generate? How did you deteremine you had written enough?
#. How long did this lab take to accomplish?
