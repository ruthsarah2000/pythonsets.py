'''
Task 1: Flight Route Comparison
Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, 
one for each airline. Write a Python program to find out:
  
Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
'''

our_routes = {"LAX", "JFK", "CDG", "DXB", "ORD", "MDW", "ATL", "MBJ"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK", "KIN", "MDW", "DFW"}

common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)


unique_to_us = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_us)


unique_to_competitor = competitor_routes.difference(our_routes)
print("Destinations unique to the competitor airline:", unique_to_competitor)


no_common_destinations = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:", no_common_destinations)
