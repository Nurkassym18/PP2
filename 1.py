class time:
    def __init__ (self,hours,minutes,seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def  __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def increment_sec(self):
        self.seconds+=1
        if self.seconds == 60:
            self.minutes +=1
            self.seconds=0
            if self.minutes>=60:
                self.hours+=1
                self.minutes=0
                if self.hours>=24:
                    self.hours=0


t1 = time(11,58,59)
print(str(t1))
t1.increment_sec()
print(t1)

