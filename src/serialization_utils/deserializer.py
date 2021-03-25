import json
from json import JSONDecodeError

from src.calculation_utils.calculation import Calculation


class Deserializer(object):

    resource_json_url = None

    @staticmethod
    def set_resource_json_url(url):
        Deserializer.resource_json_url = url

    @staticmethod
    def deserialize_json_file():
        json_string_from_file = Deserializer.read_json_file()
        if json_string_from_file is not None:
            try:
                decoded_json = json.loads(json_string_from_file)
                calculation_object_list = Deserializer.create_calculation_objects_from_decoded_json(decoded_json)
                return calculation_object_list
            except JSONDecodeError:
                print("Incorrect JSON format")

        return None

    @staticmethod
    def read_json_file():
        try:
            f = open(Deserializer.resource_json_url, "r")
            json_string = (f.read())
            return json_string
        except OSError:
            print("File reading problem has occurred!")
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
                                                        calc_dict["operation"],
                                                        calc_dict["variable2-type"]
                                                        if "variable2_type" in calc_dict
                                                        else None)
                                            )
        return task_calc_object_dict
