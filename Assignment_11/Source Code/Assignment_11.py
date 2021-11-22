########################################################################
##
## CS 101 Lab
## Python Class Clock
## Gabriel Flynn
## gflynn2002@gmail.com
##
## This program makes a clock class with hours minutes and seconds and prints it iterating like a real 24 hour clock
##  
## ERROR HANDLING:
##      No errors found.
##
## OTHER COMMENTS:
##      No other comments.
##
########################################################################



import time

class Clock:
    def __init__(self, hours = 24, minutes = 59, seconds = 59):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def getHours(self):
        return self.hours
    def getMinutes(self):
        return self.minutes
    def getSeconds(self):
        return self.seconds

    def itSeconds(self):
        return self.seconds + 1
    
    def setHours(self, h):
        self.hours = h
    def setMinutes(self, m):
        self.minutes = m
    def setSeconds(self, s):
        self.seconds = s
    
    def showClock(self):
        if self.seconds > 59:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > 59:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0

        print('{}:{}:{}'.format(self.hours, self.minutes, self.seconds))

        
hours = int(input('Please enter the hour: '))
minutes = int(input('\nPlease enter the minute: '))
seconds = int(input('\nPlease enter the second: '))

Time = Clock(hours, minutes, seconds)

x = 1
while x == 1:
    Time.showClock()
    Time.setSeconds(Time.itSeconds())
    time.sleep(1)