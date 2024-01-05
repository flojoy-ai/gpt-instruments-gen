import os
import pandas as pd
from airtable_table import get_table_data_list
import numpy as np
import json
from pyairtable.api.types import Fields
from typing import Literal

AIRTABLE_API_KEY = os.environ["AIRTABLE_API_KEY"]
LOCAL_FILE_NAME = "data/device_data.csv"


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
    df.to_csv("device_data.csv", index=False)
    df = df.sort_values(by="Corrected device name", ascending=True)
    df["Device Category"] = df["Device Category"].apply(
        lambda x: ", ".join(map(str, x))
    )
    df["Device Category"] = df["Device Category"].apply(lambda x: x.split(", "))
    df = df.explode("Device Category")
    df = df.sort_values(by=["Device Category", "Corrected device name"], ascending=True)

    return df


df = table_to_df()
df.head(2)


def read_from_cache(file_path: str) -> dict[str, list[Fields]]:
    if os.path.exists(file_path):
        with open(file_path, "r") as cf:
            return json.loads(cf.read())
    return {}


def cache_data(file_path: str, data: str):
    with open(file_path, "w") as f:
        f.write(data)


def get_libs_cats_map() -> (
    dict[Literal["category", "library", "manufacturer"], dict[str, list[Fields]]]
):
    if not os.path.exists("data"):
        os.mkdir("data")
    cats_map_file = os.path.join(os.curdir, "data/cats_map.json")
    libs_map_file = os.path.join(os.curdir, "data/libs_map.json")
    manufac_map_file = os.path.join(os.curdir, "data/manufacs_map.json")
    libs_map: dict[str, list[Fields]] = read_from_cache(libs_map_file)
    cats_map: dict[str, list[Fields]] = read_from_cache(cats_map_file)
    manufacs_map: dict[str, list[Fields]] = read_from_cache(manufac_map_file)

    if libs_map.__len__() < 1 or cats_map.__len__() < 1 or manufacs_map.__len__() < 1:
        cats_map.clear()
        libs_map.clear()
        manufacs_map.clear()
        table_data = get_table_data_list()
        for record in table_data:
            fields = record["fields"]
            cats = fields.get(Cols.category, [])
            for cat in cats:
                if cat in cats_map:
                    cats_map[cat].append(fields)
                else:
                    cats_map[cat] = [fields]
            lib = fields.get(Cols.library, "")
            if lib != "":
                if lib in libs_map:
                    libs_map[lib].append(fields)
                else:
                    libs_map[lib] = [fields]
            vendor = fields[Cols.vendor]
            if vendor in manufacs_map:
                manufacs_map[vendor].append(fields)
            else:
                manufacs_map[vendor] = [fields]

        cache_data(cats_map_file, json.dumps(cats_map, indent=3))
        cache_data(libs_map_file, json.dumps(libs_map, indent=3))
        cache_data(manufac_map_file, json.dumps(manufacs_map, indent=3))
    return {"category": cats_map, "library": libs_map, "manufacturer": manufacs_map}
