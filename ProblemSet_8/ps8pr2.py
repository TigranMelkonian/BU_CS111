#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates
#


class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    def tomorrow(self):
        """ changes the called object so that it represents one calendar
            day after the date that it originally represented.
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() and self.month == 2:
            if self.day == 28:
                self.day += 1
            elif self.day == 29:
                self.month += 1
                self.day = 1
            else:
                self.day += 1
        elif self.day == days_in_month[self.month]:
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
            self.day = 1
        else:
            self.day += 1

    def add_n_days(self, n):
        """changes the calling object so that it represents n
            calendar days after the date it originally represented.
        """
        if n == 0:
            print(self)
        else:
            print(self)
            for i in range(n):
                self.tomorrow()
                print(self)

    def __eq__(self, other):
        """returns True if the called object (self) and the argument (other) represent the same calendar date
            (i.e., if the have the same values for their day, month, and year attributes).
            Otherwise, this method should return False.
        """
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False

    def is_before(self, other):
        """ returns True if the called object represents a calendar date that occurs
            before the calendar date that is represented by other. If self and other represent
            the same day, or if self occurs after other, the method should return False.
        """
        if self == other:
            return False
        if self.year < other.year:
            return True
        elif self.year < other.year and self.month < other.month:
            return True
        elif self.year < other.year and self.month < other.month and self.day < other.day:
            return True
        else:
            return False

    def is_after(self, other):
        """ returns True if the calling object represents a calendar date that occurs after the calendar
            date that is represented by other. If self and other represent the same day, or if self occurs before other,
            the method should return False.
        """
        if self == other:
            return False
        elif not self.is_before(other):
            return True
        else:
            return False

    def diff(self, other):
        """returns an integer that represents the number of days between self and other."""
        num_days = 0
        self_copy = self.copy()
        other_copy = other.copy()
        if self == other:
            return num_days
        if self_copy.is_before(other_copy):
            while self_copy != other_copy:
                self_copy.tomorrow()
                num_days += 1
        else:
            while other_copy != self_copy:
                other_copy.tomorrow()
                num_days -= 1
        return num_days

    def day_of_week(self):
        """ returns a string that indicates the day of the week of the Date object
            that calls it. In other words, the method should return one of the following strings:
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'.
         """
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                             'Friday', 'Saturday', 'Sunday']
        known_date = Date(4, 2, 18)  # Monday
        days_diff = self.diff(known_date)
        day_of_week = day_of_week_names[-(days_diff % 7)]
        return day_of_week


