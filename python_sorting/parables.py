"""
Fill in the code below to make each classes `test` function return
the classes `answer` attribute.  Only change code between the comments.
Some code may be there for you already.

Good Luck!
"""


class Sorted:
    answer = [1, 2, 3, 4, 5, 6]

    def test(self):
        list1 = [3, 5, 1]
        list2 = [4, 2, 6]
        final_list = []
        sorted("YOUR CODE HERE")
        return final_list


class CaseSensitive:
    answer = ['BA', 'BB', 'CC', 'Ca', 'aa', 'cc']

    def test(self):
        letters = ['aa', 'BB', 'BA', 'cc', 'CC', 'Ca']
        final_list = []
        sorted("YOUR CODE HERE")
        return  final_list


class Reverse:
    answer = [6, 5, 4, 3, 2, 1]

    def test(self):
        my_list = range("YOUR CODE HERE", "YOUR CODE HERE")
        sorted("YOUR CODE HERE")
        return my_list


class SortByKey:
    answer = [
        'Some fell on hard ground',
        'some fell on stones and shriveled,'
        'others fell among the thorns and choked,',
        'but some of the seed fell on good earth and produced.',
    ]

    def test(self):
        my_list = [
            'others fell among the thorns and choked,',
            'some fell on stones and shriveled,'
            'but some of the seed fell on good earth and produced.',
            'Some fell on hard ground',
        ]
        sorted("YOUR CODE HERE")
        return my_list


class TupleUnpacking:
    answer = ["Fish", "Crabs", "Octopi", "Sushi", "Yum"]

    def test(self):
        stuff = ("YOUR CODE HERE")
        more_stuff = ("YOUR CODE HERE")
        stuff = stuff + more_stuff
        hey, ha, ho, hi, hue = stuff
        return hue, ho, hi, ha, hey


class ListComprehension1:
    answer = [2, 4, 6, 8, 10]

    def test(self):
        return ["YOUR CODE HERE" for num in range(1, 6)]


class ListComprehension2:
    answer = [1, 22, 45]

    def test(self):
        numbers = [1, 443, 568, 22, 45, 280]
        return ["YOUR CODE HERE" for num in numbers if "YOUR CODE HERE"]


questions = [Sorted, CaseSensitive, Reverse, SortByKey, TupleUnpacking,
             ListComprehension1, ListComprehension2]
