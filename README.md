# file-organizer-tool

A Python tool that organizes files into categorized folders based on file extensions, with customizable settings and logging for error tracking.

## Features
- **Organize Files by Extension**: Automatically moves files into designated folders based on their file extensions.
- **Customizable Extension Settings**: Allows for custom extension-to-folder mappings via a JSON configuration file.
- **Logging**: Logs all actions and errors to a log file for easy tracking and debugging.

## Requirements
- **Python 3.6+**

## Installation
1. **Clone the repository**:

    ```bash
    git clone https://github.com/YourUsername/file-organizer-tool.git
    cd file-organizer-tool
    ```

2. **Install Required Libraries** (if not already installed):
   - This project uses Python's standard libraries (`os`, `pathlib`, `shutil`, `logging`, `json`). No external dependencies are required.

## Configuration
- The tool uses a JSON configuration file (`extensions.json`) to define which extensions go into which folders. You can modify this file to add or change extension-folder mappings.

### Example `extensions.json`
```json
{
    ".txt": "TextFiles",
    ".jpg": "ImageFiles",
    ".pdf": "PDFFiles",
    ".png": "ImageFiles",
    ".docx": "DocumentFiles"
}


## Usage
**1. Set Up Folder Paths:**

    In the script, specify the target folder path you want to organize by replacing 'test_folder' in the organize_files() function call.

**2.Run the Script:**

    Execute the following command to run the script and organize files in the specified folder:

```bash
    python file_organizer.py

**3. Check Logs:**

    A log file (`logs/file_organizer.log`) will be created in the `logs` directory. This file records the actions taken by the script, such as files moved and any errors encountered.

## Logging
The script generates logs in `logs/file_organizer.log`. This log file includes timestamps, file movements, skipped files (unsupported extensions), and errors for easy tracking.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
JourneySculptor 
