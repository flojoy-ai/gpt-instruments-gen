import os
import pandas as pd
import airtable
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
    github_link = "GitHub link to Python driver (NOT LINK TO DOCS ON GITHUB)"
    vendor = "Vendor"
    vendor_website = "Vendor website"
    vendor_desc = "Vendor wikipedia or cruncbase description"
    category = "Device Category"
    headquarters = "Vendor headquarters"
    revenue = "Yearly revenue (millions, USD)"
    device_picture = "Device picture"
    device_image_url = "Image URL"
    vendor_logo = "Vendor logo"
    vendor_logo_url = "Vendor logo URL"


def use_device_name_when_no_correct(row: pd.Series):
    if (row[Cols.correct_device_name] is np.nan) or (
        row[Cols.correct_device_name] == "??"
    ):
        return row[Cols.device_name]
    return row[Cols.correct_device_name]


def load_data():
    if os.path.isfile(LOCAL_FILE_NAME):
        return pd.read_csv(LOCAL_FILE_NAME)
    at = airtable.Airtable("appltTe3yZzVV3Ouj", AIRTABLE_API_KEY)
    all_data = []
    offset = None
    while True:
        data = at.get("All Instrument Devices", limit=100, offset=offset)
        all_data.extend(data["records"])
        offset = data.get("offset")
        if not offset:
            break

    df = pd.DataFrame([row["fields"] for row in all_data])
    df = df[~df[Cols.device_name].isna()]
    df[Cols.correct_device_name] = df.apply(use_device_name_when_no_correct, axis=1)
    df.to_csv("device_data.csv", index=False)
    return df


df = load_data()
df.head(2)
