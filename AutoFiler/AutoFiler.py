import os
import shutil
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(filename='file_mover.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_today_date():
    """Return today's date."""
    return datetime.today().date()

def create_folder(folder_path):
    """Create a folder if it does not exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logging.info(f"Created folder: {folder_path}")

def is_today(date_to_check):
    """Check if the provided date is today's date."""
    return date_to_check == get_today_date()

def is_modified_today(path):
    """Check if a file or folder was modified today."""
    try:
        modified_time = datetime.fromtimestamp(os.path.getmtime(path)).date()
        return is_today(modified_time)
    except OSError as e:
        logging.error(f"Error accessing modification time for {path}: {e}")
        return False

def move_items_to_folder(items, destination_folder):
    """Move files and folders to the destination folder."""
    for item in items:
        try:
            shutil.move(item, destination_folder)
            logging.info(f"Moved: {item}")
        except (shutil.Error, FileNotFoundError, PermissionError) as e:
            logging.error(f"Error moving {item}: {e}")

def process_directory(directory, today_folder):
    """Process the given directory to move items modified today."""
    # List to store paths of files and folders modified today
    items_to_move = []

    # List items in the top layer of the directory
    for item_name in os.listdir(directory):
        item_path = os.path.join(directory, item_name)
        if os.path.isdir(item_path) or os.path.isfile(item_path):
            if is_modified_today(item_path):
                items_to_move.append(item_path)

    # Move the collected items to the new folder
    if items_to_move:
        move_items_to_folder(items_to_move, today_folder)
        logging.info(f"Completed moving items from {directory} to {today_folder}")
    else:
        logging.info(f"No items modified today were found in {directory}.")

def main():
    # Path to the Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create a folder with today's date on the Desktop
    today_folder = os.path.join(desktop, get_today_date().strftime('%Y-%m-%d'))
    create_folder(today_folder)

    # Paths to directories
    directories = {
        "Desktop": os.path.join(desktop),
        "Downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
        "Documents": os.path.join(os.path.expanduser("~"), "Documents"),
        "Pictures": os.path.join(os.path.expanduser("~"), "Pictures")
    }

    for name, path in directories.items():
        logging.info(f"Processing {name} directory: {path}")
        process_directory(path, today_folder)

if __name__ == "__main__":
    main()
