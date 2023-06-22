class Timemanager:
    # whr: sec, min, hour
    # delay: int or float
    def __init__(self, time: str, delay: int, whr: str):
        self.time = time
        self.delay = delay
        self.whr = whr
        self.reformat_data()
        self.increase()
        self.make_result()

    def reformat_data(self):
        time_split = self.time.split(':')
        # self.miliseconds = time_split[2][-4:]
        # self.seconds = int(time_split[2][:-4:])
        self.seconds = float(time_split[2].replace(',', '.'))
        self.minutes = int(time_split[1])
        self.hours = int(time_split[0])

    def increase(self):
        if self.whr == 'sec':
            self.seconds += self.delay
        elif self.whr == 'min':
            self.minutes += self.delay
        elif self.whr == 'hour':
            self.hours += self.delay

    def make_result(self):
        self.check_seconds()
        self.check_minutes()
        minutes = self.minutes
        seconds = self.seconds
        hours = self.hours
        if len(str(self.minutes)) == 1:
            minutes = '0' + str(self.minutes)
        if len(str(int(self.seconds // 1))) == 1:
            seconds = '0' + str(self.seconds)
        if len(str(self.hours)) == 1:
            hours = '0' + str(self.hours)
        # self.result = str(hours) + ':' + str(minutes) + ':' + str(seconds) + self.miliseconds
        self.result = str(hours) + ':' + str(minutes) + ':' + str(seconds).replace('.', ',')

    def check_seconds(self):
        if self.seconds - 60 >= 0:
            self.seconds -= 60
            self.minutes += 1
        self.seconds = int(self.seconds * 1000) / 1000

    def check_minutes(self):
        if self.minutes - 60 >= 0:
            self.minutes -= 60
            self.hours += 1


if __name__ == '__main__':
    time = Timemanager('02:29:28,927', 12.324, 'sec').result
    print(time)
