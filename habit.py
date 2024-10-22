from datetime import datetime, timedelta, date
from enum import Enum


class Habit:
    class Frequency(Enum):
        """
        Enumeration class for defining periodicity of a habit
        """
        DAILY = "Daily"
        WEEKLY = "Weekly"
        MONTHLY = "Monthly"

    def __init__(self,
                 habit_name: str,
                 habit_frequency: Frequency,
                 creation_date: datetime
                 ):
        """
        Parameters:
        - habit_name: User inputs the name of new habit
        - habit_frequency: User inputs desired frequency
        - creation_date: User inputs date and time when habit is created
        - completion_dates: Dictionary which stores dates of completion as keys and
                            True or False as value pairs.
        """
        self._habit_name = habit_name
        self._habit_frequency = habit_frequency
        # Checking if creation date is a date object if not turn it to date object
        self._creation_date = creation_date if isinstance(creation_date, date) else creation_date.date()
        self._completion_dates = {}
        self._deadline = self.display_next_deadline(creation_date)

    def update_status(self, update_date, status):
        """Updating the completion status of a habit"""
        if isinstance(update_date, datetime):
            update_date = update_date.date()  # Convert datetime to date
        self._completion_dates[update_date] = status  # Store the update date as key and status as value

    def display_next_deadline(self, current_date: date):
        """Displaying deadline of a habit according to the defined periodicity"""
        if self._habit_frequency == Habit.Frequency.DAILY:
            return current_date + timedelta(days=1)
        elif self._habit_frequency == self.Frequency.WEEKLY:
            return current_date + timedelta(weeks=1)
        elif self._habit_frequency == self.Frequency.MONTHLY:
            return current_date + timedelta(days=30)
        else:
            raise ValueError("Invalid habit frequency")

    @property
    def habit_name(self):
        # Property decorator for accessing the name of the habit
        return self._habit_name

    @habit_name.setter
    def habit_name(self, value):
        # Setter for the new name of the habit
        print(f"{self._habit_name} is now {value}")
        self._habit_name = value

    @property
    def habit_frequency(self):
        # Property decorator for accessing the frequency of the habit
        return self._habit_frequency

    @habit_frequency.setter
    def habit_frequency(self, new_frequency: str):
        # Setter for the new frequency of the habit
        print(f"{self._habit_frequency} is now {new_frequency}")
        self._habit_frequency = new_frequency

    @property
    def creation_date(self):
        # Property decorator for accessing the creation date of the habit
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        # Setter for the new creation date of the habit
        print(f"{self._creation_date} is now {value}")
        self._creation_date = value

    @property
    def completion_dates(self):
        # Property decorator for accessing the completion dates of the habit
        return self._completion_dates

    @property
    def last_deadline(self):
        # Property decorator for accessing the last deadline of the habit
        return self._deadline

    @last_deadline.setter
    def last_deadline(self, value):
        # Setting the new last deadline until when habit must be completed
        print(f"{self._deadline} is now {value}")
        self._deadline = value

    def check_broken_habit(self) -> bool:
        """
        Checking if habit is broken based on its completion status
        If the first completion status is False, or if no completion has been recorded
        the habit is considered broken
        """
        if not self.completion_dates:
            # If no completions have been recorded, consider the habit broken
            return True
        # Get the first recorded completion status
        first_completion_date = sorted(self.completion_dates.keys())[0]
        first_completion_status = self.completion_dates[first_completion_date]
        # If the first completion status is False, the habit is broken
        return not first_completion_status

    def get_habit_streak(self):
        """Get the longest streak of specified habit"""
        current_streak = 0
        longest_streak = 0

        for dates, completed in sorted(self._completion_dates.items()):
            if completed:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 0

        # Update longest streak
        longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def __str__(self):
        """Return a string representation of the Habit object"""

        return f"Habit name: {self._habit_name} \n" \
               f"Habit frequency: {self._habit_frequency}\n" \
               f"Habit creation date: {self._creation_date}\n" \
               f"Habit completion dates: {self._completion_dates} \n" \
               f"Habit last deadline: {self._deadline} \n"


def daterange(start_date, end_date):
    """Iterating over the daterange for tracking desired habit completion dates"""
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)
