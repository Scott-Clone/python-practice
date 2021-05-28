from collections import OrderedDict
import re
from itertools import chain

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = ', ' .join(cars.get('Jeep'))
    return(jeeps)

def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
   
    return [model[0] for model in cars.values()]
 
def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected

def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    r = [[i for i in cars[x] if re.search(grep, i, re.IGNORECASE)] for x in cars.keys()]
    return(list(chain(*r)))


def test_get_all_matching_models_default_grep():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected

def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return {make: sorted(model) for 
    		make, model in cars.items()}


def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected

def likes(names):
    #your code here
    n = len(names)
    return {
    0: "no one likes this",
    1: "{} likes this",
    2: "{} and {} like this",
    3: "{}, {} and {} like this",
    4: "{}, {} and {number_x} others like this",
    }[min(4, n)].format(*names[:number_x], x =(n - 2))


