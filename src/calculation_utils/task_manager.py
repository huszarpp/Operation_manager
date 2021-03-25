import sys


class TaskManager(object):

    def __init__(self, task_calculationlist_dict):
        self.task_calculationlist_dict = task_calculationlist_dict

    def get_task_calculationlist_dict(self):
        return self.task_calculationlist_dict.copy()

    def execute_all_task(self):
        if self.task_calculationlist_dict is None:
            print("Task Manager: missing data!")
            sys.exit()
        else:
            for task, calculation_list in self.task_calculationlist_dict.items():
                current_task = self.task_calculationlist_dict[task]
                for calculation in current_task:
                    calculation.calculate()
                    print(calculation.result)
