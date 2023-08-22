import numpy as np
from tqdm.auto import tqdm
from query_chatgpt import query_chatgpt, query_python_lib_desc
import os
import pandas as pd
from load_data import Cols
import re


def create_device_snippets(df: pd.DataFrame, snippets_dir: str) -> None:
    """Creates the code snippets for each device by querying chatGPT with the docstring"""
    os.makedirs(snippets_dir, exist_ok=True)

    for idx, row in tqdm(df.iterrows(), total=len(df)):
        library = row[Cols.library]
        device_name = row[Cols.device_name]
        corrected = row[Cols.correct_device_name]
        device = corrected if corrected is not np.nan else device_name

        # Don't redo one that already exists
        device_file = device.replace("/", "-")
        device_file = device_file.replace("/", "").replace("_", "-").replace(",", "")
        device_file = re.sub(r"\s+", "-", device_file).strip("-")
        device_file = device_file.replace("&", "")

        device_path = f"{snippets_dir}/{device_file}.txt"
        if os.path.isfile(device_path):
            continue

        lib_desc_path = (
            f'{snippets_dir.lower().replace(" ", "-")}/{library}_description.txt'
        )
        if os.path.isfile(lib_desc_path):
            continue

        category = row[Cols.category]
        # For some reason they are sometimes formatted as '"['text']"'
        if isinstance(category, list):
            category = category[0]
        elif isinstance(category, str) and "[" in category:
            category = eval(category)[0]
        elif category is np.nan:
            category = ""
        docstring = row[Cols.docstring]
        code = query_chatgpt(library, device, category, docstring)
        lib_desc = query_python_lib_desc(library)

        with open(device_path, "w") as f:
            f.write(code)

        with open(lib_desc_path, "w") as f:
            f.write(lib_desc)
