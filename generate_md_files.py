import os
from airtable_table import (
    get_table_data_list,
    AllInstrumentTableCols as Cols,
)
from pyairtable.api.types import RecordDict
from templates import get_device_template
from utils import (
    construct_slugs_by_cat,
    ensure_dirs,
    get_keywords,
    get_py_code_tabs,
    add_space_after_angle,
)
from generate_snippets import generate_snippets
from tqdm.auto import tqdm


def generate_md_files(base_path: str):
    table_list = get_table_data_list()
    for record in tqdm(table_list, total=len(table_list)):
        process_record(record, base_path)


def process_record(record: RecordDict, base_path: str):
    fields = record.get("fields", {})
    categories = fields.get(Cols.category, [])
    slug = (
        fields[Cols.docs_wiki].replace("/instruments-wiki", "instruments-database")
        if Cols.docs_wiki in fields and fields.get(Cols.docs_wiki, None)
        else f"instruments-database/{categories[0]}/{fields[Cols.vendor]}/{fields.get(Cols.device_name,'').replace(' ', '-')}"
    )
    constructed_slugs = construct_slugs_by_cat(categories, slug)
    title = f"Connecting to {fields[Cols.correct_device_name]} by {fields[Cols.vendor]} in Python"
    vendor = fields[Cols.vendor]
    for file_path, category in constructed_slugs:
        ensure_dirs(base_path, file_path + ".mdx")
        device_name = fields[Cols.device_name]
        corrected = fields[Cols.correct_device_name]
        device_name = corrected if corrected and corrected != "" else device_name
        tabs = get_py_code_tabs(
            device_name=device_name,
            lib=fields[Cols.library],
            category=category,
            manufacturer=vendor,
        )
        keywords = (
            "keywords: ["
            + get_keywords(
                category=category,
                lib=fields.get(Cols.library, ""),
                vendor=fields[Cols.vendor],
            )
            + "]"
        )
        template = get_device_template(
            title=title,
            sidebar_label=fields.get(Cols.correct_device_name, ""),
            description=fields.get(Cols.description, ""),
            category=category,
            device_spec=fields.get(Cols.device_specification, ""),
            meta_image=fields.get(Cols.device_image_url, ""),
            slug=file_path,
            vendor=fields.get(Cols.vendor, ""),
            vendor_description=fields.get(Cols.vendor_desc, ""),
            vendor_headquarter=fields.get(Cols.headquarters, ""),
            vendor_logo_url=fields.get(Cols.vendor_logo_url, ""),
            vendor_revennue=fields.get(Cols.revenue, ""),
            vendor_website=fields.get(Cols.vendor_website, ""),
            keywords=keywords,
            second_tab_item=tabs,
        )
        template = add_space_after_angle(template)
        with open(os.path.join(base_path, file_path.strip() + ".mdx"), "w") as f:
            f.write(template.strip())


if __name__ == "__main__":
    import argparse

    # Create a parser object
    parser = argparse.ArgumentParser(
        description="A simple command-line argument parser"
    )

    # Define command-line arguments
    parser.add_argument(
        "-d", "--dir", type=str, help="Instruments database directory path"
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the parsed arguments
    docs_dir = args.dir if args.dir != "" else os.path.join(os.curdir, "docs")

    generate_snippets()
    generate_md_files(
        base_path=docs_dir.replace("\\", "/").replace("/instruments-database", "")
    )
