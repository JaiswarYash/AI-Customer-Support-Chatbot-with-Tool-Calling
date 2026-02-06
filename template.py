import logging
import os
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "AI Customer Support Chatbot with Tool Calling"

list_of_files = [
    '.env',
    '.env.example',
    'requirements.txt',
    'app.py',
    'src/__init__.py',
    'src/main.py',
    'src/graph.py',
    'src/tools.py',
    'src/message_handler.py',
    'src/image_processor.py',
    'src/database.py',
    'src/utils.py',
    'src/config.py',
    'database/.gitkeep',
    'upload/.gitkeep',
    'log/.gitkeep',
    'templates/index.html',
    'static/css/style.css',
    'static/css/.gitkeep',
    'static/js/chat.js',
    'static/js/gitkeep'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if not exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    # Create empty file if not exists OR file is empty
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
