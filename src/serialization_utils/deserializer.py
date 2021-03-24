import json
from json import JSONDecodeError

from src.calculation_utils.calculation import Calculation


class Deserializer(object):

    @staticmethod
    def deserialize_json_file(resource_url):
        json_string_from_file = Deserializer.read_json_file(resource_url)
        if json_string_from_file is not None:
            try:
                decoded_json = json.loads(json_string_from_file)
                calculation_object_list = Deserializer.create_calculation_objects_from_decoded_json(decoded_json)
                return calculation_object_list
            except JSONDecodeError:
                print("Incorrect JSON format")

        return None

    @staticmethod
    def read_json_file(resource_url):
        try:
            f = open(resource_url, "r")
            json_string = (f.read())
            return json_string
        except OSError:
            print("File reading problem has occured!")
            return None

    @staticmethod
    def create_calculation_objects_from_decoded_json(decoded_json):
        task_calc_object_dict = {}
        for task_dict in decoded_json:
            for task, calc_list in task_dict.items():
                task_calc_object_dict[task] = []
                for calc_dict in calc_list:
                    task_calc_object_dict[task].append(Calculation(calc_dict["id"],
                                                        calc_dict["variable1"],
                                                        calc_dict["variable2"],
                                                        calc_dict["variable2-type"]
                                                        if "variable2_type" in calc_dict
                                                        else None)
                                            )
        return task_calc_object_dict
