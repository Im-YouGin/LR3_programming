import re
from itertools import cycle
from Stack import Stack
from functions import *

class Shunting_yard:
    """
    Реализация алгоритма сортировочной станции.
    """
    def __init__(self, expression):
        self.operator_stack = Stack(size=500)
        self.postfix = []
        self.expression = expression
        self.operators = ['+', '-', '*', '/', '^', '#', '!']

    def replace_unary_minus(self):
        tokens = re.findall("[+/*/!()^-]|\d+", self.expression)
        for ind, token in enumerate(tokens):
            if token == '-' and tokens[ind - 1] == '(':
                tokens[ind] = '#'

        self.expression = ''.join(tokens)

    def to_postfix(self):
        tmp_str = ''
        for token in self.expression:
            if token == ' ':
                continue

            if token.isalnum():
                tmp_str += token
                continue

            if tmp_str:
                self.postfix.append(tmp_str)
            tmp_str = ''

            if token in self.operators:
                while self.operator_stack.top is not None \
                        and self.operator_stack.top not in '()' and \
                        (presedence(self.operator_stack.top) > presedence(token) or
                        (presedence(self.operator_stack.top) == presedence(token) and
                        association(self.operator_stack.top) == 'left')):
                    self.postfix.append(self.operator_stack.pop())
                self.operator_stack.push(token)

            elif token == '(':
                self.operator_stack.push(token)

            elif token == ')':
                while self.operator_stack.top != '(':
                    self.postfix.append(self.operator_stack.pop())

                if self.operator_stack.top == '(':
                    self.operator_stack.pop()
        if tmp_str:
            self.postfix.append(tmp_str)

        while not self.operator_stack.empty:
            self.postfix.append(self.operator_stack.pop())

        return self.postfix

    def eval_postfix(self):
        stack = Stack(size=200)

        for token in self.postfix:

            if token.isalnum():
                stack.push(token)

            elif token in self.operators:
                if token == '#':
                    top = stack.pop().replace('(', '').replace(')', '')

                    stack.push(f'({str((-1) * float(top))})')
                    continue

                if token == '!':
                    top = stack.pop().replace('(', '').replace(')', '')

                    stack.push(f'({factorial(float(top))})')
                    continue

                right_operand = stack.pop()
                left_operand = stack.pop()
                res = evaluate(left_operand, right_operand, token)
                stack.push(f'({str(res)})')

        res = stack.pop()[1:-1]
        return res