import os
import pandas as pd
import airtable

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
    

def load_data():
    if os.path.isfile(LOCAL_FILE_NAME):
        return pd.read_csv(LOCAL_FILE_NAME)
    at = airtable.Airtable('appltTe3yZzVV3Ouj', AIRTABLE_API_KEY)
    all_data = []
    offset = None
    while True:
        data = at.get("All Instrument Devices", limit=100, offset=offset)
        all_data.extend(data["records"])
        offset = data.get("offset")
        if not offset:
            break

    df = pd.DataFrame([row["fields"] for row in all_data])
    df.to_csv("device_data.csv", index=False)
    return df

df = load_data()
df.head(2)
