from pyairtable import Api
from pyairtable.api.types import RecordDict

p_list = []


token = ""


def get_all_instrument_device_table():
    api = Api(token)
    table = api.table("appltTe3yZzVV3Ouj", "All Instrument Devices")
    return table


def get_table_data_list():
    table = get_all_instrument_device_table()
    all_record: list[RecordDict] = []
    for recordList in table.iterate():
        all_record = all_record + recordList
    return all_record


class AllInstrumentTableCols:
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
