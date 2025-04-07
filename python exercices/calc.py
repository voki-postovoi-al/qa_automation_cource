import re


class BaseCalc():
    def __init__(self):
        pass

    def plus(self, a, b):
        return print(a + b)

    def minus(self, a, b):
        return  print(a - b)

    def multiple(self, a, b):
        return print(a * b)

    def division(self, a, b):
        return print(a / b)

class ModifinedCalc(BaseCalc):
    def plus(self, *args):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            return print(sum(args[0]))
        elif len(args) == 2:
            return print(sum(args))
        else:
            print('Invalid input')

    def calculate_from_input(self, data=None):
        pattern = r'^(-?\d+(\.\d+)?)([+\-*/])(-?\d+(\.\d+)?)$'
        if data is None:
            data = input('Enter data: ')

        parseData = re.fullmatch(pattern=pattern, string=data)

        if parseData:
            a = float(parseData.group(1))
            op = parseData.group(3)
            b = float(parseData.group(4))

        operations = {
            '+' : self.plus,
            '-' : self.minus,
            '*' : self.multiple,
            '/' : self.division
        }

        if op in operations:
            operations[op](a, b)
        else:
            print(f'not valid data: {data}')




c = ModifinedCalc()
c.calculate_from_input()