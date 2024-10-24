import unittest
from datetime import datetime, timedelta
from habit import Habit


class TestHabit(unittest.TestCase):
    def setUp(self):
        # Setting up new habits for testing
        date_of_creation = datetime.now()
        self.daily_habit = Habit("Sleeping", Habit.Frequency.DAILY, creation_date=date_of_creation)
        self.monthly_habit = Habit("Dentist", Habit.Frequency.MONTHLY, creation_date=date_of_creation)

    def test_creation(self):
        # Testing the proper creation of a new habit
        self.assertEqual(self.daily_habit.habit_name, "Sleeping")
        self.assertEqual(self.monthly_habit.habit_frequency, Habit.Frequency.MONTHLY)

    def test_set_and_get_habit_name(self):
        # Setting the new habit name and getting it
        self.daily_habit.habit_name = "Working"
        self.assertEqual(self.daily_habit.habit_name, "Working")

    def test_set_and_get_period(self):
        # Setting monthly's frequency to weekly and then getting the same
        self.monthly_habit.habit_frequency = Habit.Frequency.WEEKLY
        self.assertEqual(self.monthly_habit.habit_frequency, Habit.Frequency.WEEKLY)

    def test_updating_status(self):
        # Checking if we are starting with empty dictionary of completion dates
        self.assertEqual(self.daily_habit.completion_dates, {})
        # Completion dates store date and status of completion therefore we update accordingly
        update_date = datetime.now().date()
        self.daily_habit.update_status(update_date, True)
        self.assertEqual(self.daily_habit.completion_dates, {update_date: True})

    def test_streak(self):
        # Completing the habit over three consecutive days to test streak calculation
        self.daily_habit.update_status(datetime.now() - timedelta(days=2), True)
        self.daily_habit.update_status(datetime.now() - timedelta(days=1), True)
        self.daily_habit.update_status(datetime.now(), True)
        self.assertEqual(self.daily_habit.get_habit_streak(), 3)

    def test_deadline(self):
        # Setting the first completion date to yesterday to simulate the past completion
        completion_date = datetime.now() - timedelta(days=1)
        last_deadline = self.daily_habit.display_next_deadline(completion_date)  # Retrieving the initial deadline
        new_completion_date = datetime.now()
        self.daily_habit.update_status(new_completion_date, True)
        # Retrieving the new deadline after the habit has been completed the following day i.e. today
        updated_last_deadline = self.daily_habit.display_next_deadline(new_completion_date)
        self.assertNotEqual(last_deadline, updated_last_deadline)

    def test_broken_habit(self):
        """
        Simulate a broken habit by setting a missed status (False)
        and verify if the habit is considered broken
        """
        update_date = datetime.now().date()
        self.daily_habit.update_status(update_date, False)
        # After updating to False we check for broken habit
        self.assertTrue(self.daily_habit.check_broken_habit())


if __name__ == "__main__":
    unittest.main()
