'''
https://adventofcode.com/2020/day/18
'''
DAY = 18

from utils import *
from collections import deque
from operator import mul, add


def parser(test=False):
    return Input(DAY, 2020, test=test)


class Evaluator:
    def __init__(self, expression):
        self.expression = deque( expression.split(' ') )
        self.state = self._start
        self.result = 0
        self.operation = add
        self.operand = 0


    def _start(self):
        self._next_operand()
        self.result = self.operand
        self.operand = 0
        self.state = self._next_operation


    def _next_operation(self):
        operator = self.expression.popleft()
        if operator == '+':
            self.operation = add
        elif operator == '*':
            self.operation = mul
        else:
            raise NotImplementedError

        self.state = self._next_operand
        

    def _next_operand(self):
        if self.expression[0].isnumeric():
            self.operand = int(self.expression.popleft())
        else: # Parenthesis
            subexpression = []
            parens = 0
            while True:
                next_block = self.expression.popleft()
                parens += next_block.count('(') - next_block.count(')')
                subexpression.append(next_block)

                if not parens:
                    break

            subexpression = ' '.join(subexpression)[1:-1]
            sub_evaluator = Evaluator(subexpression)
            self.operand = sub_evaluator.run()
        
        self.state = self._operate
        

    def _operate(self):
        self.result = self.operation(self.result, self.operand)

        self.state = self._next_operation


    def run(self):
        while self.expression:
            self.state()

        self._operate() # Last operation
        return self.result


def part1(input):
    result = 0
    for line in input:
        evaluator = Evaluator(line)
        partial_result = evaluator.run()
        result += partial_result

    return result


class AdvancedEvaluator:
    def __init__(self, expression):
        self.expression = deque( expression.split(' ') )
        self.state = self._start
        self.result = 0
        self.operation = add
        self.operand = 0
        self.mul_expression = []


    def _start(self):
        self._next_operand()
        self.result = self.operand
        self.operation = add
        self.state = self._next_operation


    def _next_operation(self):
        operator = self.expression.popleft()
        if operator == '+':
            self.operation = add
            self._next_operand()
            self._operate()
        elif operator == '*':
            self.mul_expression.append(str(self.result))
            self.mul_expression.append('*')
            self.state = self._start
        else:
            raise NotImplementedError

        
    def _next_operand(self):
        if self.expression[0].isnumeric():
            self.operand = int(self.expression.popleft())
        else: # Parenthesis
            subexpression = []
            parens = 0
            while True:
                next_block = self.expression.popleft()
                parens += next_block.count('(') - next_block.count(')')
                subexpression.append(next_block)

                if not parens:
                    break

            subexpression = ' '.join(subexpression)[1:-1]
            sub_evaluator = AdvancedEvaluator(subexpression)
            self.operand = sub_evaluator.run()
        

    def _operate(self):
        self.result = self.operation(self.result, self.operand)

        self.state = self._next_operation


    def run(self):
        while self.expression:
            self.state()

        self.mul_expression.append( str(self.result) )

        mul_expression = ' '.join(self.mul_expression)
        mul_evaluator = Evaluator(mul_expression)
        return mul_evaluator.run()


def part2(input):
    result = 0
    for line in input:
        evaluator = AdvancedEvaluator(line)
        partial_result = evaluator.run()
        result += partial_result

    return result
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [26457], part2, [694173])
    main()