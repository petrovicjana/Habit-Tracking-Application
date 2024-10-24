from datetime import timedelta
from functions_of_app import *
from habit import daterange
from database import *

# Setting the creation date to 4 weeks ago in order to have valid tracking data
creation_date = datetime.now() - timedelta(days=28)

habit1 = Habit(
    habit_name="Daily hydration goal",
    habit_frequency=Habit.Frequency.DAILY,
    creation_date=creation_date
)
habit2 = Habit(
    habit_name="Running",
    habit_frequency=Habit.Frequency.DAILY,
    creation_date=creation_date
)
habit3 = Habit(
    habit_name="Swimming",
    habit_frequency=Habit.Frequency.WEEKLY,
    creation_date=creation_date
)
habit4 = Habit(
    habit_name="Reading a book",
    habit_frequency=Habit.Frequency.WEEKLY,
    creation_date=creation_date
)
habit5 = Habit(
    habit_name="Outdoor adventure",
    habit_frequency=Habit.Frequency.MONTHLY,
    creation_date=creation_date
)

if __name__ == '__main__':

    list_of_habits = [habit1, habit2, habit3, habit4, habit5]
    # Obtaining 4 weeks testing period
    start_dt = (datetime.now() - timedelta(days=28)).date()
    end_dt = datetime.now().date()

    for habit in list_of_habits:
        for dt in daterange(start_dt, end_dt):  # Looping through dates in daterange
            if habit.habit_frequency == Habit.Frequency.DAILY:  # Updating habit statuses based on their frequency
                habit.update_status(dt, False)
            elif habit.habit_frequency == Habit.Frequency.WEEKLY:
                if (dt - habit.creation_date.date()).days % 7 == 0:
                    habit.update_status(dt, False)
            elif habit.habit_frequency == Habit.Frequency.MONTHLY:
                if dt.day == habit.creation_date.day:
                    habit.update_status(dt, False)
        habit.update_status(end_dt, True)  # Set the latest date's status to True for demonstration

    for habit in list_of_habits:
        # Printing 4 weeks data for each habit from the list
        print(f"Habit: {habit.habit_name}")
        for dt, status in sorted(habit.completion_dates.items()):
            print(f"  {dt}: {'Completed' if status else 'Not completed'}")

while True:
    try:
        user_choice = input("""

Enter 1 to mark the habit completed
Enter 2 to view the list of all habits
Enter 3 to choose one habit from the list
Enter 4 to create new habit
Enter 5 to delete existing habit
Enter 6 to edit habit details
Enter 7 to check for broken habits
Enter 8 to get longest streak from the list
Enter 9 to get longest streaks of all habits
Enter 10 to see habits with same periodicity
Enter 11 if you want to save information
Enter 12 if you want to load information
Enter 13 if you want to exit

""")
        if user_choice == "1":
            # User chooses habit from the list and marks it as completed
            chosen_habit = choose_habit_from_the_list(list_of_habits)
            check_off_habit(chosen_habit)

        elif user_choice == "2":
            # User accesses the list of all habits
            print_list_of_habits(list_of_habits)

        elif user_choice == "3":
            chosen_habit_from_list = choose_habit_from_the_list(list_of_habits)
            print(chosen_habit_from_list)

        elif user_choice == "4":
            # User creates new habit and appends it to the list
            new_habit = create_new_habit()
            list_of_habits.append(new_habit)
            print("New habit added to the tracking list!")

        elif user_choice == "5":
            # User chooses index of a habit and removes it
            habit_to_delete = choose_habit_from_the_list(list_of_habits)
            list_of_habits.remove(habit_to_delete)
            print("Habit deleted successfully!")

        elif user_choice == "6":
            # User chooses habit from the list and edits details
            habit_to_edit = choose_habit_from_the_list(list_of_habits)
            edit_habit_details(habit=habit_to_edit)
            print("Habit updated successfully!")

        elif user_choice == "7":
            for habit in list_of_habits:
                if habit.check_broken_habit():
                    print(f"The habit '{habit.habit_name}' is broken.")
                else:
                    print(f"The habit '{habit.habit_name}' is still active.")

        elif user_choice == "8":
            # Getting the habit with the longest streak
            get_habit_with_longest_streak(list_of_habits)

        elif user_choice == "9":
            # Getting the streaks of all habits from a list, but since we have 4 weeks pre-defined list of habits,
            # the longest streak we can get is one because only last day is marked as true and if first completion
            # status is False, habit is considered broken
            get_streaks_of_all_habits(list_of_habits)

        elif user_choice == "10":
            show_habits_with_same_periodicity(list_of_habits)

        elif user_choice == "11":
            save_data(filename=get_file_name(), habits=list_of_habits)

        elif user_choice == "12":
            habits_list = load_data(filename=get_file_name())

        else:
            print("Exiting the program. Goodbye!")
            break

    except Exception as e:
        # Display any exceptions that occur during the program execution
        print(f"Exception: {e}")
