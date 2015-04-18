Feature: Research Phase
  To better research our options,
  we need to learn more about
  the cities, distances, and connection speeds

  Scenario: Read info from file
    Given the information is in a file
     When a user runs the program
     Then save the file contents to memory

  Scenario: Select estimated network speed
    Given a selection of estimated network speeds
     When selecting an estimated network speed
     Then set the estimated network speed

  Scenario: Select hard drive size
    Given a selection of hard drive sizes
     When selecting a size
     Then set the hard drive size

  Scenario: Given data, determine fastest delivery method
    Given a city, network speed, and hard drive size
     When user wants to send the data
     Then determine whether driving the hard drive or sending the data over the network is faster
	  And determine the time difference between driving the hard drive and sending the data over the network

  Scenario: I want to specify vehicle when entering driving speed
    Given a vehicle and driving speed
     When entering the driving speed
     Then specify a value for vehicle
  
  Scenario: Creating and saving a new city
    Given a selection of cities
     When entering a new city
     Then create the new city
     Then write the new city to file
     
  Scenario: I want to be able to create a route of 1-10 cities for better accuracy
    Given a list of cities
     When selecting from the list of cities
     Then create a route
     
  Scenario: When starting, I want to enter my city origin
    Given a city of origin
     When starting the program
     Then set the city of origin

  Scenario: I want to be able to account for network latency
    Given network latency in milliseconds
     When entering the network latency
     Then save the network latency
     
  Scenario: I want to account for hard drive speed in GB/s
    Given hard drive speed in GB/s
     When entering the hard drive speed
     Then save the hard drive speed