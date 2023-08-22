import requests
import numpy as np
from tempfile import TemporaryDirectory
import os


def get_raw_link_from_gist(gist_url: str) -> str:
    gist_url = gist_url.rstrip("/")
    parts = gist_url.split("/")
    username = parts[-2]
    gist_id = parts[-1]
    api_url = f"https://api.github.com/gists/{gist_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            gist_data = response.json()
            files = gist_data["files"]
            first_file = next(iter(files.values()))
            return first_file["raw_url"]
        except (KeyError, ValueError):
            pass
    return None


def get_raw_link_from_file(file_link: str) -> str:
    raw_link = file_link.replace("blob/", "").replace(
        "github.com", "raw.githubusercontent.com"
    )
    return raw_link


def get_code_from_notebook(notebook_code: str) -> str:
    """Converts ipynb file into python file, return python code"""
    with TemporaryDirectory() as tmp_dir:
        n = "device"
        with open(f"{tmp_dir}/{n}.ipynb", "w") as fnotebook:
            fnotebook.write(notebook_code)

        os.system(f"jupyter nbconvert --to script {tmp_dir}/{n}.ipynb")
        with open(f"{tmp_dir}/{n}.py", "r") as fpy:
            pycode = fpy.read()

    return pycode


def get_raw_code_for_device(link: str) -> str:
    if link is np.nan or not link.startswith("http") or "github.com" not in link:
        return ""
    if "gist" in link:
        raw_link = get_raw_link_from_gist(link)
    else:
        raw_link = get_raw_link_from_file(link)
    res = requests.get(raw_link)
    if res.status_code != 200:
        return ""
    if link.endswith(".ipynb"):
        return get_code_from_notebook(res.text)
    return res.text
