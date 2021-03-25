import datetime


class Logger(object):

    filename_to_log = None

    @staticmethod
    def set_filename_to_log(filename):
        Logger.filename_to_log = "output/" + filename

    @staticmethod
    def log_into_file(id, result):
        try:
            f = open(Logger.filename_to_log, "a")
            f.write("INFO   id: " + str(id) + "  result: " + str(result)
                      + "   " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.close()
        except OSError:
            print("File writing problem has occurred!")
