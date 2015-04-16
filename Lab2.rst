Welcome to CST 236 Lab 2
------------------------

When tests and behaviour is your designated driver
**************************************************

In this weeks lab you will be presented with a series of job stories.
your job is to develop the tests and code to accomplish that given job
story. The lab is organized into five sections:

#. Python Inheritance
#. Python Logging
#. Test Driven Development
#. Python Behave
#. Behaviour Driven Development

.. note::

    There is a number of new python concepts detailed in this lab. Unlike last lab
    I'd prefer to field any questions through blackboard. If you have questions please
    look there and/or post your questions. If you see questions that you know the answer
    to feel free to respond (only post python answers, no lab answers).

Grading
*******

+---------------------------------------+---------+
| Proper implementation of job stories  | 20 pts  |
+---------------------------------------+---------+
| Coding Style / Readability            | 10 pts  |
+---------------------------------------+---------+
| Proper Documentation (sphinx)         | 10 pts  |
+---------------------------------------+---------+
| Analysis Questions                    | 30 pts  |
+---------------------------------------+---------+
| Correct usage of inheritance          | 10 pts  |
+---------------------------------------+---------+
| Correct usage of Python Logging       | 10 pts  |
+---------------------------------------+---------+
| Feature files parsed and included in  | 10 pts  |
| sphinx documentation                  |         |
+---------------------------------------+---------+
| **Total**                             | 100 pts |
+---------------------------------------+---------+


Python Inheritance
------------------

Classes and inheritance in Python is both extremely powerful and can be extremely confusing. It is very different
from the way that almost every other language handles it. Lets first take a look at the most basic of classes:

.. code:: python

    class MyClass(object):
        def __init__(self):
            self.variable = 'test'

In the above example we are creating a python class named MyClass, which inheirts from object. "object" is a python
keyword that all objects should eventually inherit from (no empty parent lists). Next you will notice the function
"__init__" this is the constructor for creating a new instance of "MyClass" optionally a list of optional / required
parameters can be specified that will require or allow the user to provide additional details on creation.

.. note::

    Parameters that specify an equals some value ("var=something") means that parameter is optional and will default
    to "something" if no parameter is specified. if the parameter is not set to some default then the user must provide
    something.

.. note::

    In the above code "self" is the same as "this" in C++. Self is the current class instance. If a function does
    not specify a self then the function is static and should no be a member of the class. Passing self is not required
    provided you are using a class object with the dot notation.

.. code:: python

    class MyClass(object):
        def __init__(self, var1, var2='test'):
            self.variable1 = var1
            self.variable2 = var2

In the above example var1 is required and must be specified by the user on instantiation. var2 is option and
can be specified at instantiation.

.. code:: python

    obj = MyClass('awesome')   # variable1 will be 'awesome' and variable2 will be 'test'

    obj = MyClass('awesome', 'story')  # variable1 will be 'awesome' and variable2 will be 'story'

.. note::

    Python has a concept of positional arguments vs. keyword arguments. Positional arguments specify values
    without specifying the argument associated with it, such as ('1') whereas keyword args specify the name
    of the parameter and the value such as (x='1'). Positional arguments can be dangerous if the underlying parameter
    list/organization might change. Also if there are several parameters with default values and you only want to
    set the last parameters value you will need to use keyword arguments.

**Variables should always be created in the init function**

* Even if __init__ does not know what value it should be it should set it to "None" (python equivalent to null)
* Your __init__ can call another function such as "reset" to initialize values but your init function must always
  call that function.

.. note::

    Python is an interpreted language so obj.variable1 is not the same as obj.var1 (obj.var1 never created) so if the
    user tries to set obj.var1 they will not receive an error and obj.variable1 will not be set.

**Other functions that can be overloaded:** There is a whole list of functions that a class receives by default.
each of these can be overloaded if there is a good reason to do so: http://www.rafekettler.com/magicmethods.html

.. note::

    Only overload the __del__ operator if you have a very very very excellent reason to do so. __del__ is dangerous
    because an error here will affect proper garbage collection.


**Properties**

Properties in python are similar to setters/getters in C++ and other languages. Python tells us that setters and getters
are confusing and clutter up your code making it unusable. Instead of creating setters and getters you should create
properties. See: https://docs.python.org/2/library/functions.html#property

**super is super confusing**

When a python class inherits from some other python class there are times when we want to use the functions from
the parent as is, python allows not defining the function you wish to use from the parent. Other times you will want
to override this function. But what if you want to use the functionality of the parent function but make some additions
or changes. This can be accomplished using the "super" call.

* Super tells python to travel up the the next parent in the inheritance tree.
* Super should almost always be used in an init function (most of the time at the start)
* Super special care must be taken with regards to parameters when using super (if the parent does not take a parameter
  you will recieve an error.

Example:

.. code:: python

    class MyClass(object):
        def __init__(self, some_var):
            self.some_var = some_var

    class MyChildClass(MyClass):

        def __init__(self, some_var, some_var2):
            super(MyChildClass, self).__init__(some_var)  # don't pass some_var2 because MyClass doesn't accept it

.. note::

    You can also specify the name of the parent you wish to call and the name of the function like
    MyClass.__init__(some_var), but this should only be used in a few select circumstances because it will make
    your life miserable if the inheritance changes. It also destroys mixins.

**Mixins/Multiple inheritance**

Mixins are a neat way to combine multiple classes into a single class (and allow that child class to overwrite as it
needs to).

Example:

This of a case of a motorized Vehicle. All cars have some of the same aspects (engine, wheels, etc.
Now if you wanted to construct an F150 you might define your class as...

.. code:: python

    class F150(Vehicle, FourWheels, TwoDoors, V6, FourWheelDrive):

Notice that this inherits from 4 mixins (Vehicle, TwoDoors, V6 and FourWheelDrive).

Now imagine a GeoMetro:

.. code:: python

    class GeoMetro(Vehicle, FourWheels, TwoDoors, FlintStonesPowered, FWD)

Notice this shares only two mixins with the F150.

When creating/using mixins remember:

* Every class in the mixin/class tree must use super in order for everyone to be able to initialize
* Mixins need to be well throught out rather than just throwing classes at a problem
* Mixins are a good way to ensure you keep your classes less than 1000 lines (pep8 recommended)


**Public, protected, private**

* Public: Variables/function without a leading underscore (_)
* protected: variables/functions with a single underscore (_protected_method)
* private: variables/functions with two underscores (__private_method)

Python Logging
--------------

Python logging is an alternative method of providing information to the console or any other steam.
Python logging is far superior than print statements for several reasons:

* Allows logging levels which can be turned off/on through configuration rather than additional decision points
* Thread Safe
* Allows changing output location using a single line
* Logging in hierarchical. If you have a logger a.b.c and a.b.d setting the level of a.b will set it for both c and d

For additional information about logging see: https://docs.python.org/2/library/logging.html


Test Driven Development Stories
-------------------------------

Your goal for this section is to implement a strong object oriented solution using TDD that completes each of the
job stories detailed in the rounds below. Each round should be done in sequence to illustrate a more realistic
development process.

.. note::

    The job stories in this section as split up into three rounds. Your job
    is to implement each round individually. **YOU MUST COMMIT EACH ROUND BEFORE
    MOVING TO THE NEXT ROUND**

.. note::

    The goal of this is to exercise the concepts of test driven development. I do not expect
    each of the end results to be a complete end to end solution especially because some factors
    might be... imaginary.

Round 1
*******

#. When defending against Orcs I want a way to tell when one has breached the perimeter so I can deploy defenses
#. When diagnosing alert system issues, I want a way to isolate output from particular modules at certain levels so
   I don't have to sift through as much logging data
#. When interfacing with the system I want "X" to quit the program so I can stop this charade.
#. When analyzing threats I want a way to see distance so I can tell how far away each one is.
#. When analyzing threats I want a way to see velocity so I can tell how quickly it's closing in.

Round 2
*******

#. When interfacing with the system I want "?" to display my options so I can see all commands
#. When identifying the threats I want to be able to identify specific orcs by type(8 types minimum) so I know what I'm up against
#. When defending the kingdom I want a way to remove threats based on unique id, so I can focus on only the alive threats
#. When using the system I want to be able to identify units (imperial, metric, parsec or nautical) using a global setting
   so I can market this to other countries.
#. When analyzing threats I want to be able to set the priority of each orc so my troops know where to target

Round 3
*******

#. When identifying threats I want each threat to have a unique id that so I can reference it to get more details
#. When I want to demo the capabilities, I want to be able to generate a listing of randomly generated orcs over time
   so that we can better market the defense shield without needing to be under attack.
#. When I'm bored of an attack, I want to be able to type "ENTer the Trees" to get rid of all orcs so that I can
   always win.

Python Behave
-------------

Behave is a python tool that aides in behaviour driven development. Behave is also the tool that I recommend
most for BDD.

Behaviour Driven Development
----------------------------

Your goal for this section is to implement a strong object oriented solution using BDD that completes each of the
job stories detailed in the rounds below. Each round should be done in sequence to illustrate a more realistic
development process.

This section should be completed using a different set of source code and tests from the previous TDD assignment.

.. note::

    The job stories in this section as split up into three rounds. Your job
    is to implement each round individually. **YOU MUST COMMIT EACH ROUND BEFORE
    MOVING TO THE NEXT ROUND**

.. note::

    The goal of this is to exercise the concepts of test driven development. I do not expect
    each of the end results to be a complete end to end solution especially because some factors
    might be... imaginary.

What is faster: Driving a Hard drive or transferring over ethernet


Round 1
*******

#. When researching speeds I want the cities, distances and connection speeds to be read in from a
   file so I don't have to type them all in
#. When researching speeds I want to be able to select an estimated speed so I can see whether the network or driving would be faster
#. When researching speeds I want to be able to select a hard drive size (in GB) so I can have more data
#. When I enter a city, a speed and hard drive size I want to see whether the network or the hard drive would be faster
#. When I enter a city, speed and hd size I want to see the difference in time between the network and the hard drive


Round 2
*******

#. When entering the driving speed I would like to be able to specify some preset values (Porsche, Bus, Cement Truck, laden swallow)
#. When selecting a city I want to be able to create a new city so I have more options
#. When I enter a new city, I want the results to be written to the city file.

Round 3
*******

#. When researching speed I want to be able to create a route of 1 - 10 cities so I can get a more accurate picture
#. When I start the application I want to enter my starting city, so I know where I am
#. When researching speeds I want to be able to account for network latency so that my numbers are more accurate.
#. When selecting a hard drive I want to enter the hard drive speed (gb/s) to account for the time to copy.

Lab Write-Up
------------

#. Explain the major differences between TDD and BDD
#. What is a mixin, what challenges can occur when testing them? What order are they initialized in
#. In python what does "super" do?
#. Was there any job stories that did not meet the criteria we discussed in class? How did you handle this case?
#. Which model did you find most challenging? Why?
#. Which model did you find easiest to update/maintain?
#. How did you test that logging occurred only when desired?

**Now make sure you have checked in all files and they test cases pass on drone.io.
Submit the assignment in blackboard and include both URLs.**
