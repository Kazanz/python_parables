"""
Fill in the code below to make each classes `test` function return
the classes `answer` attribute.  Only change code between the comments.
Some code may be there for you already.

Good Luck!
"""


class MakingDicts:
    answer = "Once upon a time"

    def test(self):
        d = {}
        d['where'] = "upon a "
        d['dimension'] = 'time.'
        d['time'] = 'Once '
        return d["YOUR CODE HERE"] + d["YOUR CODE HERE"] + d["YOUR CODE HERE"]


class MoreDicts:
    answer = "Pretty Red Door"

    def test(self):
        ideas = {'color': 'Blue ', 'paint': 'Pretty ', 22: "Door"}
        ideas["YOUR CODE HERE"] = "Red "
        return ideas["YOUR CODE HERE"] + ideas["color"] + ideas["YOUR CODE HERE"]


class EvenMoreDicts:
    answer = "Alaskan Snow Crab Legs"

    def test(self):
        words = {
            'type': 'Golden',
            'shell': 'Red',
            'origin': 'Alaskan',
            'name': 'Crab',
            'king': True,
        }
        return "%s %s %s %s" % (
            words.get("YOUR CODE HERE"),
            words.get("YOUR CODE HERE", "YOUR CODE HERE"),
            words.get("YOUR CODE HERE"),
            words.get("bodypart", "Legs"),
        )

class AndMoreDicts:
    answer = [True, True]

    def test(self):
        dinner = {
            'lettuce': '$1.95',
            'tomatos': '$1.99',
            'burgers': '$6.23',
            'ketchup': '$2.33',
        }
        has_burgers = "burgers" in "YOUR CODE HERE"
        expensive = "$6.23" in "YOUR CODE HERE"
        return [has_burgers, expensive]


class LoopingThroughLists:
    answer =  22250

    def test(self):
        prices = {
            "car": 4000,
            "house": 15000,
            "boat": 3000,
            "dog": 250,
        }
        total = 0
        for price in prices.values():
            total = "YOUR CODE HERE"
        return total


class MoreLoopingThroughLists:
    answer = ["dog"]

    def test(self):
        prices = {
            "cars": 4000,
            "house": 15000,
            "boat": 3000,
            "dog": 250,
        }
        stuff = []
        for thing in prices:
            if "YOUR CODE HERE":
                stuff.append(thing)
        return stuff


class EvenMoreLoopingThroughLists:
    answer = 80

    def test(self):
        mydict = {
            1: 10,
            2: 20,
            1: 30,
        }
        nums = []
        for key, value in mydict.items():
            nums.append("YOUR CODE HERE")
        return sum(nums)


class TestDictLooping:
    answer = [326, "Front Row Tickets"]

    def test(self):
        people_going = 3
        soccer = {
            "Tickets": 60,
            "Hotdogs": 8,
            "Parking": 20,
            "Jersey": 33,
            "Front Row Tickets": 500,
            "Sodas": 4,
            "Kiss Cam": "Priceless",
            "Sodas": 4,
            "Nachos": 5,
            "Plane Tickets": 325,
            "Bubble Gum": 1,
            "Souviner": 22,
        }
        price_per_person = 0
        ############################ YOUR CODE HERE ############################
        # Hint: Use a for loop.





        ########################################################################
        return [price_per_person]



questions = [MakingDicts, MoreDicts, EvenMoreDicts, AndMoreDicts,
             LoopingThroughLists, MoreLoopingThroughLists,
             EvenMoreLoopingThroughLists, TestDictLooping]
