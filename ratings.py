"""Restaurant rating lister."""
import sys

# put your code here
# openfile using context manager
# iterate through lines
# strip, split(:)
# add to dictionary
# use .items + sorted and print

filename = sys.argv[1]

def txt_to_dictionary(filename):
    """organizes restaurant names and ratings
    input: txt file
    returns: dictionary"""

    with open(filename) as input_file:

        restaurant_rating = {}
        for line in input_file:
            line = line.rstrip()
            rating = line.split(':')
            restaurant_rating[rating[0]] = float(rating[1])

    return restaurant_rating


def sort_and_print():
    """placeholder"""

    unsorted_dict = txt_to_dictionary(filename)
    list_of_restaurants = sorted(unsorted_dict.items())

    for restaurant in list_of_restaurants:
        print "{} is rated at {}".format(restaurant[0], restaurant[1])

sort_and_print()