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