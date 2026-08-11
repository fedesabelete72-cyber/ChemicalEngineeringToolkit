from pathlib import Path

# Get the project folder
BASE_DIR = Path(__file__).resolve().parent

# Create the full path to data/history.txt
HISTORY_FILE = BASE_DIR / "data" / "history.txt"

# Make sure the data folder exists
HISTORY_FILE.parent.mkdir(exist_ok=True)

# Make sure the history file exists
HISTORY_FILE.touch(exist_ok=True)


def save_history(history):
    with open(HISTORY_FILE, "a") as file:
        for item in history:
            file.write(item + "\n")


def load_history():
    with open(HISTORY_FILE, "r") as file:
        return file.readlines()


def clear_history():
    with open(HISTORY_FILE, "w"):
        pass