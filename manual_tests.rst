**test_window_title**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Verify that the window title displays "SharpTona"

###############

**test_labels_exist**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Verify the label "Question:" is visible
#. Verify the label "Answer:" is visible

###############

**test_ask_question**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Verify that the question edit box is enabled
#. Enter a question into the question edit box
#. Press the "Ask" button
#. Verify that a response has been inserted into the answer edit box
    
###############

**test_default_question_and_answer**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter "What is the answer to everything?" into the question edit box
#. Press the "Ask" button
#. Verify that "42" has been inserted into the answer edit box
    
###############
    
**test_default_disabled_controls**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Verify that the answer edit box, "Teach" and "Correct" buttons are disabled

###############

**test_ask_without_question**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Press the "Ask" button with the question edit box empty
#. Verify that "Was that a question?" has been inserted into the answer edit box
    
###############

**test_correct_button_pushed**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter "What is the answer to everything?" into the question edit box
#. Press the "Ask" button
#. Verify that "42" has been inserted into the answer edit box
#. Enter "43" into the answer edit box
#. Verify the "Correct" button is enabled
#. Press the "Correct" button
#. Verify that the answer edit box, "Teach" and "Correct" buttons are disabled
#. Verify the question remains in the question edit box
#. Press the "Ask" button
#. Verify that "43" has been inserted into the answer edit box

###############

**test_teach_button_pushed**

*Setup*

#. Open sharpTona.exe

*Procedure*

#. Enter "What is a banana?" into the question edit box
#. Press the "Ask" button
#. Verify that "I don't know please teach me." has been inserted into the answer edit box
#. Verify that the "Teach" button is enabled
#. Enter "a yellow fruit" into the answer edit box
#. Press the "Teach" button
#. Verify that the answer edit box, "Teach" and "Correct" buttons are disabled
#. Verify the question remains in the question edit box
#. Press the "Ask" button
#. Verify that "a yellow fruit" has been inserted into the answer edit box