import os
import pandas as pd
from airtable_table import get_table_data_list
import numpy as np


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
