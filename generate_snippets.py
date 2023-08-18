from load_data import load_data, Cols
import os
import pandas as pd
from github_utils import get_raw_code_for_device
from create_device_snippets import create_device_snippets
from tqdm.auto import tqdm

DATA_DIR = "data"
SNIPPETS_DIR = "snippets"

LIBRARY_CACHE_MAP = {
    "PyTango": f"{DATA_DIR}/pytango.csv", 
    "QCodes": f"{DATA_DIR}/qcodes.csv", 
    "QCodes Community": f"{DATA_DIR}/qcodes_community.csv", 
    "Instrumentkit": f"{DATA_DIR}/instrumentkit.csv",
    "PyMeasure": f"{DATA_DIR}/pymeasure.csv", 
    "Instrumental": f"{DATA_DIR}/instrumental.csv",
}

LIBRARY_SNIPPET_MAP = {
    "PyTango": f"{SNIPPETS_DIR}/pytango_snippets", 
    "QCodes": f"{SNIPPETS_DIR}/qcodes_snippets", 
    "QCodes Community": f"{SNIPPETS_DIR}/qcodes_community_snippets", 
    "InstrumentKit": f"{SNIPPETS_DIR}/instrumentkit_snippets",
    "PyMeasure": f"{SNIPPETS_DIR}/pymeasure_snippets", 
    "Instrumental": f"{SNIPPETS_DIR}/instrumental_snippets",
}


def get_valid_rows() -> pd.DataFrame:
    """Return rows from df that are of a valid library"""
    df = load_data()
    valid_libs = list(LIBRARY_SNIPPET_MAP.keys())
    return df[df[Cols.library].isin(valid_libs)]


def get_data_for_lib(df: pd.DataFrame, library: str) -> pd.DataFrame:
    """Filters data for a library and loads docstring for each sample
    
    First, checks cache file, returns if exists
    """ 
    cache_file = LIBRARY_CACHE_MAP[library]
    if os.path.isfile(cache_file):
        df_lib = pd.read_csv(cache_file)
    else:
        df_lib = df[df[Cols.library] == library]
        if Cols.docstring not in df_lib.columns:
            df_lib[Cols.docstring] = df_lib[Cols.github_link].map(get_raw_code_for_device)
            df_lib.to_csv(cache_file)
    return df_lib


def process_data() -> None:
    """Entrypoint. Load the data, generate the snippets"""
    df = get_valid_rows()
    unique_libs = df[Cols.library].unique()
    print(f"[INFO] Found {len(unique_libs)} libraries\n{unique_libs}")
    for lib in unique_libs:
        print(f"[INFO] Getting data for library {lib}")
        df_lib = get_data_for_lib(df, lib)
        print(f"[INFO] Generating snippets for {lib}")
        create_device_snippets(df_lib, LIBRARY_SNIPPET_MAP[lib])

if __name__ == "__main__":
    os.makedirs(SNIPPETS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)
    process_data()
