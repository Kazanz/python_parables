import json
import unittest

from python_strings.parables import questions as questions1
from python_lists.parables import questions as questions2
from python_sorting.parables import questions as questions3
from python_dictionaries.parables import questions as questions4



class TestParables(unittest.TestCase):
    correct = "\n\n" + ("_" * 70) + '\n'
    questions = [questions1, questions2, questions3, questions4]

    def msg(self, cls, user_answer, answer):
        msg = self.correct
        msg += "\n\n" + ("-" * 70)
        msg += "\n\n'{}' is incorrect."
        msg += "\n\nYou returned: \n\n\t{}"
        msg += "\n\nIt should return: \n\n\t{}"
        name = cls.__class__.__name__
        msg = msg.format(name, json.dumps(user_answer), json.dumps(answer))
        return msg

    def append_correct(self, cls):
        msg = "\n{}: Correct!"
        self.correct += msg.format(cls.__class__.__name__)

    def test_parables(self):
        for questions in self.questions:
            for cls in questions:
                cls = cls()
                answer = cls.answer
                user_answer = cls.test()
                self.assertEqual(user_answer, answer,
                                 msg=self.msg(cls, user_answer, answer))
                self.append_correct(cls)


if __name__ == '__main__':
    unittest.main()
