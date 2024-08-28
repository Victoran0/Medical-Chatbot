import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# creating files from python os
# / are used for filepath in linux and mac, \ are used in windows, to prevent isssues originating from this, we have to use the Path library (pathlib) with restpect to our os
list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    'setup.py',
    'research/trials.ipynb',
    'app.py',
    'store_index.py',
    'static/index.css',
    'templates/chat.html'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # seperating the folders from files
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        # Exist ok bool checks if the dir exists already and does not overwrite the existing dir
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")

# we can also chceck using the size (os.path.getsize(filepath) == 0) read the doc for more info
