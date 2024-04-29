import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


projectName="cnnClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",

    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

#if filepath dir. doesnt exist create one
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Create directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or ( os.path.getsize(filepath) == 0) :
        with open(filepath, "w") as f:
            pass
            logging.info(f"Create empty file: {filedir}")
    else:
        logging.info(f"{filename} is already created")


