import re


class BaseCalc:
    def __init__(self):
        pass

    def plus(self, a, b):
        result = a + b
        print(result)
        return result

    def minus(self, a, b):
        result = a - b
        print(result)
        return result

    def multiple(self, a, b):
        result = a * b
        print(result)
        return result

    def division(self, a, b):
        if b == 0:
            print('division by zero !')
        else:
            result = a / b
            print(result)
            return result


class ModifiedCalc(BaseCalc):
    def __init__(self):
        super().__init__()
        self.operations = {
            '+': self.plus,
            '-': self.minus,
            '*': self.multiple,
            '/': self.division
        }


    def plus(self, a, b=None):
        if b is None and hasattr(a, '__iter__'):
            result = sum(a)
            print(result)
            return result
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            print(result)
            return result
        else:
            print('Invalid input')
            return None

    def calculate_from_input(self, data=None):
        pattern = r'^(-?\d+(?:\.\d+)?)([+\-*/])(-?\d+(?:\.\d+)?)$'
        while True:
            if data is None:
                data = input('Enter data: ')

            parse_data = re.fullmatch(pattern, data)

            if parse_data:
                a = float(parse_data.group(1))
                op = parse_data.group(2)
                b = float(parse_data.group(3))

                if op in self.operations:
                    self.operations[op](a, b)
                    break
            else:
                print('not valid data, try again')
                data = None



if __name__ == '__main__':
    c = ModifiedCalc()
    c.calculate_from_input()
