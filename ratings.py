"""Restaurant rating lister."""
import sys

# put your code here
# openfile using context manager
# iterate through lines
# strip, split(:)
# add to dictionary
# use .items + sorted and print

def sort_ratings(text_file):  #change name
    """organizes restaurant names and ratings
    input: txt file
    returns: """

    with open(text_file) as input_file:

        restaurant_rating = {}
        for line in input_file:
            line = line.rstrip()
            rating = line.split(':')
            restaurant_rating[rating[0]] = float(rating[1])

    return restaurant_rating

sorted_ratings = sort_ratings("scores.txt") # goal:sys.argv

# make this into a function that calls the other
list_of_restaurants = sorted(sorted_ratings.items())

for restaurant in list_of_restaurants:
    print "{} is rated at {}.".format(restaurant[0], restaurant[1])

