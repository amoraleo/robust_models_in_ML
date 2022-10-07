from datetime import datetime
from time import sleep


class MyTimer:
    def __init__(self, units=""):
        self.time_units = units

    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = datetime.now()
        self.spent_time = self.end - self.start

    def elapsed_time(self):
        match self.time_units:
            case "s":
                return self.spent_time.total_seconds()
            case "m":
                return self.spent_time.total_seconds() / 60
            case "h":
                return self.spent_time.total_seconds() / 3600

with MyTimer(units="s") as t:
    sleep(5)
    print("Hello world")

print(t.elapsed_time())