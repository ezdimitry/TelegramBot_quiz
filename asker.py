import math
import random


class Asker:
    class Question:
        content = ""
        answers = []
        ansId = 0

        def __init__(self, cntnt, answ, ansid):
            self.content = cntnt
            self.answers = answ
            self.ansId = ansid

        def check(self, input):
            return self.ansId == input

    questions = []
    i = 0

    def __init__(self, qstns):
        self.questions = qstns
