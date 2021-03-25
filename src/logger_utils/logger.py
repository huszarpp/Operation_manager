import datetime


class Logger(object):

    @staticmethod
    def log_into_file(filename, __id, result):
        try:
            f = open("output/" + filename, "a")
            f.write("INFO   id: " + str(__id) + "  result: " + str(result)
                      + "   " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.close()
        except OSError:
            print("File writing problem has occurred!")
