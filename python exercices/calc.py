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
        if b == 0:
            print('division by zero !')
        else: return print(a / b)


class ModifiedCalc(BaseCalc):
    def __init__(self):
        super().__init__()
        self.operations = {
            '+': self.plus,
            '-': self.minus,
            '*': self.multiple,
            '/': self.division
        }


    def plus(self, *args):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            return print(sum(args[0]))
        elif len(args) == 2:
            return print(sum(args))
        else:
            print('Invalid input')

    def calculate_from_input(self, data=None):
        pattern = r'^(-?\d+(\.\d+)?)([+\-*/])(-?\d+(\.\d+)?)$'
        while True:
            if data is None:
                data = input('Enter data: ')

            parse_data = re.fullmatch(pattern=pattern, string=data)

            if parse_data:
                a = float(parse_data.group(1))
                op = parse_data.group(3)
                b = float(parse_data.group(4))

                if op in self.operations:
                    self.operations[op](a, b)
                    break
            else:
                print('not valid data, try again')
                data = None





c = ModifiedCalc()
c.calculate_from_input()