import datetime
import time

"""!
    @package data
"""


class dataTime():
    """!
    @deprecated @li @c time_t()
                @li @c read_data_file()
                @li @c write_data_file()
                @li @c get_delta_time()

    @warning This class was deprecated \n Этот класс устарел
    @brief Data/time tools component
    """

    def time_t(self):
        """!
        @brief Displays time delta in UNIX format
        @brief Выводит дельту времени в  UNIX формате
        """
        # datetime object to time tuple
        var = datetime.datetime.today() + datetime.timedelta(hours=1)
        var = var - datetime.timedelta(minutes=var.minute)
        print(int(
            time.mktime(var.timetuple())
        ))
        var1 = datetime.datetime.today()
        print(var1.strftime("%A, %d. %B %Y %I:%M%p"))
        print(var.strftime("%A, %d. %B %Y %I:%M%p"))

        print(int(
            time.mktime(var1.timetuple())
        ))
        var2 = time.mktime(var.timetuple())
        var3 = time.mktime(var1.timetuple())
        var4 = var2 - var3
        print(var4)

        wait = 60 * 60
        vol = wait * 1
        times = (time.time() + vol)
        print(int(times))

    def read_data_file(self):
        """!
        @brief Reads the last time it was run from a file
        @brief Считывает время последнего запуска из файла
        @return time(unix formate)
        """
        input_file = open('text.txt', 'r')
        old_time_run = input_file.read()
        print("OldTimeRun: " + old_time_run)
        old_time_run_var = datetime.datetime.fromtimestamp(float(old_time_run))
        print("OldTimeRun: " + old_time_run_var.strftime("%A, %d. %B %Y %I:%M%p"))
        input_file.close()
        return old_time_run_var

    def write_data_file(self):
        """!
        @brief Write the last time it was run from a file
        @brief Пишет время последнего запуска из файла
        """
        output_file = open('text.txt', 'w')
        now_time_run = datetime.datetime.now()
        print("NowTimeRun: " + now_time_run.strftime("%A, %d. %B %Y %I:%M%p"))
        output_file.write(str(time.mktime(now_time_run.timetuple())))
        output_file.close()

    def get_delta_time(self):
        """!
        @brief Calculates the delta time in UNIX format in the last 24 hours
        @brief Рассчитывает дельту времени в UNIX формате за последнии 24 часа
        """
        old_time_run_vars = dataTime.read_data_file()
        print("ReadDate: "
              + old_time_run_vars.strftime("%A, %d. %B %Y %I:%M%p"))
        now_time = time.mktime(datetime.datetime.now().timetuple())
        old_time = time.mktime(old_time_run_vars.timetuple())
        delta_time = now_time - old_time
        print(delta_time)
        if delta_time > 3600 * 24:
            print("Last 24 hour")
        else:
            print("Last less 24 hour: ", delta_time)
        return delta_time
