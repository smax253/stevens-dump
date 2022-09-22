'''
Created on 11/24/18
@author:   Max Shi
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''
        Decides if self and d2 
        represent the same calendar date,
        whether or not they are the in the same place in memory.
        '''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day

    def tomorrow(self):
        """Changes the object to represent the following day"""
        if self.day >= DAYS_IN_MONTH[self.month]:
            if self.month == 2 and self.isLeapYear() and self.day == 28:
                self.day += 1
            elif self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
            else: 
                self.month += 1
                self.day = 1
        else:
            self.day += 1
    
    def yesterday(self):
        """Changes the object to represent the previous day"""
        if self.day == 1:
            if self.month == 3 and self.isLeapYear():
                self.month -= 1
                self.day = 29
            elif self.month == 1:
                self.month = 12
                self.year -= 1
                self.day = DAYS_IN_MONTH[self.month]
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
    
    def addNDays(self, N):
        """Adds N days to this object"""
        print(str(self))
        for day in range(N):
            self.tomorrow()
            print(str(self))
        
    def subNDays(self, N):
        """Subtracts N days from this object"""
        print(str(self))
        for day in range(N):
            self.yesterday()
            print(str(self))
    
    def isAfter(self, d2):
        """Returns whether this object's date is after d2"""
        if d2.year < self.year:
            return True
        elif d2.year == self.year:
            if d2.month < self.month:
                return True
            elif d2.month == self.month:
                if d2.day < self.day:
                    return True
        return False

    def isBefore(self, d2):
        """Returns whether this object's date is before d2"""
        if d2.year > self.year:
            return True
        elif d2.year == self.year:
            if d2.month > self.month:
                return True
            elif d2.month == self.month:
                if d2.day > self.day:
                    return True
        return False

    def diff(self, d2):
        """Returns the difference between two days, will be negative is d2 is before this object's date"""
        numDiff = 0
        copySelf = self.copy()
        while copySelf.isBefore(d2):
            copySelf.tomorrow()
            numDiff -= 1
        while copySelf.isAfter(d2):
            copySelf.yesterday()
            numDiff += 1
        return numDiff
    
    def dow(self):
        """Returns the day of the week of this date"""
        daysOfWeek = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
        refSunday = Date(11,25,2018)
        difference = self.diff(refSunday)
        return daysOfWeek[difference%7]