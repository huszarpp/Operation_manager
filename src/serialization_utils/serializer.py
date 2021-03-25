

class Serializer(object):

    def __init__(self, filename, task_calculationlist_dict):
        self.filename_to_serialize = "output/" + filename
        self.task_calculationlist_dict = task_calculationlist_dict

    def serialize_results(self):
        result_string_to_serialize = self.create_results_string()
        try:
            f = open(self.filename_to_serialize, "w")
            f.write(result_string_to_serialize)
            f.close()
        except OSError:
            print("File writing problem has occurred!")

    def create_results_string(self):
        json_string = '{\n'
        for task, calc_list in self.task_calculationlist_dict.items():
            for calc in calc_list:
                json_string += '    {"id": ' + calc.id + ', "result": ' + str(calc.result) + '},\n'
        json_string += '}'

        return json_string
