from habit import Habit
from datetime import datetime
from typing import List


def define_frequency() -> Habit.Frequency:
    """Returns an instance of the Frequency enumeration class"""
    input_frequency = input("Choose 'D' for Daily, 'W' for weekly, 'M' for monthly").upper()
    frequency = None

    if input_frequency == "D":
        print("Habit is defined as daily")
        frequency = Habit.Frequency.DAILY
    elif input_frequency == "W":
        print("Habit is defined as weekly")
        frequency = Habit.Frequency.WEEKLY
    elif input_frequency == "M":
        print("Habit is defined as monthly")
        frequency = Habit.Frequency.MONTHLY
    else:
        print("Invalid input. Please choose 'D', 'W', or 'M'.")

    return frequency


def create_new_habit():
    """Returns new instance of the Habit class"""
    habit_name = input("Write the name of the new habit you want to track:")
    habit_frequency = define_frequency()
    creation_date = datetime.now()

    habit = Habit(
        habit_name=habit_name,
        habit_frequency=habit_frequency,
        creation_date=creation_date
    )
    return habit


def check_off_habit(habit: Habit):
    """Mark habit as completed by choosing habit from the list of Habit objects"""
    completion_date = datetime.now()
    habit.update_status(completion_date, True)  # Updating habit date and habit status
    print("Habit marked as completed!")


def mark_habit_broken(habit: Habit):
    """Manually mark a habit as uncompleted."""
    uncompleted_date = datetime.now()
    habit.update_status(uncompleted_date, False)  # Updating habit date and habit status
    print("Habit marked as uncompleted!")


def choose_habit_from_the_list(list_of_habits: List[Habit]):
    """User chooses habit from the list by entering its index"""
    chosen_habit_index = input("Choose the index of a habit")
    chosen_habit = list_of_habits[int(chosen_habit_index)-1]
    return chosen_habit


def print_list_of_habits(list_of_habits: List[Habit]):
    """Print the list of all tracked habits"""
    for index, habit_from_list in enumerate(list_of_habits):
        print(f"Habit {index + 1}:\n{habit_from_list}")


def edit_habit_details(habit: Habit):
    """Edit specific details of the habit"""
    habit.habit_name = input("Define new name:")
    habit.habit_frequency = define_frequency()


def get_habit_with_longest_streak(list_of_habits: List[Habit]):
    """Getting the habit with the longest streak out of a list of habits
    :param: list_of_habits (List[Habit]): List containing Habit objects.
    """
    # Initialize variables to track the longest streak and its corresponding index
    longest_streak = 0
    index_of_longest_streak = -1
    for index, habit in enumerate(list_of_habits):
        streak = habit.get_habit_streak()
        print(f"streak of habit{index + 1}: {streak}")
        # Check if the current habit's streak is longer than the recorded longest streak
        if streak > longest_streak:
            longest_streak = streak
            index_of_longest_streak = index
    if index_of_longest_streak != -1:
        print(f"The habit{index_of_longest_streak + 1} has the longest streak in the list: {longest_streak}")
    else:
        print("No habits found in the list.")


def get_streaks_of_all_habits(list_of_habits: List[Habit]):
    """Obtaining streaks of all habits
    :param: list_of_habits (List[Habit]): List containing Habit objects.
    """
    for index, habit in enumerate(list_of_habits):
        print(f"Streak of habit {index+1} is: {habit.get_habit_streak()}")


def show_habits_with_same_periodicity(list_of_habits: List[Habit]):
    """Inputting desired frequency and obtaining the habits with the same frequency
    :param: list_of_habits (List[Habit]): List containing Habit objects.
    """
    input_frequency = input("Enter the frequency (daily, weekly, monthly): ").strip().lower()
    valid_frequencies = {
        "daily": Habit.Frequency.DAILY,
        "weekly": Habit.Frequency.WEEKLY,
        "monthly": Habit.Frequency.MONTHLY
    }

    if input_frequency in valid_frequencies:
        matching_habits = [habit for habit in list_of_habits
                           if habit.habit_frequency == valid_frequencies[input_frequency]]
        if matching_habits:
            # If habits with the specified periodicity are found, print them
            for index, habit in enumerate(matching_habits):
                print(f"Habit {index + 1} - Name: {habit.habit_name}")
        else:
            print(f"No habits found with {input_frequency} frequency")
    else:
        print("Invalid frequency entered. Please enter one of the following: daily, weekly, monthly.")


def get_file_name(default_filename='habits.pkl'):
    """Prompts the user for filename. If not provided, it uses the default one"""
    file_name = input("Please input the file name. (eg.'habits.pkl'): ").strip()
    if not file_name:
        file_name = default_filename
    elif not file_name.endswith('.pkl'):  # If file extension is not .pkl add it for easier recognition of the file
        file_name += '.pkl'
    return file_name
