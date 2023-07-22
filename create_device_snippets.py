import numpy as np
from tqdm.auto import tqdm
from query_chatgpt import query_chatgpt
import os
import pandas as pd
from load_data import Cols

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
        device_path = f"{snippets_dir}/{device_file}.txt"
        if os.path.isfile(device_path):
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

        with open(device_path, "w") as f:
            f.write(code) 
