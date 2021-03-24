import datetime


class Calculation(object):

    datetime_mapper = {'sec': '%S', 'min': '%S', 'hour': '%S', 'day': '%S', 'month': '%S', 'year': '%S'}

    def __init__(self, __id, variable1, variable2, operator, variable2_type=None):
        self.__id = __id
        self.variable1 = variable1
        self.variable2 = variable2
        self.operator = operator
        self.variable2_type = variable2_type

        self.is_valid_operation = True
        self.result = None

    def calculate(self):
        self.convert_operands()
        if self.is_valid_operation:
            self.execute_operation()

    def convert_operands(self):
        if self.variable2_type is None:
            self.convert_float_operands()
        elif self.variable2_type in Calculation.datetime_mapper:
            self.convert_datetime_operands()
        else:
            self.is_valid_operation = False
            self.result = "No result! Cause: Illegal operand type!"

    def convert_float_operands(self):
        try:
            self.variable1 = float(self.variable1)
            self.variable2 = float(self.variable2)
        except ValueError:
            self.is_valid_operation = False
            self.result = "No result! Cause: Illegal operand type!"

    def convert_datetime_operands(self):
        try:
            self.variable1 = datetime.datetime.strptime(self.variable1, '%Y-%m-%d %H:%M:%S')
            self.variable2 = datetime.datetime.strptime(self.variable2, Calculation.datetime_mapper[self.variable2_type])
        except ValueError:
            self.is_valid_operation = False
            self.result = "No result! Cause: Illegal operand type!"

    def execute_operation(self):
        if self.operator == 'plus':
            self.result = self.variable1 + self.variable2
        elif self.operator == 'minus':
            self.result = self.variable1 - self.variable2
        elif self.operator == 'multi':
            self.result = self.variable1 * self.variable2
        elif self.operator == 'div':
            if self.variable2 != 0:
                self.result = self.variable1 / self.variable2
            else:
                self.is_valid_operation = False
                self.result = "No result! Cause: Division by Zero!"
        else:
            self.is_valid_operation = False
            self.result = "No result! Cause: Illegal operator!"
