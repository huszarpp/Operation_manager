import json
from json import JSONDecodeError

from src.calculation_utils.calculation import Calculation


class Deserializer(object):

    def __init__(self, resource_json_url):
        self.resource_json_url = resource_json_url

    def deserialize_json_file(self):
        json_string_from_file = self.read_json_file()
        if json_string_from_file is not None:
            try:
                decoded_json = json.loads(json_string_from_file)
                task_calc_object_dict = self.create_calculation_objects_from_decoded_json(decoded_json)
                return task_calc_object_dict
            except JSONDecodeError:
                print("Incorrect JSON format")

        return None

    def read_json_file(self):
        try:
            f = open(self.resource_json_url, "r")
            json_string = (f.read())
            return json_string
        except OSError:
            print("File reading problem has occurred!")
            return None

    def create_calculation_objects_from_decoded_json(self, decoded_json):
        task_calc_object_dict = {}
        for task_dict in decoded_json:
            for task, calc_list in task_dict.items():
                task_calc_object_dict[task] = []
                for calc_dict in calc_list:
                    task_calc_object_dict[task].append(Calculation(calc_dict["id"],
                                                        calc_dict["variable1"],
                                                        calc_dict["variable2"],
                                                        calc_dict["operation"],
                                                        calc_dict["variable2-type"]
                                                        if "variable2-type" in calc_dict
                                                        else None)
                                            )
        return task_calc_object_dict
