import datetime

from src.logger_utils.logger import Logger


class Calculation(object):

    datetime_mapper = {'sec': 1, 'min': 60, 'hour': 3600, 'day': 86400}

    def __init__(self, id, variable1, variable2, operator, variable2_type=None):
        self.id = id
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
            self.variable2 = int(self.variable2)
        except ValueError:
            self.is_valid_operation = False
            self.result = "No result! Cause: Illegal operand type!"

    def execute_operation(self):
        if self.operator == 'plus':
            self.result = self.variable1 + self.variable2 \
                if self.variable2_type == None \
                else self.variable1 \
                     + datetime.timedelta(seconds=self.variable2 * Calculation.datetime_mapper[self.variable2_type])
        elif self.operator == 'minus':
            self.result = self.variable1 - self.variable2 \
                if self.variable2_type == None \
                else self.variable1 \
                     - datetime.timedelta(seconds=self.variable2 * Calculation.datetime_mapper[self.variable2_type])
        elif self.operator == 'multi':
            self.result = self.variable1 * self.variable2
        elif self.operator == 'div':
            if self.variable2 != 0:
                self.result = self.variable1 / self.variable2
                self.result = round(self.result, 1)
            else:
                self.is_valid_operation = False
                self.result = "No result! Cause: Division by Zero!"
        else:
            self.is_valid_operation = False
            self.result = "No result! Cause: Illegal operator!"

        if self.is_valid_operation and isinstance(self.result, float) and int(self.result) == 85:
            self.log_to_file()

    def log_to_file(self):
        if Logger.filename_to_log is not None:
            Logger.log_into_file(self.id, self.result)


