from src.serialization_utils.deserializer import Deserializer
from src.serialization_utils.serializer import Serializer
from src.logger_utils.logger import Logger
from src.calculation_utils.task_manager import TaskManager


if __name__ == '__main__':
    deserializer = Deserializer("resources/source.json")

    Logger.set_filename_to_log("result_85.log")

    deserialized_task_calculationlist_dict = deserializer.deserialize_json_file()

    task_manager = TaskManager(deserialized_task_calculationlist_dict)
    task_manager.execute_all_task()

    serializer = Serializer("results.json", task_manager.get_task_calculationlist_dict())
    serializer.serialize_results()


