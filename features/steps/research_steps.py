import os.path
from behave import *
from source.behave.research import Research

"""
    Scenario:
        Read info from file
"""

@given('the information is in a file')
def step_get_data_from_file(context):
    dir = os.path.dirname(__file__)
    rel_path = "data.txt"
    context.data_path = os.path.join(dir, rel_path)
    assert os.path.exists(context.data_path) is True

@when('a user runs the program')
def step_get_data_pass(context):
    pass

@then('save the file contents to memory')
def step_save_data_to_memory(context):
    context.research.readDataFromFile(context.data_path)
    assert context.research.city[0] == [ 'Salem', '50', '65' ]

"""
    Scenario:
        Select estimated speed
"""

@given('a selection of estimated network speeds')
def step_impl(context):
    context.netspeed = [ 1, 10, 100 ]
    assert context.netspeed is not []

@when('selecting an estimated network speed')
def step_impl(context):
    pass

@then('set the estimated network speed')
def step_impl(context):
    context.research.mbps = context.netspeed[1]
    assert context.research.mbps is context.netspeed[1]

"""
    Scenario:
        Select hard drive size
"""

@given('a selection of hard drive sizes')
def step_impl(context):
    context.hdd_sizes = [ 100, 200, 1000]
    assert context.hdd_sizes is not []

@when('selecting a size')
def step_impl(context):
    pass

@then('set the hard drive size')
def step_impl(context):
    context.research.hdd_size = context.hdd_sizes[1]
    assert context.research.hdd_size is context.hdd_sizes[1]

"""
    Scenario:
        Given data, determine fastest
        delivery method and show time
        difference
"""

@given('a city, network speed, and hard drive size')
def step_impl(context):
    context.city = context.research.city[0][0]
    context.distance = int(context.research.city[0][1])
    context.drive_speed = int(context.research.city[0][2])
    assert context.city == "Salem"
    assert context.distance is 50
    assert context.drive_speed is 65

@when('user wants to send the data')
def step_impl(context):
    pass

@then('determine whether driving the hard drive or sending the data over the network is faster')
def step_impl(context):
    result = context.research.computeFastestMethod(context.city)
    assert result is "Driving"

@then('determine the time difference between driving the hard drive and sending the data over the network')
def step_impl(context):
    context.time_drive = context.research.computeDriveTimeInMinutes(context.distance, context.drive_speed)
    assert (context.time_drive - 46.15) < 0.01
    context.time_network = context.research.computeNetworkTimeInMinutes()
    print(context.time_network)
    assert (context.time_network - 2666.66) < 0.01
    result = context.research.computeTimeDiff(context.city)
    assert (result - 2620.51) < 0.01