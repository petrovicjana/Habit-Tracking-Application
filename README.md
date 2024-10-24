# Habit-Tracking-Application

## Description

The purpose of this application is for users to achieve their goals by tracking and growing healthy habits. Users can define specific habits, track their progress over a period, and monitor their longest streaks. The app helps users stay consistent with their routines and provides an intuitive interface for managing habits. Whether you're looking to build better habits or break bad ones, this app offers a simple yet effective way to stay on track.

## Features

- **Defining habits**: Create habits according to your routine.
- **Tracking habits**: Check off habits as you complete them.
- **Analyzing habits**: Gain insights into overall performance and deadlines.
- **Simple user interface**: Command line interface that allows easy management.

## Directory Structure

- `habits.py`: Contains Habit and Enum class definitions and related methods.
- `functions_of_app.py`: Contains the core functionalities of the application.
- `database.py`: Serializes and deserializes tracked Habit objects using the pickle module.

## Requirements

- Python 3.x
- `pickle` module (part of the standard library)
- `datetime` module (part of the standard library)

## How to use:
- **Define new habits**: Once running, choose the option from main menu to define new habits, inputting all the details
- **Track progress**: Use the options from the main menu to track overall progress, checkoff habits, edit them etc.
- **Analyze habits**: Use the analytics options to see your achievements and failures.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Installation and usage

To install and run this project, follow these steps:

```bash
# Clone this repository
git clone https://github.com/petrovicjana/Habit-Tracking-Application.git

# Change directory to the project folder
cd Habit-Tracking-Application

# Run the application
python main.py 
