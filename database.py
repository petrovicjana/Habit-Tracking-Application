import pickle
from typing import List
from habit import Habit


def save_data(filename: str, habits: List[Habit]):
    """
    Saving Habit objects using pickle serialization
    :param filename: The name of the file to save the data to
    :param habits: A list of habits to be saved
    """
    try:
        with open(filename, 'wb') as file:
            pickle.dump(habits, file)
    except Exception as e:
        print(f'Error saving habits to {filename}: {e}')


def load_data(filename: str):
    """
    Load habits from a file using pickle deserialization
    :param filename: The name of the file to load data from
    :return: List of habit objects loaded from the file
    """
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f'Error loading habits from {filename}: {e}')
