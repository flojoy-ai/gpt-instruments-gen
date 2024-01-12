import os
import json
import numpy as np
import pandas as pd
from typing import Any
from airtable_table import get_table_data_list
from pyairtable.api.types import Fields
from typing import Literal
from utils import capitalize_name, CACHE_DIR

AIRTABLE_API_KEY = os.environ["AIRTABLE_API_KEY"]
LOCAL_FILE_NAME = f"{CACHE_DIR}/device_data.csv"


class Cols:
    device_name = "Device"
    correct_device_name = "Corrected device name"
    description = "Device Description"
    library = "Library"
    vendor = "Vendor"
    docs = "Python docs link"
    docstring = "docstring"
    category = "Device Category"
    category_description = "Category Description"
    github_link = "GitHub link to Python driver (NOT LINK TO DOCS ON GITHUB)"
    vendor_website = "Vendor website"
    vendor_desc = "Vendor wikipedia or cruncbase description"
    category = "Device Category"
    headquarters = "Vendor headquarters"
    revenue = "Yearly revenue (millions, USD)"
    device_picture = "Device picture"
    device_image_url = "Image URL"
    device_specification = "Device datasheet (PDF)"
    vendor_logo = "Vendor logo"
    vendor_logo_url = "Vendor logo URL"
    docs_wiki = "Docs Wiki"


def use_device_name_when_no_correct(row: pd.Series):
    if (row[Cols.correct_device_name] is np.nan) or (
        row[Cols.correct_device_name] == "??"
    ):
        return row[Cols.device_name]
    return row[Cols.correct_device_name]


def table_to_df():
    if os.path.isfile(LOCAL_FILE_NAME):
        return pd.read_csv(LOCAL_FILE_NAME)
    table_data = get_table_data_list()
    df = pd.DataFrame([row["fields"] for row in table_data])
    df = df[~df[Cols.device_name].isna()]
    df[Cols.correct_device_name] = df.apply(use_device_name_when_no_correct, axis=1)
    df.to_csv(LOCAL_FILE_NAME, index=False)
    df = df.sort_values(by="Corrected device name", ascending=True)
    df["Device Category"] = df["Device Category"].apply(
        lambda x: ", ".join(map(str, x))
    )
    df["Device Category"] = df["Device Category"].apply(lambda x: x.split(", "))
    df = df.explode("Device Category")
    df = df.sort_values(by=["Device Category", "Corrected device name"], ascending=True)

    return df


def read_from_cache(file_path: str) -> dict[str, list[Fields]]:
    if os.path.exists(file_path):
        with open(file_path, "r") as cf:
            return json.loads(cf.read())
    return {}


def cache_data(file_path: str, data: str):
    with open(file_path, "w") as f:
        f.write(data)


def sort_mapping(mapping: dict[str, Any]):
    return dict(sorted(mapping.items()))


def get_cache_path(file_name: str):
    return f"{CACHE_DIR}/{file_name}"


def is_missing_cache(cache_files: list[dict[str, list[Fields]]]) -> bool:
    return any([mapping.__len__() < 1 for mapping in cache_files])


def get_libs_cats_map() -> (
    dict[Literal["category", "library", "manufacturer"], dict[str, list[Fields]]]
):
    if not os.path.exists("data"):
        os.mkdir("data")
    cats_map_file, libs_map_file, vendors_map_file = (
        get_cache_path("cats_map.json"),
        get_cache_path("libs_map.json"),
        get_cache_path("vendors_map.json"),
    )
    cats_map, libs_map, vendors_map = (
        read_from_cache(cats_map_file),
        read_from_cache(libs_map_file),
        read_from_cache(vendors_map_file),
    )
    if is_missing_cache([cats_map, libs_map, vendors_map]):
        cats_map.clear()
        libs_map.clear()
        vendors_map.clear()
        table_data = get_table_data_list()
        for record in table_data:
            fields = record["fields"]
            cats = fields.get(Cols.category, [])
            for cat in cats:
                cap_category = capitalize_name(cat)
                if cap_category in cats_map:
                    cats_map[cap_category].append(fields)
                else:
                    cats_map[cap_category] = [fields]
            lib = fields.get(Cols.library, "")
            if lib != "":
                if lib in libs_map:
                    libs_map[lib].append(fields)
                else:
                    libs_map[lib] = [fields]
            vendor = fields[Cols.vendor]
            vendor_cap = capitalize_name(vendor)
            if vendor in vendors_map:
                vendors_map[vendor_cap].append(fields)
            else:
                vendors_map[vendor_cap] = [fields]

        cache_data(cats_map_file, json.dumps(sort_mapping(cats_map), indent=3))
        cache_data(libs_map_file, json.dumps(sort_mapping(libs_map), indent=3))
        cache_data(vendors_map_file, json.dumps(sort_mapping(vendors_map), indent=3))
    return {"category": cats_map, "library": libs_map, "manufacturer": vendors_map}
