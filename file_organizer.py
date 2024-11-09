import os  # OS interaction functions for file and directory operations
from pathlib import Path  # Object-oriented file path handling
import shutil  # Functions for copying and moving files and directories
import logging  # Log messages for error tracking
import json  # For loading configuration from JSON files


# Configure logging to record activity and errors in the specified log file
log_file = 'logs/file_organizer.log'
os.makedirs('logs', exist_ok=True)  # Ensure the logs directory exists
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_extensions(config_file='extensions.json'):
    """
    Load file extensions from a JSON configuration file. If the file is not found or 
    an error occurs, default categories are returned.

    Args:
        config_file (str): Path to the JSON configuration file.

    Returns:
        dict: Dictionary of file extensions and their corresponding folder names.
    """
    default_extensions = {'.txt': 'TextFiles', '.jpg': 'ImageFiles', '.pdf': 'PDFFiles'}

    try:
        with open(config_file, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f'Error loading extensions config: {str(e)}')
        return default_extensions

def organize_files(target_folder):
    """
    Organize files in the target directory by moving them into subfolders based on their extensions.

    Args:
        target_folder (str or Path): The path to the folder where files will be organized.

    Raises:
        FileNotFoundError: If the target folder does not exist.
    """
    extensions = load_extensions()  # Load file extension categories from config file
    target_folder = Path(target_folder)

    try:
        if not target_folder.exists():
            raise FileNotFoundError(f"The folder {target_folder} does not exist.")

        # Create subfolders based on the extension categories in the config
        for folder in extensions.values():
            (target_folder / folder).mkdir(exist_ok=True)

        # Filter files based on extensions in the config
        for file in target_folder.glob('*.*'):  # Matches all files in the target folder
            extension = file.suffix.lower()

            # Skip files whose extension is not in the config
            if extension not in extensions:
                logging.info(f'Skipping file: {file} (Unsupported extension)')
                continue

            # Determine destination folder based on file extension
            dest_folder = target_folder / extensions[extension]
            dest_file = dest_folder / file.name

            # Avoid overwriting existing files by renaming if necessary
            counter = 1
            while dest_file.exists():
                dest_file = dest_folder / f"{file.stem}_{counter}{file.suffix}"
                counter += 1

            # Move the file to the appropriate folder
            shutil.move(str(file), str(dest_file))

            # Log the file movement for tracking
            logging.info(f'Moved file: {file} -> {dest_file}')

    except FileNotFoundError as e:
        logging.error(f'Error: {str(e)}')
    except Exception as e:
        logging.error(f'Unexpected error: {str(e)}')

if __name__ == '__main__':
    # Test the file organization with a specific folder
    organize_files('test_folder')
